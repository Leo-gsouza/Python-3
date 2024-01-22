def titulo(titulo, linha, qtdd):
    titulo = titulo.upper()
    tamanho = len(titulo)+qtdd
    print(linha*tamanho)
    print(titulo.center(tamanho))
    print(linha*tamanho)

def tabulacao(a, b, c="",d="", e="", f="" ):
    print(f'{a:<12}{b:<12}{c:<12}{d:<12}{e:<12}{f:<12}')

def menu(lista):
    contador = 1
    for item in lista:
        print(f'{contador} - {item}')
        contador += 1

def linha(linha, qtdd):
    print(linha*qtdd)

def cores(cor, texto):
    if cor.lower() == 'vermelho':
        print(f'\033[1;31m{texto}\033[m')
    if cor.lower() == 'verde':
        print(f'\033[1;32m{texto}\033[m')
    if cor.lower() == 'amarelo':
        print(f'\033[1;33m{texto}\033[m')
    if cor.lower() == 'azul':
        print(f'\033[1;34m{texto}\033[m')
    if cor.lower() == 'roxo':
        print(f'\033[1;35m{texto}\033[m')
    if cor.lower() == 'ciano':
        print(f'\033[1;36m{texto}\033[m')
    if cor.lower() == 'branco':
        print(f'\033[1;37m{texto}\033[m')

