primeiro = int(input("Informe o 1º termo: "))
razao = int(input("informe a razão: "))

for i in range(primeiro, primeiro+(razao*10), razao):
    print(f"{i}",end=" ► ")
print("Acabou")
