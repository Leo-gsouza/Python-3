from validacao import *
from dinheiro import *

def sacar(saldo, saque, extrato):
    saldo-= saque
    extrato += f'Saque:    {cifrao(saque)}\n'
    return saldo, extrato

def depositar(saldo, extrato):
    deposito = leiafloat('Valor de deposito » R$')
    saldo += deposito
    extrato += f'Deposito: {cifrao(deposito)}\n'
    return saldo, extrato

def cadastrar_cliente(cpf, nome, lista = []):
    nome = nome.strip().title()
    cpf = cpf.strip().replace('.','').replace('-','')
    temporario = {}
    cadastro = False

    for chave in lista:
        if cpf in chave['cpf']:
            cadastro = True
    if cadastro == False:    
        temporario['nome'] = nome
        temporario['cpf'] = cpf
        lista.append(temporario.copy())
    return lista
    


