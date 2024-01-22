cidade = str(input("nome da cidade: ")).strip()

if cidade[:5].title() == "Santo":
    print("Sim! começa com santo")
else:
    print("Não começa com Santo")