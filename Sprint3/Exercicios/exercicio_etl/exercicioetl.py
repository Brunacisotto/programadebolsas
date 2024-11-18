import re

COLUNA_NOME_ATOR = 0
COLUNA_TOTAL_BRUTO = 1
COLUNA_NUMERO_FILMES = 2
COLUNA_MEDIA_POR_FILME = 3
COLUNA_PRIMEIRO_FILME = 4
COLUNA_BRUTO = 5

def resgatarFilmeComMaisFrequencia(lista_atores: list) -> list:
    resultado: list = []
    verificar_se_filme_na_lista: list = []
    for linha in lista_atores:
        if linha[COLUNA_PRIMEIRO_FILME] in verificar_se_filme_na_lista:
            for res in resultado:
                if res[0] == linha[COLUNA_PRIMEIRO_FILME]:
                    res[1] += 1
        else:
            verificar_se_filme_na_lista.append(linha[COLUNA_PRIMEIRO_FILME])
            resultado.append([linha[COLUNA_PRIMEIRO_FILME], 1])

    return sorted(resultado, key = lambda x: x[1], reverse=True)

def resgataAtoresCsv(path: str) -> list:
    lista_atores = []
    count = 0
    PATTERN = re.compile(r'''((?:[^,"']|"[^"]*"|'[^']*')+)''')
    with open(path, 'r') as file:
        for line in file:
            if not count:
                count += 1
            else:
                rows = PATTERN.split(line)[1::2]
                lista_atores.append((rows))

    print(sorted(lista_atores, key = lambda x: x[0], reverse=False))
    return lista_atores

#main
lista_atores: list = resgataAtoresCsv('./actors.csv')

#01 - ator com maior n de filmes n de filmes
ator_maior_numero_filmes: list = sorted(lista_atores, key = lambda x: x[COLUNA_NUMERO_FILMES], reverse=True)[0]
print(ator_maior_numero_filmes[0], ator_maior_numero_filmes[2])
texto_tarefa1: bytes = bytes(f'{ator_maior_numero_filmes[COLUNA_NOME_ATOR]} {ator_maior_numero_filmes[COLUNA_NUMERO_FILMES]}', 'utf-8')
open('./tarefa1.txt', "wb").write(texto_tarefa1)

#02 - media do n de filmes por ator
media_numero_filmes: float = sum(map(lambda x: int(x[COLUNA_NUMERO_FILMES]), lista_atores)) / len(lista_atores)
print(media_numero_filmes)
texto_tarefa2: bytes = bytes(f'{media_numero_filmes}', 'utf-8')
open('./tarefa2.txt', "wb").write(texto_tarefa2)

#03 - ator com a maior media por filme
ator_maior_media: list = sorted(lista_atores, key = lambda x: x[COLUNA_MEDIA_POR_FILME], reverse=True)[0]
print(ator_maior_media[0])
texto_tarefa3: bytes = bytes(f'{ator_maior_media[COLUNA_NOME_ATOR]}', 'utf-8')
open('./tarefa3.txt', "wb").write(texto_tarefa3)

#04 - nome dos filmes mais frequentes e frequencia
filme_com_mais_frequencia: list = resgatarFilmeComMaisFrequencia(lista_atores)
print(filme_com_mais_frequencia)
texto_tarefa4: str = ""
for i in filme_com_mais_frequencia:
    texto_tarefa4 += f"{i[0]} {i[1]}\n"
bytes_tarefa4: bytes = bytes(texto_tarefa4, 'utf-8')

open('./tarefa4.txt', "wb").write(bytes_tarefa4)

#05 - lista dos atores ordenada por pagamento
atores_pagamentos: list = sorted(lista_atores, key = lambda x: x[COLUNA_TOTAL_BRUTO], reverse=True)
print(atores_pagamentos)
texto_tarefa5: str = ""
for i in atores_pagamentos:
    texto_tarefa5 += f"{i[COLUNA_NOME_ATOR]} {i[COLUNA_TOTAL_BRUTO]}\n"

open('./tarefa5.txt', "wb").write(bytes(texto_tarefa5, 'utf-8'))