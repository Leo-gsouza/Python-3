retas = []

for i in range(1,4):
    reta = int(input(f"Valor da {i}ª reta ►► "))
    retas.append(reta)

if retas[0] < retas[1]+ retas[2] and retas[1] < retas[0]+retas[2] and retas[2] < retas[0]+retas[1]:
    print("▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬\
          \nÉ possivel formar um triangulo\
          \n▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬▬")

    if retas[0] == retas[1] == retas[2]:
        print("Triangulo Equilatero")
    #Poderia ter usado o else
    elif retas[0] == retas[1] != retas[2]\
    or retas[0] == retas[2]  != retas[1]\
    or retas[2] == retas[1] != retas[0]:
        print("Triangulo Isosceles")
    
    elif retas[0] != retas[1] != retas[2] != retas[0]:
        print("Triangulo Escaleno")

else:
    print("Não é possivel formar um triangulo")