#exercicio 17 parte 2
def dividir_lista(lista):
    tamanho = len(lista)
    parte = tamanho // 3  
    parte_um = lista[:parte]
    parte_dois = lista[parte:2*parte]
    parte_tres = lista[2*parte:]
    return parte_um, parte_dois, parte_tres  # Retorna as sublistas separadamente

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
lista1, lista2, lista3 = dividir_lista(lista)
print(lista1, lista2, lista3)
