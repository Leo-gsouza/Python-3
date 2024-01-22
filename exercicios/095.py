lista_jogadores = []
dados_jogador = {}
gols_por_partida = []

while True:
   dados_jogador['nome'] = str(input('Nome do jogador: ')).strip().title()
   partidas = int(input(f'Quantas partidas {dados_jogador["nome"]} jogou: '))
   for c in range(0, partidas):
      gols_por_partida.append(int(input(f'Quantos gols na partida {c}ª partida: ')))

   dados_jogador['gols'] = gols_por_partida.copy()
   dados_jogador['total_gols'] = sum(gols_por_partida.copy())
   lista_jogadores.append(dados_jogador.copy())
   gols_por_partida.clear()

   while True:
      opcao = str(input('Deseja continuar? [S/N] » ')).strip().upper()[0]
      if opcao not in 'SN':
         print('Digite apenas sim ou não')
      else:
         break   
   if opcao == 'N':
      break

print(f'{"Nome":<9}{"Gols":^9}{"Total":>9}')
for dic in lista_jogadores:
   print(f'{dic["nome"]:<9}{dic["gols"]}{dic["total_gols"]:>9}')

while True:
   opcao = str(input('Deseja consultar os dados de algum jogador? [S/N] » ')).strip().upper()[0]
   if opcao == 'N':
      break
   selecionar = str(input('Mostrar dados de qual jogador: ')).strip().title()
   for dic in lista_jogadores:
      if dic['nome'] == selecionar:
         cont = 1
         for gol in dic['gols']:
            if gol == 0:
               print(f'No {cont}º jogo não fez nenhum gol')
            elif gol == 1:
               print(f'No {cont}º jogo fez {gol} gol')
            elif gol == 3:
               print(f'No {cont}º jogo fez um hatchtrick!')
            else:
               print(f'No {cont}º jogo fez {gol} gols')
            cont += 1
            print("=▬"*25)
      else:
         print(f'{"=▬"*25}\nErro de digitação ou jogador não cadastrado!\n{"=▬"*25}')

print('Finalizando........')







       




      