numero = int(input("Digite um número: "))
fatorial = numero
cont = 0

while cont != numero-1:
    cont += 1
    multiplicador = numero - cont
    print(f'{fatorial} x {multiplicador} = ',end='')
    fatorial *= multiplicador
    print(f'{fatorial}')
    
    
print(f"\nFatorail de {numero} = {fatorial}")