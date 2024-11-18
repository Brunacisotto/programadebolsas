#exercicio 7 parte 2

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
impares = []

for numero in a:
    if numero % 2 != 0:
        impares.append(numero)

print(impares)