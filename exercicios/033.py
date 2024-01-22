numeros = []
for i in range(1,4):
    numero = int(input(f"digite {i}º numero: "))
    numeros.append(numero)

if numeros[1] == numeros[2] == numeros[0]:
    print(f"O numeros são iguais")

elif numeros[0] >= numeros[1] >= numeros[2]:
    print(f"O numero {numeros[0]} é o maior\nO numero {numeros[2]} é o menor")

elif numeros[0] >= numeros[2] >= numeros[1]:
    print(f"O numero {numeros[0]} é o maior\nO numero {numeros[1]} é o menor")

elif numeros[1] >= numeros[2] >= numeros[0]:
    print(f"O numero {numeros[1]} é o maior\nO numero {numeros[0]} é o menor")

elif numeros[1] >= numeros[0] >= numeros[2]:
    print(f"O numero {numeros[1]} é o maior\nO numero {numeros[2]} é o menor")

elif numeros[2] >= numeros[1] >= numeros[0]:
    print(f"O numero {numeros[2]} é o maior\nO numero {numeros[0]} é o menor")

elif numeros[2] >= numeros[0] >= numeros[1]:
    print(f"O numero {numeros[2]} é o maior\nO numero {numeros[1]} é o menor")





