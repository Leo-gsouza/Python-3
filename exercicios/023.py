from random import randint
#opcão 1
numero = randint(0000,9999)
num = str(numero)
print(f"unidade ► {num[3]}\nDezena ► {num[2]}\nCentena ► {num[1]}\nMilhar ► {num[0]}")

#opção 2
uni = numero // 1 % 10
dez = numero // 10 % 10
cent = numero // 100 % 10
mil = numero // 1000 % 10
print(f"unidade ► {uni}\nDezena ► {dez}\nCentena ► {cent}\nMilhar ► {mil}")
