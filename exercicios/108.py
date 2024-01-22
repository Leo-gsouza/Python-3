import moeda

valor = float(input('Valor do produto: '))

print(f'A metade de {moeda.cifrao(valor)} é {moeda.cifrao(moeda.metade(valor))}')
