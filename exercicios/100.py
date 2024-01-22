from random import randint
from time import sleep
numeros = []
somar = 0

def sorteia(lista):
   for cont in range(0,5):
      numero = randint(1,100)
      lista.append(numero)
      print(f'{numero}, ',end="")
      sleep(0.5)
   print('Fim')
   

def somapar(lista):
   somar = 0
   print('Soma dos números pares ')
   for num in lista:
      if num % 2 == 0:
         print(f'{num} + ',end="")
         somar += num
   print(f' = {somar} ')
         
    

sorteia(numeros)
somapar(numeros)


