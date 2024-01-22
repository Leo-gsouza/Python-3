
valor = int(input("Valor de saque » R$"))
nota = 50
cedulas = 0

while True:
    if valor >= nota:
        valor -= nota
        cedulas += 1
    else:
        if cedulas > 0:
            print(f"Total de {cedulas} notas de R${nota}")
    
        if nota == 50:
            nota = 20
        elif nota == 20:
            nota = 10
        elif nota == 10:
            nota = 1

        cedulas = 0
        
        if valor == 0:
            break

print("Obrigado pela visita!")