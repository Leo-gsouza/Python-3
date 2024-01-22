soma = 0
numeros = ""
for n in range(1,7):
    numero = int(input(f"Digite o {n}º numero: "))
    if numero % 2 == 0:
        soma += numero
        numeros += f"{numero},"

print (f"A soma dos números {numeros} é {soma}")