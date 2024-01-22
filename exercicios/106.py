cores = {'vermelho':'\033[1;30;41m','verde':'\033[1;30;42m','azul':'\033[1;30;44m','roxo':'\033[1;30;45m', 'ciano':'\033[1;30;46m', 'cinza':'\033[1;30;47', 'limpa':'\033[m' }


def ajuda(com, cor=0, limpa=cores['limpa']):
    print(cor)
    help(com)
    print(limpa)

def titulo(msg, cor=0, limpa=cores['limpa']):
    print(cor)
    tam = len(msg) + 4
    print('▬'* tam)
    print(f"  {msg}  ")
    print('▬'* tam)
    print(limpa)

#programa principal
while True:
    titulo('Sistema de Ajuda PyHelp', cores['roxo'])
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando, cores['ciano'])
print('Até logo')
