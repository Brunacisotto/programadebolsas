# Etapa 2 lista de nomes de animais
animais = [
    "Cachorro", "Gato", "Pato", "Leão", "Peixe",
    "Girafa", "Vaca", "Urso", "Cavalo", "Baleia",
    "Hiena", "Macaco", "Lobo", "Pinguim", "Peixe",
    "Tucano", "Abelha", "Cobra", "Formiga", "Golfinho"
]


animais.sort() # Ordenar a lista em ordem crescente


for animal in animais: # iterar sobre os itens e imprimir um por um
    print(animal)


with open("animais.csv", "w", encoding="utf-8") as arquivo: # escrever no arquivo CSV
    for animal in animais:
        arquivo.write(animal + "\n")

print("Arquivo salvo com sucesso!")