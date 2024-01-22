numeros = [[],[]]

for c in range(1,7):
    numero = int(input(f'Digite o {c}º valor: '))
    
    if numero % 2 == 0:
        numeros[0].append(numero)
    else:
        numeros[1].append(numero)


print(numeros)
print(numeros[0])
print(numeros[1])
