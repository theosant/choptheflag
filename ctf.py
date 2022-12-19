# Sistemas Operacionais - SSC0140
from random import randint
from threading import *
from screen import Screen
import threading as th
import time

class Character:
    def __init__(self, y = None, x = None):
        self.stop = False
        self.icon = '☻'
        if y == None and x == None:
            tmp = Game.rand_positions()
            self.y = tmp[0][0]
            self.x = tmp[0][1]
        else:
            self.y = y
            self.x = x

    def change_icon(self,icon):
        self.icon = icon

    def move_rand(self):
        self.dx =  randint(-1,1)
        self.dy =  randint(-1,1)

        while not self.is_valid([self.x + self.dx, self.y + self.dy]):
            self.dx =  randint(-1,1)
            self.dy =  randint(-1,1)

        self.x += self.dx
        self.y += self.dy

    def move_rand_loop(self, flag):
        while True:
            self.move_rand()
            time.sleep(0.25)
            if self.stop:
                break

    def set_stop(self, op):
        self.stop = op

    def is_valid(self, position, height = 35,lenght = 100):
        if position[0] > 1 and position[0] < lenght - 1 and \
            position[1] > 1 and position[1] < height - 1:
            return True
        return False

    def move(self, y, x):
        self.y = y
        self.x = x

    def position(self):
        return self.y, self.x

class Flag(Character):
    #flag ocupa o espaço de 1+ para todas as direções inclusive diagonal
    def __init__(self,y = None,x = None):
        super().__init__(y,x)
        self.size = 1
        self.semaphore = 1
        self.icon = '⚑'

    def is_Inside(self,y,x):
        if x >= self.x - self.size and x <= self.x + self.size and \
        y >= self.y - self.size and y <= self.y + self.size:
            return True
        return False

    def Wait(self):
        while True:
            if self.semaphore > 0:
                break
        self.semaphore -= 1

    def Resolve(self):
        self.semaphore += 1


class Game:
    def __init__(self):
        self.height = 35
        self.lenght = 100
        self.screen = Screen()
        self.flags = list()
        self.enemies = list()
        self.occupied_positions = list()
        self.all_objects = list()
        self.main_character = list()

    def start(self):
        self.spawn(3, '⚑')
        self.spawn(3, '☻')
        self.spawn(1, '♥')

        self.screen.select_screen()

        # Inimigos
        u = th.Thread(target = self.enemies[1].move_rand_loop, args=[self.flags])
        w = th.Thread(target = self.enemies[2].move_rand_loop, args=[self.flags])
        v = th.Thread(target = self.enemies[0].move_rand_loop, args=[self.flags])

        v.start()
        w.start()
        u.start()

        # Tela
        s = th.Thread(target = self.screen.run_screen, args=[self.all_objects])
        s.start()

        self.threads = list()
        self.threads.append(u)
        self.threads.append(v)
        self.threads.append(w)
        self.threads.append(s)

        self.screen.game_screen(self.all_objects, self.enemies, self.threads)


    def spawn(self, number, character):
        for i in range(number):
            if character == '⚑':
                aux = Flag()
                self.flags.append(aux)
            elif character == '☻':
                aux = Character()
                self.enemies.append(aux)
            elif character == '♥':
                aux = Character()
                aux.change_icon('♥')
                self.main_character.append(aux)
            self.all_objects.append(aux)

    # Funcao de gerar posicao aleatória.
    def rand_positions(number = 1,height = 35,lenght = 100):
        positions = list()
        for i in range(0, number):
            heig = randint(1, height - 2)
            leng = randint(1, lenght - 2)
            position = [heig, leng]
            if position in positions:
                positions.pop()
                i -= 1
            positions.append(position)

        return positions

    def new_occupied_position(self,positions):
        for position in positions:
            self.occupied_positions.append(position)


if __name__ == "__main__":
    game = Game()
    game.start()
