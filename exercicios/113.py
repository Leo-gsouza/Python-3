def leiaint(msg):
    while True:
        try:
            valor = int(input(msg))
        except (ValueError, TypeError):
            print('Erro! Informe um número inteiro valido')
        except (KeyboardInterrupt):
            print('Entrada de dados foi interrompida pelo usuario')
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


 
        
       




#programa principal

#print(f'numero inteiro » {leiaint("Digite um número inteiro » ")}')
#print(f'numero real » {leiafloat("Digite um número real » ")}')

print(leiaalpha('Digite um texto: '))