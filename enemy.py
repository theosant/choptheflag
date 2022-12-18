from random import randint
from screen import Screen

# Antes de alterar a posição do enemigo na tela tem que confirmar regiões criticas
# Sugestão, o inimigo tem x,y, mas só é aplicado na tela caso não de ruim com 
# Região critica
# o ctf verifica se esta em uma região critica
# caso não chama a apply move
# caso sim verifica o semaforo