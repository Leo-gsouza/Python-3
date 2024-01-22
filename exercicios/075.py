tupla = (int(input("Primeiro valor » ")),
         int(input("Segundo valor » ")),
         int(input("Terceiro valor » ")),
         int(input("Quarto valor » ")))

print(f'\nO valor 9 apareceu {tupla.count(9)} vezes')


if 3 in tupla:
    print((f'\nO primeiro valor 3 foi digitado na posição {tupla.index(3)}'))
else:
    print('\nNão tem o valor 3 na tupla')

print('\nNumeros pares são: ',end=" ")
for numero in tupla:
    if numero % 2 == 0:
        print(numero,end=" » ")
print('Fim')