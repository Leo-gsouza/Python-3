usuarios = []
pessoa = {}
for c in range(0,3):
    pessoa['nome'] = str(input('nome: ')).strip().title()
    pessoa['cpf'] = int(input('cpf: '))
    usuarios.append(pessoa.copy())

print(usuarios)



