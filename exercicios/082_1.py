numeros = []
pares = []
impares = []

while True:
    numero = (int(input("\nDigite um número » ")))
    numeros.append(numero)
    pares.append(numero) if numero % 2 == 0 else impares.append(numero)    
    opcao = str(input('Deseja continuar » ')).strip().upper()[0]
    if opcao == "N":
        break

print(f'Lista completa » {numeros}\
      \nNúmeros pares » {pares}\
      \nNúmeros impares » {impares}')
