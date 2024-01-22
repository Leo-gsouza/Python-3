from time import sleep

razao = int(input("razão » "))
primeiro = int(input("primeiro termo » "))
num_termos = int(input("número de termos » "))
cont = 0
print("▬"*(num_termos*5))

while cont < num_termos:
    cont += 1
    primeiro += razao
    sleep(0.4)
    print(f"{primeiro} ► ",end="")

sleep(1.2)
print("acabou")
print("▬"*(num_termos*5))