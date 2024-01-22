numeros = []

while True:
    numero = int(input('Digite um número » '))
    if numero not in numeros:
        numeros.append(numero)
    else:
        print(f'O número {numero} já está na lista')
    
    opcao = str(input('Deseja continuar? » ')).strip().upper()[0]
    if opcao == "N":
        break
    else:
        print('')

numeros.sort()
print(f'\nLista de números\n{numeros}')