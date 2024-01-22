lista_1 = []
lista_1.append('Leo')
lista_1.append(34)
print(lista_1)

lista_2 = []
lista_2.append(lista_1[:])#[:] cria uma copia da lista dentro de outra lista
print(lista_2)

lista_1[0] = "Naty" #substituiu Leo
lista_1[1] = 29 #Substituiu 34
lista_2.append(lista_1[:])#Adicionou uma copia de Naty, 29 na segunda lista mantendo Leo, 34
print(lista_1)
print(lista_2)

###############################################################################################

lista_3 = []
dados = []
for c in range(0,3):
    dados.append(str(input("Nome: ")))
    dados.append(int(input("Idade: ")))
    lista_3.append(dados[:])
    dados.clear()

print(lista_3)

print('\nMaiores de idade:')
for p in lista_3:
    if p[1] >= 18:
        print(f'{p[0]} tem {p[1]} anos')
