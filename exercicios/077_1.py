tupla = ('maça', 'uva','pera','abacaxi','banana','abacate')

for item in tupla:
    print(f'\nNa palavra {item} temos » ',end="")
    for letra in item:  
        if letra in 'aeiou':
            print(f'{letra}',end=" ")
    
        
