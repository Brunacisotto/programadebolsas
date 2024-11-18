# exercicio 6 parte 2

a = [1, 1, 2, 3, 5, 8, 14, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

n1 = set(a)
n2 = set(b)

em_comum = n1.intersection(n2)
result = list(em_comum)
print(result)