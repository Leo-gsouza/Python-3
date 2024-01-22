numeros = []
cont = 1 

while True:
    numeros.append(int(input(f"Digite o {cont}º número » ")))
    opcao = str(input('Deseja continuar? » ')).strip().upper()[0]
    if opcao == "N":
        break
    cont += 1

numeros.sort(reverse=True)
print(f'\nForam digitados {len(numeros)} números')
print(f'\nA lista em ordem decrescente:\n{numeros}')
print (f'\nO valor 5 {""if 5 in numeros else "não"} foi digitado')
