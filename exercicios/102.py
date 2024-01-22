def fatorial(num, show=False):
    antecessor = num - 1
    fatorial = num

    while antecessor != 0:
        fatorial *= antecessor
        antecessor -= 1
     
    if show == True:
        for c in range(num,0,-1):
            if c != 1:
                print(f'{c} x ',end="")
            else:
                print(f'{c} = ',end="")         
        print(f'{fatorial}')
    
    else:
        print(f'{fatorial}')

fatorial(12)
fatorial(5, True)