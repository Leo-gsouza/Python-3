from datetime import date 

ano_nascimento = int(input("Ano de nascimento: "))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento

if idade <= 9:
    print(f"Idade: {idade}\nCategoria Mirim")
elif  idade <= 14:
    print(f"Idade: {idade}\nCategoria Infantil")
elif  idade <= 19:
    print(f"Idade: {idade}\nCategoria Junior")
elif  idade <= 25:
    print(f"Idade: {idade}\nCategoria Sênior")
else:
    print(f"Idade: {idade}\nCategoria Master")
