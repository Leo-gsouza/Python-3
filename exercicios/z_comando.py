nome = 'Leonardo Garcia de Souza'

nome_separado_lista = nome.split()
print(nome_separado_lista)

primeiro_nome_op1 = nome_separado_lista[0]
ultimo_nome_op1 = nome_separado_lista[-1]
print(primeiro_nome_op1)
print(ultimo_nome_op1)

encontrar_espaco = nome.find(" ")
primeiro_nome_op2 = nome[:encontrar_espaco]
print(primeiro_nome_op2)
