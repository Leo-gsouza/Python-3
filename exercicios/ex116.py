from validacao import *
from banco import *
from menu import *
from time import sleep


#programa principal
saldo = 2000
extrato = ''
LIMITE_SAQUE = 0

while True:
    titulo('Sistema Bancario', "=", 30)
    menu(['Saque','Deposito','Extrato','Cadastrar cliente','Ver clientes', 'Sair'])
    linha('-',46)

    opcao = leiaint('\nSua opção » ')
    print(' ')
    
    if opcao == 1:
        saque = leiafloat('Valor de saque » R$')
        if saque > 500:
            print('É permitido o saque de até R$500')
        elif LIMITE_SAQUE == 3:
            print('O limite de saques por dia já foi excedido')
        else:
            saldo, extrato = sacar(saldo, saque, extrato)
            LIMITE_SAQUE += 1

    elif opcao == 2:
        saldo, extrato = depositar(saldo, extrato)
    
    elif opcao == 3:
        titulo('Extrato','▬',25)
        print(extrato)
        print(f'\nSaldo » {cifrao(saldo)}')
        linha("▬",32)
        sleep(5)

    elif opcao == 4:
        lista = []
        cadastro = False
        nome = str(input('Informe o seu nome: '))
        cpf = str(input('Informe o seu CPF: ' ))
        lista = cadastrar_cliente(cpf, nome)

    elif opcao == 5:
        titulo('clientes do banco','-',30)
        for dic in lista:
            print(f'CLIENTE » {dic["nome"]:<12}CPF: {dic["cpf"]}  ')
            sleep(3)
    
    else:
        break

print('Muito obrigado! Volte sempre')