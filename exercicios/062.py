from time import sleep

razao = int(input("razão » "))
primeiro = int(input("primeiro termo » "))
cont = 0

while cont <= 10:
    cont += 1
    primeiro += razao
    sleep(0.4)
    print(f"{primeiro} ► ",end="")

while True:    
    opcao = int(input("\nQuantos termos você quer mostrar a mais?\n»» "))
    if opcao == 0:
        break
    else: 
        termos = opcao
        while termos != 0:
            termos -= 1
            primeiro += razao
            sleep(0.4)
            print(f"{primeiro} ► ",end="")
    print("Pausa")



sleep(1.2)
print("acabou")
