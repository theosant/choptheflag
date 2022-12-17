from random import randint
import curses

class Screen:
    def __init__(self, height=35, lenght=100):
        self.height = height
        self.lenght = lenght
        self.occupied_positions = list()
        self.screen = self.create_screen()

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

if __name__ == '__main__':
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()

    stdscr.addstr(0, 0, "Chop The Flag",
              curses.A_REVERSE)

    x = 0
    y = 0
    while True:
        if stdscr.getkey() == 'q':
            curses.nocbreak()
            stdscr.keypad(False)
            curses.echo()
            curses.endwin()
            break;
        elif stdscr.getkey() == 'w' and x > 0:
            x = x - 1
        elif stdscr.getkey() == 'a' and y > 0:
            y = y - 1
        elif stdscr.getkey() == 's':
            x = x + 1
        elif stdscr.getkey() == 'd':
            y = y + 1
        stdscr.addch(x, y, '*')
        #stdscr.refresh()
