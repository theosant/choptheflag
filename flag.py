class Flag:
    #flag ocupa o espaço de 1+ para todas as direções inclusive diagonal
    def __init__(self,y,x):
        self.x = x
        self.y = y
        self.size = 1

    def is_Inside(self,y,x):
        if x >= self.x - self.size and x <= self.x + self.size and \
        y >= self.y - self.size and y <= self.y + self.size:
            return True
        return False