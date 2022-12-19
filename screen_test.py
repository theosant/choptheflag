from random import randint
import curses

class Screen:
    def __init__(self, height=100, lenght=100):
        self.height = height
        self.lenght = lenght
        self.occupied_positions = list()
        self.screen = self.create_screen()
        self.stdscr = curses.initscr()
        self.stdscr.resize(height, lenght)
        curses.resizeterm(height, lenght)
        curses.cbreak()
        curses.noecho()

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

    def print_screen(self):
        for i in self.screen:
            for j in i:
                print(f'{j}', end='')
            print()

    def place_character(self, character, position):
        self.screen[position[0]][position[1]] = character

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
        curses.nocbreak()
        self.stdscr.keypad(False)
        curses.echo()
        curses.endwin()

    def select_screen(self):
        self.stdscr.resize(100, 100)
        curses.resizeterm(100, 100)
        self.stdscr.addstr(0, 0, "=========================================================================\n")
        self.stdscr.addstr("|    ________                   ________            ________            |\n")
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
        self.stdscr.addstr("|                    < Pressione 'S' para começar >                     |\n")
        self.stdscr.addstr("|                                                                       |\n")
        self.stdscr.addstr("=========================================================================\n")
        self.stdscr.refresh()

        while True:
            c = self.stdscr.getkey()
            if c == 's':
                break

if __name__ == '__main__':
    '''
    stdscr = curses.initscr()
    #curses.noecho()
    curses.cbreak()

    stdscr.addstr(0, 0, "Chop The Flag",
              curses.A_REVERSE)

    x = 0
    y = 0
    while True:
        c = stdscr.getkey()
        if c == 'q':
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            break;
        elif c == 'w' and x > 0:
            x = x - 1
        elif c == 'a' and y > 0:
            y = y - 1
        elif c == 's':
            x = x + 1
        elif c == 'd':
            y = y + 1
        stdscr.clear()
        stdscr.addch(x, y, '*')
        stdscr.refresh()
    '''
    screen = Screen()
    screen.select_screen()
    screen.end()
