# exercicio 14 parte 2

def imprimir_valores(*args, **kwargs):
    for i in args:
        print(i)
    for i in kwargs:
        print(kwargs[i])

imprimir_valores(1, 3, 4, 'hello', parametro_nomeado ='alguma coisa', x=20)