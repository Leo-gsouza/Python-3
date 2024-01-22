velocidade = float(input("Velocidade do carro: "))
ACIMA_VELOCIDADE = 80
VALOR_MULTA = 7

if velocidade > ACIMA_VELOCIDADE:
    print(f"Foi multado!!!\nVeiculo atingiu ►► {velocidade}km/h\
          \nValor da multa: R${(velocidade - ACIMA_VELOCIDADE) * VALOR_MULTA:.2f}")