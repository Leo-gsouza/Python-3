tupla = ('maça', 'uva','pera','abacaxi','banana','abacate')

for item in tupla:
    print(f'\n{item} vogais encontradas » ',end="")
    for letra in item:  
        if letra == "a":
            print('a',end=" ")
        if letra == "e":
            print('e',end=" ")
        if letra == "i":
            print('i',end=" ")
        if letra == "o":
            print('o',end=" ")
        if letra == "u":
            print('u',end=" ")
    
        
