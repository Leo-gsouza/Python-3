from random import randint
from time import sleep

dados_jogador = {}
gols_por_partida = []

dados_jogador['nome'] = str(input('Nome do jogador: ')).title()
dados_jogador['partida'] = randint(1,38)
for c in range(0, dados_jogador['partida']):
   gols_por_partida.append(randint(0,3))
   
dados_jogador['gols'] = gols_por_partida

gols = 0
for n in gols_por_partida:
   gols += n

dados_jogador['total_gols'] = gols

print(dados_jogador)
print('-'*40)

for chave, valor in dados_jogador.items():
   print(f'{chave} » {valor}')
print('-'*40)

for posicao, valor in enumerate(gols_por_partida):
   sleep(3)
   if valor == 0:
     print(f'» Na partida {posicao+1}, não fez nenhum gol')
   elif valor == 1:
    print(f'» Na partida {posicao+1}, fez {valor} gol')
   else:
     print(f'» Na partida {posicao+1}, fez {valor} gols') 
      
       




      