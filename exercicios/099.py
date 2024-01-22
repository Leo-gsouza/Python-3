
def maior(*num):
    contador = 0
    print('\nAnalisando os valores passados')
    for n in num:
        print(f'{n} » ',end="")
        if contador == len(num)-1:
             print('Fim')
        if contador == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        contador += 1
    
    print(f'Foram informados {len(num)} valores\nO maior valor foi {maior}')
   
maior(2,5,9,7,5)
maior(2,10,52)
maior(2,10,52,104,65,47,17,241,956,562,1)