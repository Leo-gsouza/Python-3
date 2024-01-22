numeros = []

for c in range(0,5):
    numero = int(input(f'Digite o {c+1}º valor » '))#ex 5  8  2  4  1 
    if c == 0:
        numeros.append(numero)# » (5)
    elif numero > numeros[-1]:
        numeros.append(numero)# 5 » (8)
    else:
        posicao = 0
        while posicao < len(numeros):
            if numero <= numeros[posicao]:
                numeros.insert(posicao,numero)# » {1} (2) [4] 5  8
                break
            posicao += 1

print(numeros)
            


