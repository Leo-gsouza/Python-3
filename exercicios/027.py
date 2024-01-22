nome = str(input("Informe o nome completo: ")).strip()
#opção 1
primeiro_nome = nome.find(" ")
ultimo_nome = nome.rfind(" ")
print(f"Primeiro nome: {nome[:primeiro_nome]}")
print(f"Ultimo nome: {nome[ultimo_nome:]}")

#opção 2
nome_lista = nome.split()
print(f"Primeiro nome: {nome_lista[0]}")
print(f"Ultimo nome: {nome_lista[-1]}")