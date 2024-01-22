turma = {}

turma['aluno'] = str(input('Nome do aluno: '))
turma['media'] = float(input('Média do aluno: '))
turma['status'] = 'aprovado' if turma["media"] >= 7 else 'Reprovado'

print(f'Aluno  » {turma["aluno"]}\
      \nMédia  » {turma["media"]}\
      \nStatus » {turma["status"]}')