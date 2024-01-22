idade_homem_mais_velho = mulheres_menos_20 = num_pessoas = soma_idades = 0
nome_homem_mais_velho = ""

for p in range(1,5):
    nome = str(input(f"\nNome da {p}ª pessoa: ")).strip().title()
    genero = str(input(f"Genero de {nome} [M/F]: ")).strip().upper()
    genero = genero[0]
    idade = int(input(f"Idade de {nome}: "))
    num_pessoas += 1
    soma_idades += idade
    
    if genero == "M" and idade > idade_homem_mais_velho:
        idade_homem_mais_velho = idade
        nome_homem_mais_velho = nome
    
    if genero == "F" and idade < 20:
        mulheres_menos_20 += 1

print(f"\nO homem mais velho se chama {nome_homem_mais_velho}\
      \nA quantidade de mulheres com menos de 20 anos = {mulheres_menos_20}\
      \nA média das idades = {soma_idades/num_pessoas}")
