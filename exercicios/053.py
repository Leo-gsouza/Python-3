texto = str(input("Digite um texto: ")).strip().upper()
texto = texto.replace(" ", "")

if texto == texto[::-1]:
    print(f"O texto é palindromo\n{texto}\n{texto[::-1]} ")
else:
    print(f"O texto não é palindromo\n{texto}\n{texto[::-1]} ")
