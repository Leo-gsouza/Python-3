from menu import *

def cifrao(valor = 0, cifrao = 'R$'):
    return f'{cifrao}{valor:.2f}'.replace('.',',')

def validar_dinheiro(msg):
    while True:
        entrada = str(input(msg)).replace(',','.')
        if entrada.isalpha() or entrada.strip() == "":
            cores('roxo', 'Erro! Informe um preço valido')
        else:
            break
    return float(entrada)