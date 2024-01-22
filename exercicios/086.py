matriz = [[],[],[]]
contador = -1

for c in range(0,3):
    contador += 1
    for c in range(0,3):
        numero = int(input(f"Digite um valor [{contador}, {c}] » "))
        if contador < 1:
            matriz[0].append(numero)
        elif contador < 2:
            matriz[1].append(numero)
        else:
            matriz[2].append(numero)

print(f'\nMatriz completa » {matriz}')


print(f'[{matriz[0][0]}] [{matriz[0][1]}] [{matriz[0][2]}] ')
print(f'[{matriz[1][0]}] [{matriz[1][1]}] [{matriz[1][2]}] ')
print(f'[{matriz[2][0]}] [{matriz[2][1]}] [{matriz[2][2]}] ')