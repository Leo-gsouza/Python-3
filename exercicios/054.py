from datetime import date
maior_idade = menor_idade = 0
ano_atual = date.today().year
informacao_maior = ""
informacao_menor = ""

for pes in range(1,4):
    nome = str(input("\nNome: ")).title()
    data_nascimento = int(input(f"Data de nascimento da {pes}ª pessoa: "))
    idade = ano_atual - data_nascimento
    if  idade >= 18:
        maior_idade += 1
        informacao_maior += f"{nome}, nasceu em {data_nascimento} e tem {idade} anos atualmente\n"
    else:
        menor_idade += 1
        informacao_menor += f"{nome} é menor de idade, tem apenas {idade} anos\n"

print(f"\nUm total de {maior_idade} pessoas maiores de idade que são:\
      \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\
      \n{informacao_maior}")