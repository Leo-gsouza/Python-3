soma = contador = 0

for num in range(1,501,2):
    if num % 3 == 0:
        contador += 1
        soma += num

print(f"Foram encontrados {contador} números divisiveis por 3\
      \nA soma entre todos os valores é {soma}")