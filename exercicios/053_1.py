texto = str(input("Digite um texto: ")).strip().upper()
texto = texto.split()#Criou uma lista com o texto
texto = "".join(texto)#Transformou a lista em um texto sem separação ""

inverso =""

for n in range(len(texto) -1, -1, -1):
    inverso += texto[n]
    
if texto == inverso:    
    print(f"O texto é palindromo\n{texto}\n{inverso} ")
else:
    print(f"O texto não é palindromo\n{texto}\n{inverso} ")
