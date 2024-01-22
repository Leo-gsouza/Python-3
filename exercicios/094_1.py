
dados = []
mulheres = []
acima_da_media = []
pessoa = {}
soma_idade = 0
opcao = ""


while True:
    pessoa['nome'] = str(input(f'\nNome: ')).title()
    pessoa['idade'] = int(input(f'Idade: '))
    soma_idade += pessoa['idade']
    while True:
        pessoa['sexo'] = str(input(f'Genero: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MFHM':
            break
        print(f'Por favor! Digite apenas masculino ou feminino\
              \nSem frescura!!!')

    dados.append(pessoa.copy())
    opcao = str(input('Deseja continuar? \n» ')).strip().upper()[0]
    if opcao == 'N':
        break

print(f'A) Foram cadastradas {len(dados)} pessoas')
print(f'B) A soma das idades = {soma_idade:.0f}')
print(f'C) A média das idades = {soma_idade/len(dados):.0f}')

print(f'\nD)Lista das mulheres')
for pessoa in dados:
    if pessoa['sexo'] == "F":
        print(f'{pessoa["nome"]}',end=" │ ")
print(f"{'-'*30}")
               
print(f'\nE)Lista acima da média')
for pessoa in dados:
     if pessoa['idade'] > soma_idade/len(dados): 
        print(f"{pessoa['nome']} com {pessoa['idade']} anos",end=" │ ") 
print(f"{'-'*30}")





