# exercicio 8 parte2

palavras = ['maça', 'arara', 'audio', 'radio', 'radar', 'moto']

for p in palavras:
     if p == p[::-1]:
        print(f"A palavra: {p} é um palíndromo")
     else:
        print(f"A palavra: {p} não é um palíndromo")