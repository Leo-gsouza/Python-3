turma = {}

turma['aluno'] = str(input('Nome do aluno: ')).strip().title()
turma['sobrenome'] = str(input(f'Sobrenome de {turma["aluno"]}: ')).strip().title()
turma['media'] = float(input(f'Média de {turma["aluno"]}: '))
if turma['media'] < 5:
      turma['status'] = 'Reprovado'
elif turma['media'] < 7:
      turma['status'] = 'Recuperação'
else:
      turma['status'] = 'Aprovado'

print(f'Aluno  » {turma["aluno"]} {turma["sobrenome"]}\
      \nMédia  » {turma["media"]}\
      \nStatus » {turma["status"]}')