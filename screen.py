import curses
import copy
import time

class Screen:
    def __init__(self, height=35, lenght=100):
        self.stop = False
        self.height = height
        self.lenght = lenght

        # Curses (Teclado e tela)
        self.stdscr = curses.initscr()
        curses.start_color()
        self.stdscr.resize(height, lenght)
        curses.resizeterm(height, lenght)
        curses.cbreak()
        curses.noecho()
        curses.curs_set(False)

        # Setando cores
        curses.init_color(250, 941, 977, 930) # White
        curses.init_color(249, 910, 211, 254) # Red
        curses.init_color(248, 648, 852, 863) # Light Blue
        curses.init_color(247, 261, 477, 621) # Blue
        curses.init_color(246, 109, 203, 343) # Navy
        curses.init_pair(1, 249, curses.COLOR_BLACK) # Red in Black
        curses.init_pair(2, 248, curses.COLOR_BLACK) # Light Blue in Black
        curses.init_pair(3, 247, curses.COLOR_BLACK) # Blue in Black
        curses.init_pair(4, 250, curses.COLOR_BLACK) # Navy in Black
        curses.init_pair(5, curses.COLOR_YELLOW, curses.COLOR_BLACK)


    def end(self):
        self.stdscr.clear()
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.curs_set(True)
        curses.echo()
        curses.endwin()

    # Impressão por meio de 'curses'
    def print_screen(self, characters):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)
        self.stdscr.move(0,0)

        for i in range(self.height):
            self.stdscr.addstr(i,0,'+')
            self.stdscr.addstr(i,self.lenght-1,'+')
        for i in range(self.lenght):
            self.stdscr.addstr(0,i,'+')
            self.stdscr.addstr(self.height-1, i,'+')

        for c in characters:
            for i in c:
                if i.icon == '♥':
                    self.stdscr.addstr(i.y,i.x,i.icon, curses.color_pair(1)) # Cores
                elif i.icon == '☻':
                    self.stdscr.addstr(i.y,i.x,i.icon, curses.color_pair(5))
                else:
                    self.stdscr.addstr(i.y,i.x,i.icon)
        self.stdscr.refresh()

    # Loop de tela
    def run_screen(self, characters):
        while True:
            self.stdscr.clear()
            self.print_screen(characters)
            time.sleep(0.05)

            if self.stop:
                break

    def end_screen(self, enemies, threads):
        for i in enemies:
            i.set_stop(True)
        self.stop = True

        for thread in threads:
            thread.join(0)

        self.stdscr.clear()

    def game_screen(self, character, enemies, flags,threads):
        # Movimentação do jogador
        end = 0
        player = character[0]
        while True:
            c = self.stdscr.getkey()
            if c == 'q':
                self.end_screen(enemies,threads)
                self.end()
                break

            elif c == 'w':
                end = player.move(-1, 0, flags, enemies)
            elif c == 'a':
                end = player.move(0, -1, flags, enemies)
            elif c == 's':
                end = player.move(1, 0, flags, enemies)
            elif c == 'd':
                end = player.move(0, 1, flags, enemies)
            if end != 0:
                self.end_screen(enemies,threads)
                if end == 1:
                    self.parabains()
                else:
                    self.loose()
                self.end()
                break

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

    def loose(self):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)

        while True:
            # Impressão da imagem
            self.stdscr.addstr(0, 0, "=============================================\n|", curses.color_pair(4))
            self.stdscr.addstr("   ____                 _                  ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  |  _ \  ___  _ __  __| |  ___  _   _     ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  | |_) |/ _ \| '__|/ _` | / _ \| | | |    ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  |  __/|  __/| |  | (_| ||  __/| |_| |    ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  |_|    \___||_|   \__,_| \___| \__,_|    ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  __     __            _  _   /\/|         ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("  \ \   / /__ _   ___ (_)| | |/\/_   ___   ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("   \ \ / // _` | / __|| || | / _` | / _ \  ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("    \ V /| (_| || (__ | || || (_| || (_) | ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("     \_/  \__,_| \___||_||_| \__,_| \___/  ", curses.color_pair(1))
            self.stdscr.addstr("|\n|", curses.color_pair(4))
            self.stdscr.addstr("                                           ")
            self.stdscr.addstr("|\n|...........................................|\n|", curses.color_pair(4))
            self.stdscr.addstr("                                           |", curses.color_pair(4))
            self.stdscr.addstr("\n|       ", curses.color_pair(4))
            self.stdscr.addstr("< Press 'F' to pay respects >", curses.A_BLINK)
            self.stdscr.addstr("       |\n|", curses.color_pair(4))
            self.stdscr.addstr("                                           |", curses.color_pair(4))
            self.stdscr.addstr("\n=============================================\n", curses.color_pair(4))
            self.stdscr.refresh()

            # Verificação da tecla 'Q'
            c = self.stdscr.getkey()
            if c == 'f':
                break
