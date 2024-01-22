from random import randint
from time import sleep

dados_jogador = {}
gols_por_partida = []

dados_jogador['nome'] = str(input('Nome do jogador: ')).title()
partidas = randint(1,5)
for c in range(0, partidas):
   gols_por_partida.append(int(input(f'Quantos gols na partida {c}: ')))
   
dados_jogador['gols'] = gols_por_partida
dados_jogador['total_gols'] = sum(gols_por_partida)

print(dados_jogador)
print('-'*40)

for chave, valor in dados_jogador.items():
   print(f'{chave} » {valor}')
print('-'*40)

for posicao, valor in enumerate(gols_por_partida):
   sleep(1)
   if valor == 0:
     print(f'» Na partida {posicao+1}, não fez nenhum gol')
   elif valor == 1:
    print(f'» Na partida {posicao+1}, fez {valor} gol')
   else:
     print(f'» Na partida {posicao+1}, fez {valor} gols') 
      
       




      