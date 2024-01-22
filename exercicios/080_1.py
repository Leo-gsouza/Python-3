cesto = []

for c in range(0,5):
    fruta = str(input(f'Qual a {c+1}ª fruta inserida no cesto » '))

    if c == 0:
        cesto.append(fruta)

    elif fruta > cesto[-1]:
        cesto.append(fruta)
        
    else:
        posicao = 0
        while posicao < len(cesto):
            if fruta <= cesto[posicao]:
                cesto.insert(posicao,fruta)
                break
            posicao += 1

print(cesto)
            


