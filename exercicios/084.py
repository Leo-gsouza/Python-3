pessoas = []
temporario = []
maior = menor = 0

while True:
    temporario.append(str(input("Nome: ")))
    temporario.append(float(input("Peso: Kg")))

    if len(pessoas) == 0:
        maior = menor = temporario[1]
    else:
        if temporario[1] > maior:
            maior = temporario[1]
        if temporario[1] < menor:
            menor = temporario[1]

    pessoas.append(temporario[:])
    temporario.clear()
   
    opcao = str(input('Deseja continuar » ')).strip().upper()[0]
    if opcao == "N":
        break

print(f'Foram cadastradas {len(pessoas)} pessoas')

print(f'Pessoas mais pesadas » ',end="")
for pessoa in pessoas:
    if pessoa[1] == maior:
        print(f'{pessoa[0]}, ',end="")

print(f'Pessoas menos pesadas » ',end="")
for pessoa in pessoas:
    if pessoa[1] == menor:
        print(f'{pessoa[0]}, ',end="")







