## exercicio05
def processar_notas(estudantes_csv):
    with open(estudantes_csv, 'r') as file:
        linhas = file.readlines()

    relatorio = []
    for linha in linhas:
        dados = linha.strip().split(',')
        nomes = dados[0]
        notas = sorted(map(int, dados[1:]), reverse=True)[:3]
        media = round(sum(notas) / 3, 2)
        relatorio.append((nomes, notas, media))

    relatorioordenado = sorted(relatorio, key=lambda x: x[0])

    for nomes, notas, media in relatorioordenado:
        print(f"Nome: {nomes} Notas: {notas} Média: {media:}")
processar_notas('estudantes.csv')