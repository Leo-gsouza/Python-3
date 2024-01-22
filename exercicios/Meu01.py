from textos import *

texto = str(input('Copie e Cole o texto que desejar: '))
palavra = str(input('Digite a palavra que deseja consultar: '))
letra = str(input('Digite a letra que deseja consultar: '))

quantidade_palavra = pesquisar_palavra(texto, palavra)
print(f'A palavra {palavra} foi encontrada {quantidade_palavra} vezes no texto')

quantidade_letra = pesquisar_letra(texto, letra)
print(f'A palavra {letra} foi encontrada {quantidade_letra} vezes no texto')
