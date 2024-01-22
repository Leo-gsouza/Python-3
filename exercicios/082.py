numeros = []
pares = []
impares = []

while True:
    numeros.append(int(input("\nDigite um número » ")))
    opcao = str(input('Deseja continuar » ')).strip().upper()[0]
    if opcao == "N":
        break

for numero in numeros:
    pares.append(numero) if numero % 2 == 0 else impares.append(numero)

print(f'Lista completa » {numeros}\
      \nNúmeros pares » {pares}\
      \nNúmeros impares » {impares}')

