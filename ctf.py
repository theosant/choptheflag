# Sistemas Operacionais - SSC0140
from screen import Screen
from character import Flag
from character import Main
from character import Enemy
import threading as th

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

        self.screen.game_screen(self.main_character, self.enemies,self.flags, self.threads)

    def spawn(self, number, character):
        for i in range(number):
            if character == '⚑':
                aux = Flag()
                self.flags.append(aux)
            elif character == '☻':
                aux = Enemy()
                self.enemies.append(aux)
            elif character == '♥':
                aux = Main()
                aux.change_icon('♥')
                self.main_character.append(aux)

        if character == '⚑':
            self.all_objects.append(self.flags)
        elif character == '☻':
            self.all_objects.append(self.enemies)
        elif character == '♥':
            self.all_objects.append(self.main_character)

    def new_occupied_position(self,positions):
        for position in positions:
            self.occupied_positions.append(position)


if __name__ == "__main__":
    game = Game()
    game.start()
