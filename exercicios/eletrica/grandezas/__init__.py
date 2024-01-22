def Potencia(volt=0, ampere=0, ohm=0):
    if volt > 0 and ampere > 0:
        return f'{volt*ampere:.1f} watts'
    elif volt > 0 and ohm > 0:
        return f'{volt**2 / ohm:.1f} watts'
    elif ampere > 0 and ohm > 0:
        return f'{ampere**2 * ohm:.1f} watts'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Tensão = {volt:<7}{"│":>3}\n│ Corrente = {ampere:<5}{"│":>3}\n│ Resistencia = {ohm:<4}{"│":>1}\n{"▀"*21}\n'

def Tensao(watt=0, ampere=0, ohm=0):
    if watt > 0 and ampere > 0:
        return f'{watt/ampere:.1f} volts'
    elif watt > 0 and ohm > 0:
        return f'{watt**0.5 * ohm**0.5:.1f} volts'
    elif ampere > 0 and ohm > 0:
        return f'{ampere * ohm:.1f} volts'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Potencia = {watt:<6}{"│":>2}\n│ Corrente = {ampere:<5}{"│":>3}\n│ Resistencia = {ohm:<4}{"│":>1}\n{"▀"*21}\n'
    
def Corrente(watt=0, volt=0, ohm=0):
    if watt > 0 and volt > 0:
        return f'{watt/volt:.1f} amperes'
    elif watt > 0 and ohm > 0:
         return f'{watt**0.5 / ohm**0.5:.1f} amperes'
    elif volt > 0 and ohm > 0:
            return f'{volt / ohm:.1f} amperes'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Potencia = {watt:<6}{"│":>2}\n│ Tensão = {volt:<6}{"│":>4}\n│ Resistencia = {ohm:<4}{"│":>1}\n{"▀"*21}\n'
    
def Resistencia(watt=0, volt=0, ampere=0):
    if watt > 0 and volt > 0:
        return f'{volt**2 / watt:.1f} ohm'
    elif watt > 0 and ampere > 0:
         return f'{watt/ ampere**2:.1f} ohm'
    elif volt > 0 and ampere > 0:
            return f'{volt / ampere:.1f} ohm'
    else:
        return f'\n\033[1;31mErro! Você digitou apenas uma grandeza\033[m\
            \n{"▄"*21}\n│ Potencia = {watt:<6}{"│":>2}\n│ Tensão = {volt:<6}{"│":>4}\n│ Corrente = {ampere:<5}{"│":>3}\n{"▀"*21}\n'


def tratamento():
     linha(20)
     opcao = int(input('Deseja saber o valor de qual grandeza?\
                       \n[1]Tensão \t[2]Potencia\n[3]Corrente \t[4]Resistencia\n» '))
     if opcao == 1:
          print('\nPara encontrar o valor da TENSÃO precisa ter\
                \n em mãos os valores de 2 grandezas\
                \n[1]Potencia e Corrente\
                \n[2]Potencia e Resistencia\
                \n[3]Corrente e Resistencia')
          
          grandezas = int(input('Informe a opção que contenha as\
                                \n grandezas que você conhece os valores\n» '))
          if grandezas == 1:     
            potencia = int(input('\nInforme o valor da potencia » '))
            corrente = int(input('Informe o valor da corrente » '))
            print(Tensao(potencia, corrente))

          elif grandezas == 2:     
            potencia = int(input('\nInforme o valor da potencia » '))
            resistencia = int(input('Informe o valor da resistencia » '))
            print(Tensao(potencia, 0, resistencia))

          elif grandezas == 3:     
            corrente = int(input('\nInforme o valor da corrente » '))
            resistencia = int(input('Informe o valor da resistencia » '))
            print(Tensao(0, corrente, resistencia))

     elif opcao == 2:
          print('\nPara encontrar o valor da POTENCIA precisa ter\
                \n em mãos os valores de 2 grandezas\
                \n[1]Tensão e Corrente\
                \n[2]Tensão e Resistencia\
                \n[3]Corrente e Resistencia')
          grandezas = int(input('Informe a opção que contenha as\
                                \n grandezas que você conhece os valores\n» '))
          if grandezas == 1:     
            tensao = int(input('Informe o valor da tensão » '))
            corrente = int(input('Informe o valor da corrente » '))
            print(Potencia(tensao, corrente))

          elif grandezas == 2:     
            tensao = int(input('Informe o valor da potencia » '))
            resistencia = int(input('Informe o valor da resistencia » '))
            print(Potencia(tensao, 0, resistencia))

          elif grandezas == 3:     
            corrente = int(input('Informe o valor da corrente » '))
            resistencia = int(input('Informe o valor da resistencia » '))
            print(Potencia(0, corrente, resistencia))

     elif opcao == 3:
          print('\nPara encontrar o valor da CORRENTE precisa ter\
                \n em mãos os valores de 2 grandezas\
                \n[1]Tensão e Potencia\
                \n[2]Tensão e Resistencia\
                \n[3]Potencia e Resistencia')
          grandezas = int(input('Informe a opção que contenha as\
                                \n grandezas que você conhece os valores\n» '))
          if grandezas == 1:     
            tensao = int(input('Informe o valor da tensão » '))
            potencia = int(input('Informe o valor da potencia » '))
            print(Corrente(potencia, tensao))

          elif grandezas == 2:     
            tensao = int(input('Informe o valor da tensao » '))
            resistencia = int(input('Informe o valor da resistencia » '))
            print(Corrente(0, tensao, resistencia))

          elif grandezas == 3:     
            potencia = int(input('Informe o valor da potencia » '))
            resistencia = int(input('Informe o valor da resistencia » '))
            print(Corrente(potencia, 0, resistencia))

     elif opcao == 4:
          print('\nPara encontrar o valor da RESISTENCIA precisa ter\
                \n em mãos os valores de 2 grandezas\
                \n[1]Tensão e Potencia\
                \n[2]Tensão e Corrente\
                \n[3]Potencia e Corrente')
          grandezas = int(input('Informe a opção que contenha as\
                                \n grandezas que você conhece os valores\n» '))
          if grandezas == 1:     
            tensao = int(input('Informe o valor da tensão » '))
            potencia = int(input('Informe o valor da potencia » '))
            print(Resistencia(potencia, tensao))

          elif grandezas == 2:     
            tensao = int(input('Informe o valor da tensao » '))
            corrente = int(input('Informe o valor da corrente » '))
            print(Resistencia(0, tensao, corrente))

          elif grandezas == 3:     
            potencia = int(input('Informe o valor da potencia » '))
            corrente = int(input('Informe o valor da resistencia » '))
            print(Resistencia(potencia, 0, corrente))

def linha(qtdd = 0, traco = "⚡" ):
    print(traco*qtdd)