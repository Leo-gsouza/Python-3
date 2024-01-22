from random import randint
from time import sleep

jogos = []
temporaria = []
cont = 0 

numero_jogos = int(input("Número de jogos » "))

for linha in range(0,numero_jogos):
    while cont != 5:
        valor = randint(1,60)
        if valor not in temporaria:
            temporaria.append(valor)
            cont += 1

    jogos.append(temporaria[:])
    jogos[-1].sort()
    temporaria.clear()
    cont = 0

print(f'\n--------------SORTEIO--------------')
sleep(1.5)
for c in range(0,numero_jogos):
    sleep(1)
    print(f'{c+1}º Jogo » {jogos[c]}')