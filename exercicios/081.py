numeros = []

for c in range(1,6):
    numero = int(input(f"Digite o {c}º número » "))
    numeros.append(numero)

numeros.sort(reverse=True)
print(f'\nForam digitados {len(numeros)} números')
print(f'\nA lista em ordem decrescente:\n{numeros}')
print (f'\nO valor 5 {""if 5 in numeros else "não"} foi digitado')

