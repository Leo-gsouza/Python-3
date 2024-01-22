from time import sleep 

valor_1 = float(input("Digite o 1º valor: "))
valor_2 = float(input("Digite o 2º valor: "))

while True:
    print("\n[1] somar\n[2] multiplicar\n[3] maior\
          \n[4] novos números\n[5] sair do programa")
    opcao = int(input("\nQual é a sua opção?\n»» "))

    if opcao == 1:
        print(f"\nA soma dos valores {valor_1} + {valor_2} = {valor_1+valor_2}")
        sleep(3)

    elif opcao == 2:
        print(f"\nO produto dos valores {valor_1} x {valor_2} = {valor_1*valor_2}")
        sleep(3)

    elif opcao == 3:
        if valor_1 > valor_2:
            print(f"\nO maior valor é {valor_1}")
            sleep(2)
        elif valor_2 > valor_1:
            print(f"\nO maior valor é {valor_2}")
            sleep(2)
        else:
            print(f"\nOs valores são iguais")
            sleep(2)

    elif opcao == 4:
        valor_1 = float(input("\nDigite o 1º valor: "))
        valor_2 = float(input("Digite o 2º valor: "))
        sleep(1.5)

    elif opcao == 5:
        print("Encerrando o programa",end="")
        sleep(0.5)
        print(".",end="")
        sleep(0.5)
        print(".",end="")
        sleep(0.5)
        print(".",end="")
        sleep(0.5)
        print(".",end="")
        sleep(0.5)
        print(".",end="")
        break
    
    else:
        print("\nOpção invalida!")
