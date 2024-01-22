from random import randint
vitorias = 0
partida = 1

while True:
    print(f"\n▬▬▬▬▬▬▬▬▬ {partida}ª PARTIDA ▬▬▬▬▬▬▬▬▬▬▬")
    escolha_jogador = str(input("PAR ou IMPAR » ")).strip().upper()[0]    
    numero_jogador = int(input("Digite um número de 0 a 10 » "))
    pc = randint(0,10)
    if (numero_jogador+pc) % 2 == 0:
        soma = "PAR"
    else:
        soma = "IMPAR"

    print(f"\nComputador jogou » {pc}\
          \nJogador jogou » {numero_jogador}\
          \nResultado » {soma}")

    if escolha_jogador == soma[0]:
        print("\nParabens! Você ganhou")
        vitorias += 1
        partida += 1
    else:
        print(f"\nVocê perdeu!\nTotal de partidas vencidas » {vitorias}")
        break

