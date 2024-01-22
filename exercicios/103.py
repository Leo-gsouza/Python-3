
def ficha(jogador="desconhecido", gols=0):
    return f'O {jogador} fez {gols} gol(s)'


n = str(input('nome do jogador: '))
g = str(input('numero de gols: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == "":
    print(ficha(gols=g))
else:
    print(ficha(n, g))


