# exercicio 19 parte2
import random

random_list = random.sample(range(500), 50)

valor_maximo = max(random_list)
valor_minimo = min(random_list)
soma = sum(random_list)
quantidade = len(random_list)
media = soma / quantidade


sorted_list = sorted(random_list)
if quantidade % 2 == 1:
    mediana = sorted_list[quantidade // 2]
else:
    meio1 = sorted_list[quantidade // 2 - 1]
    meio2 = sorted_list[quantidade // 2]
    mediana = (meio1 + meio2) / 2

print(f"Media: {media:.2f}, Mediana: {mediana}, Mínimo: {valor_minimo}, Máximo: {valor_maximo}")
