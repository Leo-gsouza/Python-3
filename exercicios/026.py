frase = str(input("digite uma frase: ")).strip()

print(frase.lower().count("a"))#Quantidade de letra a na frase
print(frase.lower().find("a")+1)#Posição da primeira letra a
print(frase.lower().rfind("a")+1)#posição da ultima letra a 