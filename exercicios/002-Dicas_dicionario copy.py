brasil = list()
estado1 = {'uf':'São Paulo', 'sigla': 'SP','populacao': 44.411238}
estado2 = {'uf':'Rio de Janeiro', 'sigla': 'RJ','populacao': 16.054524}
estado3 = {'uf':'Amazonas', 'sigla': 'AM','populacao': 3.941613}

brasil.append(estado1)
brasil.append(estado2)
brasil.append(estado3)

print(brasil)
print(f"{brasil[2]['uf']}\n")#Amazonas
#=======================================================================================================
estado = {}
for c in range(0,1):
    estado['uf'] = str(input('Unidade federativa: '))
    estado['sigla'] = str(input('Sigla do Estado: '))
    estado['populacao'] = float(input('População do Estado: '))
    brasil.append(estado.copy())
#===============================================================================================================
valor_maior_população = 0
nome_maior_população = ""
for dic in brasil:#acessar os dicionarios dentro da lista
    for chave, valor in dic.items():
        print(f'{chave} » {valor}')
        if chave == 'populacao' and valor > valor_maior_população:
            valor_maior_população = valor
            
        if valor == valor_maior_população:
            nome_maior_população = dic['uf']

    print('-'*20)

print(f'{nome_maior_população} com uma população de {valor_maior_população}')
    






