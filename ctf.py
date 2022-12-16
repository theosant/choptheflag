# Sistemas Operacionais - SSC0140

from threading import *
from screen import Screen

class Game:
    def __init__(self):
        self.screen = Screen()
        self.flags = list()
        self.enemies = list()
    
    def start(self):
        self.flags = self.spawn(3, '⚑')
        self.enemies = self.spawn(3, '☻')
        self.main_character = self.spawn(1, '♥')
        self.screen.print_screen()
    
    def spawn(self, number, character):
        positions = self.screen.rand_positions(number)
        for position in positions:
            self.screen.place_character(character, position)
        return position

if __name__ == "__main__":
    game = Game() 
    game.start()
