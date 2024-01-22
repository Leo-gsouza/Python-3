def fatorial(num, mostrar = False):
    fatorial = 1
    for c in range(1,num+1):
        fatorial *= c
        if mostrar == True and c < num:
            print(f'{c} x ',end='')
        if mostrar == True and c == num:
            print(f'{c} = ',end='') 
    return fatorial

def bhaskara(a, b, c, ver_delta = False):
    delta = (b**2) - 4*a*c
    if ver_delta == True:
        print(f'O valor de delta = {delta}')
    if delta > 0:
        x1 = (- b + delta**0.5 )/(2*a)
        x2 = (- b - delta**0.5 )/(2*a)
        info = 'Duas raizes'
        return x1, x2, info
    elif delta == 0:
        x = (-b + delta) /(2*a)
        info = 'Uma raiz'
        return x, info
    else:
        info = 'Sem raiz'
        return info, delta
    
def somar_lista(lista):
    soma = 0
    for c in lista:
        soma+= c
    return soma

def raiz(numero):
    raiz_n = numero **0.5
    return raiz_n


def juros(valor, percentual, show = False):
    if show == True:
        return cifrao(valor + valor*percentual/100)
    else:
        return valor + valor*percentual/100
    
def desconto(valor, percentual, show = False):
    if show == True:
        return cifrao(valor - valor*percentual/100)
    else:
        return valor - valor*percentual/100

