from random import randint
from time import sleep
from operator import itemgetter

jogadores = {}

jogadores['Leonardo'] = randint(1,60)
jogadores['Natalia'] = randint(1,60)
jogadores['Thiago'] = randint(1,60)
jogadores['Larissa'] = randint(1,60)

for chave, valor in jogadores.items():
    print(f'{chave} tirou o número {valor} ')

ranking = []
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)

for indice, valor in enumerate(ranking):
    print(f'{indice+1}º lugar » {valor[0]} com {valor[1]}')
    sleep(1)
