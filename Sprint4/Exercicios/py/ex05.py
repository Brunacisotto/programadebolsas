## exercicio05

def processar_notas(estudantes_csv):
    with open(estudantes_csv, 'r') as file:
        linhas = file.readlines()

    relatorio = []
    for linha in linhas:
        dados = linha.strip().split(',')
        nomes = dados[0]
        notas = sorted(map(float, dados[1:]), reverse=True)[:3]
        media = round(sum(notas) / 3, 2)
        relatorio.append((nomes, notas, media))

    relatorioordenado = sorted(relatorio, key=lambda x: x[0])

    for nomes, notas, media in relatorioordenado:
        notasformatadas = [int(nota)
        if nota.is_integer()
        else round(nota, 2)
        for nota in notas]

        if media.is_integer():
            mediaformatada = f"{int(media)}.0"
        else:
            mediaformatada = f"{media:.2f}"

        print(f"Nome: {nomes} Notas: {notasformatadas} Média: {mediaformatada}")

processar_notas('estudantes.csv')