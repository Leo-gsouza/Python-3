from menu import *
from validacao import *
from arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'
if not existe(arq):
    criar(arq)

while True:
    titulo('MENU PRINCIPAL', '▬', 25)
    menu(['Ver pessoas cadastradas', "Cadastrar nova pessoa", "Sair do sitema"])
    linha('▬',39)

    opcao = leiaint('Sua opção: ')

    if opcao == 1:
        ler(arq)

    elif opcao == 2:
        titulo('NOVO CADASTRO','-', 20)
        nome = str(input('Nome: ')).strip().title()
        idade = leiaint('Idade: ')
        cadastrar_pessoa(arq, nome, idade)

    elif opcao == 3:
        break  

    else:
        print('\n\033[1;31mOPÇÃO INVALIDA!\033[m\n')

print('\n\033[33mFINALIZANDO...')
sleep(1)
print('OBRIGADO! VOLTE SEMPRE!\033[m')