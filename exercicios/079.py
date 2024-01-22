numeros = []
cont = 0
fim = int(input("Quantos números deseja digitar » "))

for c in range(0,fim):
    while cont != fim:
        numero = int(input('Digite um número » '))
        if numero not in numeros:
            numeros.append(numero)
            cont += 1
        else:
            print(f'O número {numero} já está na lista')

numeros.sort()
print(numeros)