# Sistemas Operacionais - SSC0140

from threading import *

class Screen:
    def __init__(self):
        self.height = 35
        self.lenght = 100

        screen = list()
        for i in range(self.height):
            screen.append(list())

        for i in range(self.height):
            for j in range(self.lenght):
                if j == 0 or j == self.lenght - 1 or i == 0 or i == self.height - 1:
                    screen[i].append('+')
                else: 
                    screen[i].append(' ')
        self.screen = screen

    def print_screen(self):
        for i in self.screen:
            for j in i:
                print(f'{j}', end='')
            print()

if __name__ == "__main__":
    tela = Screen()
    tela.print_screen()
