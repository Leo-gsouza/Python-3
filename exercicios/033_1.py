numeros = []
for i in range(1,4):
    numero = int(input(f"Digite o {i}º número: "))
    numeros.append(numero)
if numeros[0] == numeros[1] == numeros[2]:
    print("Os numeros são iguais")
else:
    print(f'o maior número é {max(numeros)}')
    print(f'o menor número é {min(numeros)}')