usuarios = []
temporario = {}

while True:
    cadastro = False
    nome = str(input('nome » ')).strip().title()
    cpf = str(input('cpf » ')).replace('.','').replace('-','').strip()

    if usuarios == []:
        temporario['nome'] = nome
        temporario['cpf'] = cpf
        usuarios.append(temporario.copy())
        temporario.clear()
    else:    
        for chave in usuarios:
            if cpf in chave['cpf']:
                print('existente')
                cadastro = True

        print(cadastro)
        if cadastro == False:
            temporario['nome'] = nome
            temporario['cpf'] = cpf
            usuarios.append(temporario.copy())
            temporario.clear()
            print('foi cadastrado')
    
    opcao = int(input("opção: "))
    if opcao == 1:
        break
    else:
        continue

print(usuarios)

