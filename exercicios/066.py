cont = 1
soma = 0

while True:
    valor = float(input(f"Digite o {cont} valor: "))
    if valor == 999:
        break
    soma += valor
    cont += 1

print(f"A soma de todos os valores » {soma}\
      \nForam digitados {cont-1} valores")