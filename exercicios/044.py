valor_produto = float(input("Valor do produto: R$"))
forma_de_pagamento = int(input("Forma de pagamento\
                           \n[1]Dinheiro\n[2]Cartão de crédito\n►► "))

if forma_de_pagamento == 1:
    print(f"A vista tem 10% de desconto\
          \nValor do produto: R${valor_produto*0.9:.2f}")
else:
    opcao = int(input("[1]A vista\n[2]Parcelado\n►► "))
    if opcao == 1:
        print(f"Crédito a vista tem 5% e desconto\
          \nValor do produto: R${valor_produto*0.95:.2f}")
    else:
        parcelas = int(input("Número de parcelas ►►  "))

        if parcelas == 2:
            print(f"Em 2x não tem juros\
          \nValor do produto: R${valor_produto:.2f}\
          \n{parcelas}x de R${valor_produto/parcelas:.2f}")
            
        elif 2 < parcelas <=5:
            print(f"Entre 3 e 5 parcelas o juros é de 7%\
          \nValor do produto: R${valor_produto * 1.07:.2f}\
          \n{parcelas}x de R${(valor_produto*1.07)/parcelas:.2f}")
            
        elif 5 < parcelas <=8:
            print(f"Entre 6 e 8 parcelas o juros é de 12%\
          \nValor do produto: R${valor_produto * 1.12:.2f}\
          \n{parcelas}x de R${(valor_produto*1.12)/parcelas:.2f}")
            
        elif parcelas <=12:
            print(f"Entre 9 e 12 parcelas o juros é de 20%\
          \nValor do produto: R${valor_produto * 1.20:.2f}\
          \n{parcelas}x de R${(valor_produto*1.20)/parcelas:.2f}")
            
        else:
            print("Numero de parcelas invalido!")