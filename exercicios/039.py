from datetime import date

nome = input("Nome: ")
ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade > 18:
    print(f"{nome} já se alistou há {idade - 18} ano(s)")
elif idade < 18:
    print(f"{nome} vai se alistar em {(18 - idade) + ano_atual}")
else:
    print(f"{nome} precisa se alistar este ano")