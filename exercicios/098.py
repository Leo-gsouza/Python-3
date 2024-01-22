from time import sleep

def contador (inicio, fim, passo):
        if inicio < fim:
            while inicio <= fim:
                sleep(0.5)
                print(f'{inicio}',end=" ")
                inicio += passo
        elif inicio > fim:
            while inicio >= fim:
                sleep(0.5)
                print(f'{inicio}',end=" ")
                inicio -= passo

        print('Fim')

contador(1, 10, 1)
contador(10, 0, 2)

inicio = int(input('inicio » '))
fim = int(input('fim » '))
passo = int(input('passo » '))

contador(inicio, fim, passo)