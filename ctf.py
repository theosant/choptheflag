# Sistemas Operacionais - SSC0140

from threading import *


# a ser implementado
height = 35
lenght = 50

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


game = create_screen()

for i in game:
    for j in i:
        print(f'{j}', end=' ')
    print()
