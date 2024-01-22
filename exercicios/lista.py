valores = list(range(10,-1,-1))
valores.append(15)#Adicionou 15 na lista (ultima posição)
valores.insert(2,13)#Adicionou o valor 13 na posição 2
del valores[3]#remover o elemento que está na posição 3
valores.pop(1)#remover o elemento que está na posição 1
valores.pop()#remover o ultimo elemento
valores.remove(6)#remover o valor 6 
valores.sort()#colocar em ordem
valores.sort(reverse=True)#colocar a ordem contraria

for c in range(0,2):
    valores.append(int(input("Digite um valor: ")))

for c in range(0,3):
    valor = int(input("\nDigite um valor:"))
    if valor not in valores:
        valores.append(valor)

valores_b = valores[:]#criar uma copia
valores_b.sort()#copia em ordem

print(f'{valores}\n{valores_b}')

