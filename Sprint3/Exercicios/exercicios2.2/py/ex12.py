# exercicio 12 parte2

def my_map(lista, funcao):
       nova_lista = list(map(funcao, lista))
       return nova_lista
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = my_map(numeros, lambda x: x ** 2)
print(resultado)