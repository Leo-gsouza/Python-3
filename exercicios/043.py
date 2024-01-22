peso = float(input("Informe o seu peso: "))
altura = float(input('Informe a sua altura: '))
imc = peso / (altura*altura)
print(f"▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\
      \nIMC ►► {imc:.2f}")

if imc <= 18.5:
    print("Abaixo do peso")
elif imc <= 25:
    print("Peso ideal")
elif imc <= 30:
    print("Sobrepeso")
elif imc <= 40:
    print("obesidade")
else:
    print("Obesidade morbida")