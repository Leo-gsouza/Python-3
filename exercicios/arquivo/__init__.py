from menu import *
from matematica import *

def existe(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    
def criar(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um erro na criação do arquivo')
    else:
        print(f'Arquivo {nome} criado com sucesso')

def ler(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo')
    else:
        titulo('PESSOAS CADASTRADAS','▬',20)
        print (a.read())
       
    finally:
        a.close()

def cadastrar_pessoa(arq, nome= 'desconhecido', idade= 0):
    try:
        a = open(arq, 'at') 
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            a.write(f'{nome:<24}{idade:>3} anos\n')
        except:
            print('Houve um ERRO na hora de escrever os dados ')
        else:
            print(f'Novo registro de {nome} adicionado')
            a.close()
            
def cadastrar_produto(arq, categoria, modelo, tamanho ,cor="sem cor", custo=0, venda=0):
    try:
        a = open(arq, 'at') 
    except:
        print('Houve um ERRO na abertura do arquivo')
    else:
        try:
            lucro = venda - custo
            a.write(f'{categoria:<14}{modelo:<17}{tamanho:<10}{cor:<12}{cifrao(custo):<10}{cifrao(venda):<10}{cifrao(lucro):<10}')
        except:
            print('Houve um ERRO na hora de escrever os dados ')
        else:
            print(f'\n\033[1;31m{categoria}-{modelo} foi adicionado com sucesso\033[m\n')
            a.close()


