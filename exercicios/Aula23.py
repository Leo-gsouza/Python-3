try:
    a = int(input('Numerado: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print("Problema no tipo de dado informado")

except (ZeroDivisionError):
    print("Não é possivel dividir por 0")
    
except (KeyboardInterrupt):
    print("Não foi inserido nenhum valor")

except Exception as erro:
    print(f'Infeliz ocorreu o erro » {erro}')
else:
    print(f'Resultado é {r}')
finally:
    print('Volte sempre')