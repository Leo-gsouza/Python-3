from menu import *

def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('\n\033[1;31mDADO INVALIDO!\033[m\n')
        except (KeyboardInterrupt):
            print('\n\033[1;31mPROGRAMA INTERROMPIDO\033\n[m')
        else:
            return valor
        
def leiafloat(msg):
    while True:
        try:
            valor = float(input(msg))
        except (ValueError, TypeError):
            print('Erro! Informe um número valido')
        except (KeyboardInterrupt):
            print('Entrada de dados foi interrompida pelo usuario')
        else:
            return valor
        
def leiaalpha(msg):
    while True:
        try:
            texto = str(input(msg))
        except (ValueError, TypeError):
            print('Erro! Informe apenas letras. ')
        except (KeyboardInterrupt):
            print('Entrada de dados foi interrompida pelo usuario')
        else:
             if texto.isalpha():
                return texto
             else:
                print('Erro! Digite apenas letras')
                continue
             

