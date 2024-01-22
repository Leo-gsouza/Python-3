tabela = ('Tottenham','Arsenal','Manchester City','Liverpool','Aston Villa',\
          'Newcastle','Brighton','Manchester United','West Ham','Brentford',\
            'Chelsea','Wolves','Crystal Palace','Fulham','Nottingham Florest',\
                'Everton','Bounemouth','Luton Town','Burley','Sheffield United')

print ('\n▬▬▬▬▬ G6 ▬▬▬▬▬')
for pos, time in enumerate(tabela[:6]):
    print(f'{pos+1} » {time}')

print ('\n▬▬▬▬▬ Rebaixamento ▬▬▬▬▬')
for pos, time in enumerate(tabela[-2:]):
    print(f'{pos+19} » {time}')

print ('\n▬▬▬▬▬▬▬▬▬▬ Ordem alfabetica ▬▬▬▬▬▬▬▬▬▬')
print(sorted(tabela))

print ('\n▬▬▬▬▬ Rebaixamento ▬▬▬▬▬')
print(f'O chelsea está na {tabela.index("Chelsea")+1}ª colocação')