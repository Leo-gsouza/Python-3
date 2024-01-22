nota_50 = nota_20 = nota_10 = nota_1 = 0

valor = int(input("Valor de saque » R$"))

while True:
    if valor >= 50:
        nota_50 += 1
        valor -= 50
    elif    valor >= 20:
        nota_20 += 1
        valor -= 20
    elif    valor >= 10:
        nota_10 += 1
        valor -= 10
    elif    valor >= 1:
        nota_1 += 1
        valor -= 1
    else:
        break

print(f"\nTotal de notas de R$50 » {nota_50} \
      \nTotal de notas de R$20 » {nota_20}\
      \nTotal de notas de R$10 » {nota_10}\
      \nTotal de notas de R$1 » {nota_1}")