cont = soma = 0


while cont < 5:
    cont += 1
    valor = int(input(f"Digite o {cont}º valor » "))
    soma += valor
    if cont == 1:
        maior = valor
        menor = valor
    elif valor > maior:
        maior = valor
    elif valor < menor:
        menor = valor

while True:
    opcao = str(input("Deseja continuar » ")).strip().upper()[0]
    if opcao == "N":
        break
    else:
        cont += 1
        valor = int(input(f"Digite o {cont}º valor » "))
        soma += valor
        if valor > maior:
            maior = valor
        
        if valor < menor:
            menor = valor
print(f"A media dos valores » {soma/cont:.2f}\
      \nMaior valor » {maior}\nMenor valor » {menor}")

