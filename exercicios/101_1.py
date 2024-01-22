def voto(ano_nascimento):
    from datetime import date
    idade = date.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: Não Vota'
    elif 16 <= idade < 18 or idade >= 65:
        return f'Com {idade} anos: Voto opcional'
    else:
        return f'Com {idade} anos: Voto obrigatorio'

ano_nascimento = int(input('Ano de nascimento » '))
ano_nascimento1 = int(input('Ano de nascimento » '))
ano_nascimento2 = int(input('Ano de nascimento » '))

print(voto(ano_nascimento))
print(voto(ano_nascimento1))
print(voto(ano_nascimento2))

