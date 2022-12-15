from random import randint
from ctf import game

class enemy:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def move_enemy(self):
        move = randint(0, 3)

        if move == 0 and game.screen[self.x + 1][self.y] == ' ':
            self.x += 1
        elif move == 1 and game.screen[self.x - 1][self.y] == ' ':
            self.x -= 1
        elif move == 2 and game.screen[self.x][self.y + 1] == ' ':
            self.y += 1
        elif move == 3 and game.screen[self.x][self.y - 1] == ' ':
            self.y -= 1
