# Sistemas Operacionais - SSC0140

from threading import *


# a ser implementado
height = 35
lenght = 100

def create_screen():
    screen = list()
    for i in range(height):
        screen.append(list())

    for i in range(height):
        for j in range(lenght):
            if j == 0 or j == lenght - 1 or i == 0 or i == height - 1:
                screen[i].append('+')
            else: 
                screen[i].append(' ')
    return screen

def print_screen(game):
    for i in game:
        for j in i:
            print(f'{j}', end='')
        print()

game = create_screen()
print_screen(game)
