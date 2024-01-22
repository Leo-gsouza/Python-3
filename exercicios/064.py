soma = cont = 0
info = ""

while True:
    valor = int(input("Digite um valor » "))
    if valor == 999:
        break
    
    else:
        cont += 1
        soma += valor
        info += f"O {cont}º valor foi » {valor}\n"

print(f"A soma de todos os valores »» {soma}\
      \n{info}")
