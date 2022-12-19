from random import randint
import curses
import copy
import time
import os

class Screen:
    def __init__(self, height=35, lenght=100):
        self.stop = False
        self.height = height
        self.lenght = lenght
        self.screen = self.create_screen()

        # Curses...
        self.stdscr = curses.initscr()
        curses.start_color()
        self.stdscr.resize(height, lenght)
        curses.resizeterm(height, lenght)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(False)

        curses.init_color(250, 941, 977, 930) # White
        curses.init_color(249, 910, 211, 254) # Red
        curses.init_color(248, 648, 852, 863) # Light Blue
        curses.init_color(247, 261, 477, 621) # Blue
        curses.init_color(246, 109, 203, 343) # Navy
        curses.init_pair(1, 249, curses.COLOR_BLACK) # Red in Black
        curses.init_pair(2, 248, curses.COLOR_BLACK) # Light Blue in Black
        curses.init_pair(3, 247, curses.COLOR_BLACK) # Blue in Black
        curses.init_pair(4, 250, curses.COLOR_BLACK) # Navy in Black
        '''
        curses.init_pair(1, 249, 250) # Red in White
        curses.init_pair(2, 248, 250) # Light Blue in White
        curses.init_pair(3, 247, 250) # Blue in White
        curses.init_pair(4, 246, 250) # Navy in White
        '''


    def create_screen(self):
        screen = list()
        for i in range(self.height):
            screen.append(list())

        for i in range(self.height):
            for j in range(self.lenght):
                if j == 0 or j == self.lenght - 1 or i == 0 or i == self.height - 1:
                    screen[i].append('+')
                else:
                    screen[i].append(' ')
        return screen

    def print_screen(self,characters):
        screen2 = copy.deepcopy(self.screen)
        for i in characters:
            screen2[i.y][i.x] = i.icon
        for i in screen2:
            for j in i:
                print(f'{j}', end='')
            print()

    # Funcao de gerar posicao aleatória.
    def rand_positions(self, number):
        positions = list()
        for i in range(0, number):
            heig = randint(1, self.height - 2)
            leng = randint(1, self.lenght - 2)
            position = [heig, leng]

            if position not in self.occupied_positions:
                positions.append(position)
                self.occupied_positions.append(position)
        return positions


# Mexendo com curses aqui...

    def get_key(self):
        return self.stdscr.getkey()

    def end(self):
        self.stdscr.clear()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.curs_set(True)
        curses.echo()
        curses.endwin()

    def select_screen(self):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)

        while True:
            # Impressão da imagem
            self.stdscr.addstr(0, 0, "=========================================================================\n|", curses.color_pair(4))
            self.stdscr.addstr("    ________                   ________            ________            ", curses.color_pair(3))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("   / ____/ /_  ____  ____     /_  __/ /_  ___     / ____/ /___ _____ _ ", curses.color_pair(3))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  / /   / __ \/ __ \/ __ \     / / / __ \/ _ \   / /_  / / __ `/ __ `/ ", curses.color_pair(3))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr(" / /___/ / / / /_/ / /_/ /    / / / / / /  __/  / __/ / / /_/ / /_/ /  ", curses.color_pair(3))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr(" \____/_/ /_/\____/ .___/    /_/ /_/ /_/\___/  /_/   /_/\__,_/\__, /   ", curses.color_pair(3))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("                 /_/                                         /____/    ", curses.color_pair(3))
            self.stdscr.addstr("|\n|.......................................................................|\n", curses.color_pair(4))
            self.stdscr.addstr("|                    ",                                                       curses.color_pair(4))
            self.stdscr.addstr("_  ",                                                                         curses.color_pair(3))
            self.stdscr.addstr("   _.--.____.--._                               ",                            curses.color_pair(1))
            self.stdscr.addstr("|\n|",                                                                        curses.color_pair(4))
            self.stdscr.addstr("                   ( )",                                                      curses.color_pair(3))
            self.stdscr.addstr("=.-\":;:;:;;':;:;:;\"-._                           ",                         curses.color_pair(1))
            self.stdscr.addstr("|\n|                    \\\\",                                                curses.color_pair(4))
            self.stdscr.addstr("\\:;:;:;:;:;;:;::;:;:;:\\                          ",                         curses.color_pair(1))
            self.stdscr.addstr("|\n|                     \\\\", curses.color_pair(4))
            self.stdscr.addstr("\\:;:;:;:;:;;:;:;:;:;:;\\                         ", curses.color_pair(1))
            self.stdscr.addstr("|\n|                      \\\\", curses.color_pair(4))
            self.stdscr.addstr("\\:;::;:;:;:;:;::;:;:;:\\                        ", curses.color_pair(1))
            self.stdscr.addstr("|\n|                       \\\\", curses.color_pair(4))
            self.stdscr.addstr("\\:;:;:;:;:;;:;::;:;:;:\\                       ", curses.color_pair(1))
            self.stdscr.addstr("|\n|                        \\\\", curses.color_pair(4))
            self.stdscr.addstr("\\:;::;:;:;:;:;::;:;:;:\\                      ", curses.color_pair(1))
            self.stdscr.addstr("|\n|                         \\\\", curses.color_pair(4))
            self.stdscr.addstr("\\;;:;:_:--:_:_:--:_;:;\\                     ", curses.color_pair(1))
            self.stdscr.addstr("|\n|                          \\\\", curses.color_pair(4))
            self.stdscr.addstr("\\_.-\"             \"-._\\                    ", curses.color_pair(1))
            self.stdscr.addstr("|\n|                           \\\\                                          |\n", curses.color_pair(4))
            self.stdscr.addstr("|                            \\\\                                         |\n", curses.color_pair(4))
            self.stdscr.addstr("|                             \\\\                                        |\n", curses.color_pair(4))
            self.stdscr.addstr("|                              \\\\                                       |\n", curses.color_pair(4))
            self.stdscr.addstr("|                               \\\\                                      |\n", curses.color_pair(4))
            self.stdscr.addstr("|                                \\\\                                     |\n", curses.color_pair(4))
            self.stdscr.addstr("|                                                                       |\n", curses.color_pair(4))
            self.stdscr.addstr("|                    ", curses.color_pair(4))
            self.stdscr.addstr("< Pressione 'S' para começar >", curses.A_BLINK)
            self.stdscr.addstr("                     |\n", curses.color_pair(4))
            self.stdscr.addstr("|                                                                       |\n", curses.color_pair(4))
            self.stdscr.addstr("=========================================================================\n" ,curses.color_pair(4))
            self.stdscr.refresh()

            # Verificação da tecla 'S'
            c = self.stdscr.getkey()
            if c == 's':
                break

    # Impressão por meio de 'curses'
    def print_screen(self, characters):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)
        screen2 = copy.deepcopy(self.screen)
        for c in characters:
            for i in c:
                screen2[i.y][i.x] = i.icon
        self.stdscr.move(0,0)
        for i in screen2:
            for j in i:
                self.stdscr.addch(j)

    def run_screen(self, characters):
        while True:
            self.stdscr.clear()
            self.print_screen(characters)
            self.stdscr.refresh()
            time.sleep(0.25) 

            if self.stop:
                break
            # os.system('clear')
            # self.print_screen(characters)


    def end_screen(self, enemies, threads):
        for i in enemies:
            i.set_stop(True)
        self.stop = True 

        for thread in threads:
            thread.join(0)

        self.stdscr.clear()
        

    def game_screen(self, character, enemies, flags,threads):
        # self.stdscr.clear()
        # self.print_screen2(characters)

        # Movimentação do jogador
        x = 0
        player = character[0]
        pos_y, pos_x = player.position()
        while True:
            c = self.stdscr.getkey()
            if c == 'q':  
                self.end_screen(enemies,threads)
                self.end()
                break

            elif c == 'w' and pos_y > 1:
                 x = player.move(-1, 0, flags)
            elif c == 'a' and pos_x > 1:
                pos_x = pos_x - 1
                x = player.move(0, -1, flags)
            elif c == 's' and pos_y < self.height - 2:
                x = player.move(1, 0, flags)
            elif c == 'd' and pos_x < self.lenght - 2:
                x = player.move(0, 1, flags)

            if x:
                self.end_screen(enemies,threads)
                self.parabains()
                self.end()
                break

            
            # Impressão da tela e atualização
            # self.print_screen2(characters)
            # self.stdscr.refresh()
            #time.sleep(0.05)

    def parabains(self):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)

        while True:
            # Impressão da imagem
            self.stdscr.addstr(0, 0, "=======================================================\n|", curses.color_pair(4))
            self.stdscr.addstr("     ____                   __                    __ ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("    / __ \____ __________ _/ /_  ___  ____  _____/ / ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("   / /_/ / __ `/ ___/ __ `/ __ \/ _ \/ __ \/ ___/ /  ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  / ____/ /_/ / /  / /_/ / /_/ /  __/ / / (__  )_/   ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr(" /_/    \__,_/_/   \__,_/_.___/\___/_/ /_/____(_)    ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("                                                     ")
            self.stdscr.addstr("|\n|.....................................................|\n|", curses.color_pair(4))
            self.stdscr.addstr("                                                     |", curses.color_pair(4))
            self.stdscr.addstr("\n|             ", curses.color_pair(4))
            self.stdscr.addstr("< Pressione 'Q' para sair >", curses.A_BLINK)
            self.stdscr.addstr("             |\n|", curses.color_pair(4))
            self.stdscr.addstr("                                                     |", curses.color_pair(4))
            self.stdscr.addstr("\n=======================================================\n", curses.color_pair(4))
            self.stdscr.refresh()
            # Verificação da tecla 'Q'
            c = self.stdscr.getkey()
            if c == 'q':
                break

if __name__ == '__main__':
    screen = Screen()
    screen.select_screen()
    #screen.game_screen()
    screen.end()
