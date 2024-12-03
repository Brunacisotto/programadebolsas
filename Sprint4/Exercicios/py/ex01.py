#exercicio 01

def processar_numeros(arquivo: str):
    with open(arquivo, 'r') as file:
        cincomaiores_pares = sorted(
            filter(lambda x: x % 2 == 0, map(int, file.readlines())),
            reverse=True
        )[:5]
        soma = sum(cincomaiores_pares)
    return cincomaiores_pares, soma
cincomaiores, soma = processar_numeros('number.txt')
print(cincomaiores)
print(soma)