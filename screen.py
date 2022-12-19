from random import randint
import curses
import copy

class Screen:
    def __init__(self, height=35, lenght=100):
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
        # Positions
        #self.player = list()
        self.enemies = list()
        self.flags = list()

        curses.init_color(250, 941, 977, 930) # White
        curses.init_color(249, 910, 211, 254) # Red
        curses.init_color(248, 648, 852, 863) # Light Blue
        curses.init_color(247, 261, 477, 621) # Blue
        curses.init_color(246, 109, 203, 343) # Navy
        curses.init_pair(1, 249, 250) # Red in White
        curses.init_pair(2, 248, 250) # Light Blue in White
        curses.init_pair(3, 247, 250) # Blue in White
        curses.init_pair(4, 246, 250) # Navy in White


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

    def place_character(self, character, position):
        self.screen[position[0]][position[1]] = character
        if (character == '⚑'):
            self.flags.append(position)
        elif (character == '☻'):
            self.enemies.append(position)
        else:
            self.player = position

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
        curses.echo()
        curses.endwin()

    def select_screen(self):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)

        while True:
            self.stdscr.addstr(0, 0, "=========================================================================\n", curses.color_pair(4))
            self.stdscr.addstr("|    ________                   ________            ________            |\n",)
            self.stdscr.addstr("|   / ____/ /_  ____  ____     /_  __/ /_  ___     / ____/ /___ _____ _ |\n")
            self.stdscr.addstr("|  / /   / __ \/ __ \/ __ \     / / / __ \/ _ \   / /_  / / __ `/ __ `/ |\n")
            self.stdscr.addstr("| / /___/ / / / /_/ / /_/ /    / / / / / /  __/  / __/ / / /_/ / /_/ /  |\n")
            self.stdscr.addstr("| \____/_/ /_/\____/ .___/    /_/ /_/ /_/\___/  /_/   /_/\__,_/\__, /   |\n")
            self.stdscr.addstr("|                 /_/                                         /____/    |\n")
            self.stdscr.addstr("|.......................................................................|\n")
            self.stdscr.addstr("|                    _    _.--.____.--._                                |\n")
            self.stdscr.addstr("|                   ( )=.-\":;:;:;;':;:;:;\"-._                           |\n")
            self.stdscr.addstr("|                    \\\\\\:;:;:;:;:;;:;::;:;:;:\\                          |\n")
            self.stdscr.addstr("|                     \\\\\\:;:;:;:;:;;:;:;:;:;:;\\                         |\n")
            self.stdscr.addstr("|                      \\\\\\:;::;:;:;:;:;::;:;:;:\\                        |\n")
            self.stdscr.addstr("|                       \\\\\\:;:;:;:;:;;:;::;:;:;:\\                       |\n")
            self.stdscr.addstr("|                        \\\\\\:;::;:;:;:;:;::;:;:;:\\                      |\n")
            self.stdscr.addstr("|                         \\\\\\;;:;:_:--:_:_:--:_;:;\\                     |\n")
            self.stdscr.addstr("|                          \\\\\\_.-\"             \"-._\\                    |\n")
            self.stdscr.addstr("|                           \\\\                                          |\n")
            self.stdscr.addstr("|                            \\\\                                         |\n")
            self.stdscr.addstr("|                             \\\\                                        |\n")
            self.stdscr.addstr("|                              \\\\                                       |\n")
            self.stdscr.addstr("|                               \\\\                                      |\n")
            self.stdscr.addstr("|                                \\\\                                     |\n")
            self.stdscr.addstr("|                                                                       |\n")
            self.stdscr.addstr("|                    ")
            self.stdscr.addstr("< Pressione 'S' para começar >", curses.A_BLINK)
            self.stdscr.addstr("                     |\n")
            self.stdscr.addstr("|                                                                       |\n")
            self.stdscr.addstr("=========================================================================\n")
            self.stdscr.refresh()

            c = self.stdscr.getkey()
            if c == 's':
                break

    def print_screen2(self,characters):
        screen2 = copy.deepcopy(self.screen)
        for i in characters:
            screen2[i.y][i.x] = i.icon
        self.stdscr.move(0,0)
        for i in screen2:
            for j in i:
                self.stdscr.addch(j)

    def game_screen(self, characters):
        self.stdscr.clear()
        self.print_screen2(characters)

        # Movimentação do jogador
        player = characters[len(characters) - 1]
        pos_y, pos_x = characters[len(characters) - 1].position()
        while True:
            c = self.stdscr.getkey()
            if c == 'q':
                break
            elif c == 'w' and pos_y > 1:
                pos_y = pos_y - 1
                player.move(pos_y, pos_x)
            elif c == 'a' and pos_x > 1:
                pos_x = pos_x - 1
                player.move(pos_y, pos_x)
            elif c == 's' and pos_y < self.height - 2:
                pos_y = pos_y + 1
                player.move(pos_y, pos_x)
            elif c == 'd' and pos_x < self.lenght - 2:
                pos_x = pos_x + 1
                player.move(pos_y, pos_x)

            # Impressão da tela e atualização
            self.print_screen2(characters)
            self.stdscr.refresh()

if __name__ == '__main__':
    screen = Screen()
    screen.select_screen()
    screen.game_screen()
    screen.end()
