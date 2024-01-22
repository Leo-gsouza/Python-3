reta1 = int(input("Informe a 1ª reta: "))
reta2 = int(input("Informe a 2ª reta: "))
reta3 = int(input("Informe a 3ª reta: "))

if reta1 < reta2+reta3 and reta2< reta1+reta3 and reta3< reta2+reta1:
    print("\033[1;32mÉ possivel formar um triangulo\033[m")

else:
    print("\033[1;31mNão é possivel formar um triangulo\033[m")