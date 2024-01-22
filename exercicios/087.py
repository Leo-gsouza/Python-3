matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_coluna3 = maior_valor2 = 0
num_pares = ""


for linha in range(0,3):
    for coluna in range(0,3):
        valor = int(input(f'Digite o valor da │L:{linha}│C:{coluna}│ »  '))
        matriz[linha][coluna] = valor
        if coluna == 2:
            soma_coluna3 += valor

        if valor % 2 == 0:
            soma_pares += valor
            num_pares += (f'{valor} » ')

        if linha == 1:
            if coluna == 0:
                maior_valor2 = valor
            else:
                if valor > maior_valor2:
                    maior_valor2 = valor

print(f'\nOs numeros pares são: {num_pares}│Soma total » {soma_pares} ')
print(f'A soma da terceira coluna » {soma_coluna3}')     
print(f'Maior valor da segunda linha » {maior_valor2}')
      

       