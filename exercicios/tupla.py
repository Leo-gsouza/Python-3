frutas = ("uva", "maça", "pera", "melancia", "abacaxi")

for item in frutas:
    print(f"{item} » ",end="")
print("")

for cont in range(0, len(frutas)):
    print(f"{cont}: {frutas[cont]}")

for item in enumerate(frutas):
    print(f"{item}")

for pos, item in enumerate(frutas):
    print(f"{pos}: {item}")

print(sorted(frutas))#colocar em ordem