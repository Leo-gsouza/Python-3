nota_1 = float(input("Primeira nota: "))
nota_2 = float(input("Segunda nota: "))
media = (nota_1 + nota_2) / 2

if media < 5:
    print(f"O aluno foi REPROVADO\nMédia = {media}")
elif 5 < media < 7:
    print(f"O aluno está de RECUPERAÇÃO\nMédia = {media}")
else:
    print(f"O aluno está APROVADO\nMédia = {media}")