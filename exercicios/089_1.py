
temporario = []
lista_alunos = []


alunos = int(input('Consultar a média de quantos alunos: '))
    
for linha in range(0, alunos):
    temporario.append(str(input('Nome do aluno: ')).strip().capitalize())
    temporario.append(float(input('1ª nota: ')))
    temporario.append(float(input('2ª nota: ')))
    media = ((temporario[1]+temporario[2])/2)
    temporario.append(media)
    lista_alunos.append(temporario[:])
    temporario.clear()

for aluno in lista_alunos:
   print(f'{aluno[0]:<10} » média {aluno[3]:>3}')

while True:
    nome = str(input('\nDeseja consultar as notas de qual aluno? » ')).strip().capitalize()
    for aluno in lista_alunos:
        if nome == aluno[0]:
            print(f'{aluno[0]} » nota1 {aluno[1]} nota2 {aluno[2]}')
            break

    opcao = str(input('\nDeseja continuar: ')).strip().upper()[0]
    if opcao == 'N':
        break


print('Finalizando............')




