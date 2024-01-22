numero_extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete',\
                  'oito','nove','dez','onze','doze','treze','quatorze',\
                  'quinze','dezesseis','dezessete','dezoioto','dezenove','vinte')



while True:
    numero = int(input('Digite um valor de 0 a 20: '))
    while True:
        if 0 <= numero <=20:
            break
        else:
            print("Valor invalido!")
            numero = int(input('\nDigite um valor de 0 a 20: '))

    print (numero_extenso[numero])
    opcao = str(input("\nDeseja continuar? » ")).strip().upper()[0]

    if opcao == "N":
        break
    
        
print('\nFinalizando programa......')