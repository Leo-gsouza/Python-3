listagem = (str(input("Nome do produto: ")), float(input("Valor do produto: R$")),
            str(input("Nome do produto: ")), float(input("Valor do produto: R$")),
            str(input("Nome do produto: ")), float(input("Valor do produto: R$")))

print("▬"*40)
print(f'{"Listagem de Preços":^40}')
print("▬"*40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}',end="")
    else:
        print(f'R${listagem[pos]:>7.2f}')
    
