def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade >= 18:
        return True
    else:
        return False
        
ano_nascimento = int(input('Ano de nascimento » '))


if voto(ano_nascimento):
    print(f'Apto para votar!')
else:
    print(f'Inapto para votar!')
