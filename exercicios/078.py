valores = []

for c in range(1,6):
    valores.append(int(input(f"Insira o {c}º valor: ")))

print(f'O maior valor da lista » {max(valores)}\
      \nO menor valor da lista » {min(valores)}')