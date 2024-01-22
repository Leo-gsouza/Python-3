def fatorial(num, show=False):
    """Calcula o fatorial de um número.
    Args:
        num (Inteiro): O número a ser calculado
        show (bool, optional): Mostrar ou não a conta 
    Returns:
        Inteiro: Retorna o valor do fatorial de num
    """
    fatorial = 1
    for n in range(num, 0, -1):
        if show == True:
            if n > 1:
                print(f'{n} x ',end="")
            else:
                print(f'{n} = ',end="")
        fatorial *= n
    return fatorial

print(fatorial(5))
print(fatorial(5, True))
help(fatorial)