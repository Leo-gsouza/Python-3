valor_total = cont = 0
mais_de_1000 = ""

while True:
    nome_produto = str(input("\nNome do produto » ")).strip().capitalize()
    valor_produto = float(input("Preço do produto » R$"))
    cont += 1
    valor_total += valor_produto

    if valor_produto > 1000:
        mais_de_1000 += f"{nome_produto} » R${valor_produto:.2f}\n"

    if cont == 1:
        mais_barato = valor_produto
        nome_mais_barato = nome_produto
    elif valor_produto < mais_barato:
        mais_barato = valor_produto
        nome_mais_barato = nome_produto

    opcao = ' '   
    while opcao not in "SN":
        opcao = str(input("Deseja continuar? » ")).strip().upper()[0]
    if opcao == "N":
        break   

print(f"\nGasto total R${valor_total:.2f}\
      \n\nProdutos que custam mais de R$1000:\n{mais_de_1000}\
      \nProduto mais barato » {nome_mais_barato} R${mais_barato:.2f}")