from random import randint
from screen import Screen

# Antes de alterar a posição do enemigo na tela tem que confirmar regiões criticas
# Sugestão, o inimigo tem x,y, mas só é aplicado na tela caso não de ruim com 
# Região critica
class Enemy:
    def __init__(self, y, x):
        self.x = x
        self.y = y
    
    def move_enemy(self):
        self.dx =  randint(-1,1)
        self.dy =  randint(-1,1)
    
    

# o ctf verifica se esta em uma região critica
# caso não chama a apply move
# caso sim verifica o semaforo