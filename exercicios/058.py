from random import randint
partidas = 0

while True:
    partidas += 1
    print(f"▬▬▬▬▬▬▬▬▬▬ {partidas}ª partida ▬▬▬▬▬▬▬▬▬▬")
    jogador = int(input("Escolha um número de 1 a 5 ► "))
    pc = randint(1,5)
    

    if jogador == pc:
        break
    else:
        print(f"Errou! Pc escolheu ► {pc} ▬ Você escolheu ► {jogador}\n")

print(f"Parabéns! Você ganhou depois de {partidas} partidas")

