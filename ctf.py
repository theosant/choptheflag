# Sistemas Operacionais - SSC0140
from random import randint
from screen import Screen
import threading as th
import time

class Character:
    def __init__(self, y = None, x = None):
        self.icon = '☻'
        self.pontuacao = 0
        self.stop = False
        self.value = False
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

    def move_apply(self):
        if self.is_valid([self.x + self.dx, self.y + self.dy]):
            self.x += self.dx
            self.y += self.dy

    def move(self,dy, dx, flags, enemies):
            #define nova posição
            # pegar entrada do player
            self.dx = dx
            self.dy = dy
            y = False
            # thread que pega as entradas do player
            #define o tipo de movimento
            for f in flags:
                next = f.is_Next_Inside(self)
                now = f.is_Now_Inside(self)
                #entra no semaforo se entrar na regiao
                if(not now and next):
                    f.Wait()
                elif (now and not next):
                    f.Resolve()
                    flags.remove(f)
                    y = self.point()
            #aply move
            self.move_apply()
            for i in enemies:
                if i.position() == self.position():
                    y = 2
            time.sleep(0.25)
            return y

    def point(self):
        self.pontuacao += 1
        if self.pontuacao == 3:
            return 1
            #tela de fim de jogo
        return 0

    def move_rand_loop(self, flags):
        while True:
            #define nova posição
            self.move_rand()

            #define o tipo de movimento
            for f in flags:
                next = f.is_Next_Inside(self)
                now = f.is_Now_Inside(self)
                #entra no semaforo se entrar na regiao
                if(not now and next):
                    f.Wait()
                elif (now and not next):
                    f.Resolve()
            #aply move
            self.move_apply()
            time.sleep(0.25)
            if self.stop:
                break

    def set_stop(self, op):
        self.stop = op

    def is_valid(self, position, height = 35,lenght = 100):
        if position[0] >= 1 and position[0] < lenght - 1 and \
            position[1] >= 1 and position[1] < height - 1:
            return True
        return False

    def position(self):
        return self.y, self.x

class Flag(Character):
    #flag ocupa o espaço de 1+ para todas as direções inclusive diagonal
    def __init__(self,y = None,x = None):
        super().__init__(y,x)
        self.size = 1
        self.semaphore = 1
        self.icon = '⚑'

    def is_Next_Inside(self, character):
        if character.x  + character.dx >= self.x - self.size and \
        character.x  + character.dx <= self.x + self.size and \
        character.y  + character.dy >= self.y - self.size and \
        character.y  + character.dy <= self.y + self.size:
            return True
        return False
    def is_Now_Inside(self, character):
        if character.x >= self.x - self.size and \
        character.x <= self.x + self.size and \
        character.y >= self.y - self.size and \
        character.y <= self.y + self.size:
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
        self.all_objects = [[],[],[]]
        self.main_character = list()
        self.threads = list()

    def start_enemies(self):
        for i in self.enemies:
            t = th.Thread(target = i.move_rand_loop, args=[self.flags])
            t.start()
            self.threads.append(t)

    def start(self):
        self.spawn(3, '⚑')
        self.spawn(30, '☻')
        self.spawn(1, '♥')

        self.screen.select_screen()

        # Inimigos
        self.start_enemies()
        # Tela
        s = th.Thread(target = self.screen.run_screen, args=[self.all_objects])
        self.threads.append(s)
        s.start()

        u = th.Thread(target = self.screen.game_screen, args=[self.main_character, self.enemies,self.flags, self.threads])
        u.start()

        u.join()


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

        if character == '⚑':
            self.all_objects.append(self.flags)
        elif character == '☻':
            self.all_objects.append(self.enemies)
        elif character == '♥':
            self.all_objects.append(self.main_character)
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
