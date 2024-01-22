nome_maior_peso = nome_menor_peso = ""


for p in range(1,4):
    nome = str(input("\nNome: ")).title()
    peso = float(input(f"Peso de {nome}: Kg "))

    if p == 1:
        maior_peso = peso
        menor_peso = peso
    else:
        if peso > maior_peso:
            maior_peso = peso
            nome_maior_peso = nome
        
        if peso < menor_peso:
            menor_peso = peso
            nome_menor_peso = nome

print(f"\n{nome_maior_peso} tem o maior peso = {maior_peso:.2f}Kg\
      \n{nome_menor_peso} tem o menor peso = {menor_peso:.2f}Kg")