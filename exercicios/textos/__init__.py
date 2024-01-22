def pesquisar_letra(texto, letra):
    qtdd_letras = 0

    for l in texto:
        if l == 'ã':
            l = 'a'
        if strip_title(l) == strip_title(letra):
            qtdd_letras += 1
    return qtdd_letras

def pesquisar_palavra(texto, palavra):
    quantidade = 0
    for p in texto.split():
        if strip_title(p) == strip_title(palavra):
            quantidade += 1
    return quantidade

def strip_title(palavra):
    palavra = palavra.strip().title()
    return palavra

def primeiro_nome(nome):
    primeiro = nome.find(' ')
    nome = nome[:primeiro]
    return nome

def ultimo_nome(nome):
    ultimo = nome.rfind(' ')+1
    nome = nome[ultimo:]
    return nome