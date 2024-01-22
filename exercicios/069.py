mais_18 = homens = mulheres_menos_20 = 0

while True:
    idade = int(input("\nInforme a idade » "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Informe o sexo » ")).strip().upper()[0]

    if idade >= 18:
        mais_18 += 1
    
    if sexo == "M":
        homens += 1

    if idade < 20 and sexo == "F":
         mulheres_menos_20 += 1

    opcao = input("Deseja continuar » ").strip().upper()[0]
    if opcao == "N":
        break

    

print(f"\nTotal de pessoas maiores de idade » {mais_18}\
      \nTotal de homens » {homens}\
       \nTotal de mulheres com menos de 20 anos » {mulheres_menos_20} ")

