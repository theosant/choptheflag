from random import randint

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