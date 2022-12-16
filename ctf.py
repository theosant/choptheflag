# Sistemas Operacionais - SSC0140

from threading import *
from screen import Screen
from flag import Flag
from enemy import Enemy


if __name__ == "__main__":
    tela = Screen()
    flags = []
    enemies = []
    for i in range(3):
        flags.append(Flag(2*i + 1,2*i + 1))
        tela.apply_move(2*i + 1,2*i + 1,0,0,2)
    enemies.append(Enemy(5,4))
    tela.apply_move(5,4,0,0,1)
    tela.print_screen()
    enemies[0].move_enemy()
    for flag in flags:
        print(flag.is_Inside(enemies[0].y + enemies[0].dy,enemies[0].x + enemies[0].dx))
    tela.apply_move(enemies[0].y,enemies[0].x,enemies[0].dy,enemies[0].dx,1)
    tela.print_screen()
