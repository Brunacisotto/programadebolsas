#exercicio 4 parte1



for numero in range(1, 101):
    primo = True
    if numero > 1:
        for n in range(2, numero):
            if numero % n == 0:
                primo = False
                break
        if primo:
            print(numero)