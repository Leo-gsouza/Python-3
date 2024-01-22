valores = []
maior = menor = 0
inicio = 0
fim = 5

while True:
    for c in range(inicio,fim):
        valores.append(int(input(f"Insira o {inicio+1}º valor: ")))
        inicio += 1

        if c == 0:
            maior = valores[c]
            menor = valores[c]
        else:
            if valores[c] > maior:
                maior = valores[c]
            if valores[c] < menor:
                menor = valores[c]

    opcao = str(input("Deseja continuar? » ")).strip().upper()[0]
    if opcao == "N":
        break
    else:
        mais_valores = int(input("Quantos valores deseja inserir » "))
        fim += mais_valores



print(f'O maior valor da lista » {maior}\
      \nO menor valor da lista » {menor}')