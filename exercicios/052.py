numero = int(input("Informe um numero: "))
divisivel = 0
numeros = ""

for n in range(1, numero+1):
    if numero % n == 0:
        divisivel += 1
        numeros += f"{n} ► "

if divisivel == 2:
    print(f"O numero {numero} é primo\
          \nDivisivel por {numeros}",end="")
else:
    print(f"O numero {numero} não é primo\
          \nDivisivel por {numeros}",end="") 

print("Acabou")   


