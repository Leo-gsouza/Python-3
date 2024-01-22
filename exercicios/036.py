cores =  {"verde":"\033[1;32m","vermelho":"\033[1;31m","limpa":"\033[m"}

valor_casa = float(input("Valor da casa: R$"))
salario = float(input('Salario: R$'))
num_parcelas = int(input("Numero de parcelas: "))

if salario*0.3 < valor_casa/num_parcelas:
    print(f"O emprestimo foi {cores['vermelho']}negado{cores['limpa']}\
          \nValor da parcela ►► R${valor_casa/num_parcelas}\
          \n30% do salario   ►► R${salario*0.3}")
else:
    print(f"O emprestimo foi {cores['verde']}aprovado{cores['limpa']}\
          \nValor da parcela ►► R${valor_casa/num_parcelas}\
          \n30% do salario   ►► R${salario*0.3}")