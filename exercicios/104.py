
def leiaint(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            num = int(num)
            break
        else:
            print('\033[0;31mErro! Digite um número valido\033[m')
    return num

num = leiaint('Digite um número: ')
print(f'Número digitado foi {num}')