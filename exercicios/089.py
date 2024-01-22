
alunos = int(input('Consultar a média de quantos alunos: '))
temporario = []
lista_alunos = []

for linha in range(0, alunos):
    temporario.append(str(input('Nome do aluno: ')).strip().capitalize())
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    temporario.append((nota1+nota2)/2)
    
    lista_alunos.append(temporario[:])
    temporario.clear()


nome = str(input('Qual aluno deseja consulta: ')).strip().capitalize()
for aluno in lista_alunos:
    if aluno[0] == nome:
        print(f'A média de {aluno[0]} é {aluno[1]}')




