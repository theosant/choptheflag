# Sistemas Operacionais - SSC0140

from threading import *
from screen import Screen

class Game:
    def __init__(self):
        self.screen = Screen()
        self.flags = list()
        self.enemies = list()
    
    def start(self):
        self.spawn_flags(3)
        self.spawn_enemies(3)
        self.screen.print_screen()
    
    def spawn_flags(self, number):
        self.flags = self.screen.rand_positions(number)
        for flag in self.flags:
            self.screen.place_character('⚑', flag)

    def spawn_enemies(self, number):
        self.enemies = self.screen.rand_positions(number)
        for enemy in self.enemies:
            self.screen.place_character('☻', enemy)

if __name__ == "__main__":
    game = Game() 
    game.start()
