from random import randint
import time

class Character:

    def __init__(self, y = None, x = None):
        self.icon = '☻'
        self.stop = False
        if y == None and x == None:
            tmp = self.rand_positions()
            self.y = tmp[0][0]
            self.x = tmp[0][1]
        else:
            self.y = y
            self.x = x

    def change_icon(self,icon):
        self.icon = icon

    def move_apply(self):
        if self.is_valid([self.x + self.dx, self.y + self.dy]):
            self.x += self.dx
            self.y += self.dy

    def set_stop(self, op):
        self.stop = op

    def is_valid(self, position, height = 35,lenght = 100):
        if position[0] >= 1 and position[0] < lenght - 1 and \
            position[1] >= 1 and position[1] < height - 1:
            return True
        return False

    def position(self):
        return self.y, self.x
    
    def rand_positions(self, height = 35, lenght = 100, number = 1):
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

class Main(Character):

    def __init__(self, points=0, y = None, x = None):
        super().__init__(y, x)
        self.points = points
        
    def move(self,dy, dx, flags, enemies):
            # Define o movimento
            self.dx = dx
            self.dy = dy
            end = 0 # Nao é o fim do jogo

            for f in flags:
                _next = f.is_Next_Inside(self)
                _now = f.is_Now_Inside(self)
                #entra no semaforo se entrar na regiao
                if(not _now and _next):
                    f.Wait()
                elif (_now and not _next):
                    f.Resolve()
                    flags.remove(f)
                    end = self.point()

            # Aplicando movimento
            self.move_apply()

            # Verifica se o personaem esta no mesmo lugar
            # que o inimigo
            for i in enemies:
                if i.position() == self.position():
                    end = 2 # perdeu de jogo
            time.sleep(0.1)
            return end

    def point(self):
        self.points += 1
        if self.points == 3:
            return 1 # ganhou o jogo
        return 0

class Enemy(Character):
    def __init__(self, y = None, x = None):
        super().__init__(y, x)

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

    def move_rand(self):
        self.dx =  randint(-1,1)
        self.dy =  randint(-1,1)

        while not self.is_valid([self.x + self.dx, self.y + self.dy]):
            self.dx =  randint(-1,1)
            self.dy =  randint(-1,1)

class Flag(Character):

    # flag ocupa o espaço de 1+ para todas as direções inclusive diagonal
    def __init__(self, y = None, x = None):
        super().__init__(y, x)
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