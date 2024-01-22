sexo = str(input("Sexo: ")).strip().upper()[0]

while sexo not in "FM":
    print("Dado invalido")
    sexo = str(input("Sexo: ")).strip().upper()[0]  

print(f"Deu certo! sexo = {sexo}")