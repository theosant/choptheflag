# Sistemas Operacionais - SSC0140
from random import randint
from threading import *
from screen import Screen


class Character:
    def __init__(self, y = None, x = None):
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

        #self.screen.print_screen(self.all_objects)
        self.screen.game_screen(self.all_objects)
        self.screen.end()


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
