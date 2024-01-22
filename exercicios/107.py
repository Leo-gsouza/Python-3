import moeda

valor = float(input('Valor do produto: R$'))

print(moeda.aumentar(valor, 20))
print(moeda.diminuir(valor, 12))
print(moeda.metade(valor))
print(moeda.dobro(valor))