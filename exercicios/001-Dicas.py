#MANIPULAR STRINGS

nome = 'Leon Scott Kennedy'

print(nome.count('e'))#Contar quantas letras 'e' tem na variavel
print(nome.upper())#transformar em maiusculo 
print(nome.lower())#transformar em minusculo 
print(nome.replace('e', 'i'))#trocar 'e' por 'i'
print(nome.capitalize())#1ª letra maiuscula do primeiro nome
print(nome.title())#1ª letra maiuscula após o espaço
print(len(nome))#quantas letras tem na variavel
print(nome.startswith('Leo'))#se inicia com uma determinada sequencia - true
print(nome.startswith('sco'))#se inicia com uma determinada sequencia - false
print(nome.endswith('edy'))#se inicia com uma determinada sequencia - true
print(nome.endswith('sco'))#se inicia com uma determinada sequencia - false
print(nome.isalnum())#se possui conteudo alfanumerico - letras e numeros
print(nome.isalpha())#se possui conteudo alfabetico - letras 
print(nome.islower())#se todas as letras são minusculas
print(nome.isupper())#se todas as letras são maiuscula
print(nome.swapcase())#Inverte maiusculo/minusculo
print(nome.split())#transforma em uma lista
print(nome.find('n'))#a primeira posição de 'n'
print(nome.rfind('n'))#a primeira posição de 'n'
print(nome.find('n'))#a primeira posição de 'n'
print(nome.ljust(30))#ajusta a string  e acrescenta espaços a direita
print(nome.rjust(30))#ajusta a string  e acrescenta espaços a esquerda
print(nome.center(30))#ajusta a string no centro
print(nome.rstrip(30))#remove espaços do lado direito
print(nome.lstrip(30))#remove espaços do lado esquerdo
print(nome.strip(30))#remove todos os espaços da string
#isalpha()é usado para verificar se uma string consiste apenas em caracteres alfabéticos.
#isnumeric()verifica se todos os caracteres de uma string são números.
#isalnum()verifica se uma string contém apenas letras ou números ou ambos.




