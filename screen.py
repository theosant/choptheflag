import copy

class Screen:
    def __init__(self, height=35, lenght=100):
        self.height = height
        self.lenght = lenght
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

    def print_screen(self,characters):
        screen2 = copy.deepcopy(self.screen)
        for i in characters:
            screen2[i.y][i.x] = i.icon
        for i in screen2:
            for j in i:
                print(f'{j}', end='')
            print()