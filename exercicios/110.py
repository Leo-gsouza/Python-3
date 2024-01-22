from utilidadecev import moeda, dado

valor = dado.validar_dinheiro('Informe o preço: ')
juros = int(input("Juros » "))
desconto = int(input("Desconto » "))

moeda.resumo(valor,juros,desconto)
