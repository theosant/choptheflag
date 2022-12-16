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

    def apply_move(self,y,x,dy,dx,tipo):
        self.screen[y][x] = ' '
        if(tipo == 1):
            char = '☻'
        elif(tipo == 2):
            char = '⚑'
        self.screen[y + dy][x + dx] = char