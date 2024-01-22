from random import randint
from time import sleep
ponto_jogador = 0
ponto_computador = 0
empate = 0
numero_partidas = 0

while numero_partidas <= 5:

    sleep(1)    
    jogador = str(input("Sua opção\nPapel\nPedra\nTesoura\n►► ")).strip().upper()
    computador = randint(1,3)

    if computador == 1:
        escolha_computador = "PAPEL"
    elif computador == 2:
        escolha_computador = "PEDRA"
    elif computador == 3:
        escolha_computador = "TESOURA"

    sleep(1)
    print("\nJO",end="...")
    sleep(1)
    print("KEN",end="...")
    sleep(1)
    print("PO!!!",end="...\n")
    sleep(1)

    if jogador[:2] == "PA" and computador == 2 or \
    jogador[:2] == "PE" and computador == 3 or \
    jogador[:2] == "TE" and computador == 1:
        numero_partidas += 1
        ponto_jogador += 1
        print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nJogador Venceu!\
            \nJogador escolheu    ►► {jogador}\
            \nComputador escolheu ►► {escolha_computador}\
            \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

    elif computador == 1 and jogador[:2] == "PE" or \
    computador == 2 and jogador[:2] == "TE" or \
    computador == 3 and jogador[:2] == "PA":
        numero_partidas += 1
        ponto_computador += 1
        print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nComputador Venceu!\
            \nJogador escolheu    ►► {jogador}\
            \nComputador escolheu ►► {escolha_computador}\
            \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

    else:
        numero_partidas += 1
        empate += 1 
        print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\nEmpate!\
            \nJogador escolheu    ►► {jogador}\
            \nComputador escolheu ►► {escolha_computador}\
            \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\n")

print(f"Jogador venceu ►► {ponto_jogador} vezes\
      \nComputador venceu ►► {ponto_computador} vezes\
      \nEmpate ►► {empate} vezes")
