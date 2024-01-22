distancia = float(input("Distancia da viagem: "))
ATE_200KM = 0.50
ACIMA_200KM = 0.45

if distancia > 200:
    print(f"Valor da passagem R${distancia*ACIMA_200KM:.2f}")
else:
    print(f"Valor da passagem R${distancia*ATE_200KM:.2f}")