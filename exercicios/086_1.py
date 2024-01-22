matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for coluna in range(0,3):
    print("▬"*40)
    for linha in range(0,3):
        matriz[coluna][linha] = int(input(f'Digite o valor da coluna {coluna} linha {linha}: '))

print("▬"*40)

for coluna in range(0,3):
    for linha in range(0,3):
        print(f'[{matriz[coluna][linha]}]',end=" ")
    print("")