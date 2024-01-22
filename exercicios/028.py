from random import randint

numero_usuario = int(input("Digite um numero de 0 a 5 \n►► "))
numero_computador = randint(0,5)

if numero_usuario == numero_computador:
    print("Parabens! Você acertou")
else:
    print(f"Você errou! o computador escolheu o numero ► {numero_computador}")
