from datetime import date
from time import sleep

funcionario = {}
funcionario['nome'] = str(input('Nome: '))
funcionario['ano_nascimento'] = int(input('Ano de nascimento: '))
funcionario['idade'] = date.today().year - funcionario['ano_nascimento'] 
funcionario['sexo'] = str(input('Sexo: ')).strip().upper()[0]
funcionario['ctps'] = int(input('CTPS: '))
if funcionario['ctps'] != 0:
    funcionario['ano_contratacao'] = int(input('Ano de contratação: '))
    funcionario['salario'] = float(input('Salario: R$'))
    if funcionario['sexo'] == 'M':
        funcionario['aposentadoria'] = (funcionario['ano_contratacao'] + 35) - funcionario['ano_nascimento']
    else:
        funcionario['aposentadoria'] = (funcionario['ano_contratacao'] + 30) - funcionario['ano_nascimento']
print('▬'*40)
for chave, valor in funcionario.items():
    print(f'{chave:>4} » {valor:<8}')
    sleep(1)