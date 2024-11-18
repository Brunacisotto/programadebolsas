# exercicio 16 parte 2

num: str = "1,3,4,6,10,76"
lista: list = num.split(',')
print(sum(int(i) for i in lista))
