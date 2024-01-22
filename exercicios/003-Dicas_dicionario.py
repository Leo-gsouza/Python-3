pessoa = {'nome':'Leonardo', 'idade': 34, 'sexo': 'M' }
pessoa['telefone'] = '9605-6598'#inseriu na lista a chave telefone e o valor 9605-6598
pessoa['peso'] = 97#inseriu na lista a chave peso e o valor 97
print(pessoa)
print(pessoa.values())#Exibir os valores
print(pessoa.keys())#Exibir as chaves
print(pessoa.items())

print (f"{pessoa['nome']} tem {pessoa['idade']} anos e pertence ao sexo {pessoa['sexo']}")

for chave in pessoa.keys():
    print(chave)

for valor in pessoa.values():
    print(valor)

for chave, valor in pessoa.items():
    print(f'Chave » {chave} │ Valor » {valor}')