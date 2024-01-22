qtdd_elementos = int(input("Quantidade de elementos: "))
primeiro = 0
segundo = 1
cont = 2
print(f"{primeiro} ► {segundo} ► ",end="")
while cont < qtdd_elementos:
    sequencia = primeiro + segundo
    primeiro = segundo
    segundo = sequencia
    cont += 1
    print(f"{sequencia} ► ",end="")

print("acabou")

