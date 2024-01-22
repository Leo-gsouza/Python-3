
while True:
    multiplicador = int(input("\nMultiplicador » "))
    if multiplicador < 0:
        break

    for multiplicando in range(1,11):
        print(f"{multiplicador:2} x {multiplicando:2} = {multiplicador*multiplicando:3}")

print("\nFinalizado")