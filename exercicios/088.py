from random import randint
from time import sleep

jogos = []
temporaria = []
cont = 0 

numero_jogos = int(input("Número de jogos » "))

for linha in range(0,numero_jogos):
    for coluna in range(0,6):
        valor = randint(1,60)
        while True:
            if valor in temporaria:
                valor = randint(1,60)
            else:
                temporaria.append(valor)
                break

    jogos.append(temporaria[:])
    jogos[-1].sort()
    temporaria.clear()

print(f'\n--------------SORTEIO--------------')
sleep(1.5)
for c in range(0,numero_jogos):
    sleep(1)
    print(f'{c+1}º Jogo » {jogos[c]}')