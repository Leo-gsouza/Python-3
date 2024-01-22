numero = int(input("Digite um número: "))
opcao = input("Digite uma opção\n[1]Binário\n[2]octal\n[3]Hexadecimal\n►►")

if opcao == "1":
    print (bin(numero)[2:])
elif opcao == "2":
    print (oct(numero)[2:])
elif opcao == "3":
    print (hex(numero)[2:])
else:
    print ("Opção invalida")