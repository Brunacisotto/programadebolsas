import requests
import os
import json
import boto3
from datetime import datetime

# Inicializando o cliente S3
s3_client = boto3.client('s3')

def lambda_handler(event, context): # Função Lambda 
    
    try: # chamar função que processa filmes relacionados a Stephen King
        filmes_com_stephen_king()
        return {
            "statusCode": 200,
            "body": json.dumps('Processamento realizado com sucesso!')
        }
    except Exception as e:
        print(f"Erro no processamento: {e}")
        return {
            "statusCode": 500,
            "body": json.dumps(f'Erro interno: {e}')
        }





def filmes_com_stephen_king():  # buscar todos os filmes relacionados a Stephen King
    
    API_KEY = os.getenv('APIKEYTMDB') #armazenei a apikey como variavel de ambiente
    BASE_URL = 'https://api.themoviedb.org/3'
    
    url = f"{BASE_URL}/person/3027/movie_credits"  # url que busca créditos de filmes de Stephen King (ID do artista 3027 no tbdb)
    params = {
        'api_key': API_KEY, #definicao de parametros 
        'language': 'pt-BR'
    }
    response = requests.get(url, params=params) # requisicao get para a api 
    if response.status_code != 200: ## se a resposta não é de sucesso, ou seja, status diferente de 200, exibir mensagem de erro
        print("Erro ao buscar filmes de Stephen King.")
        return





    
    filmes = response.json().get('cast', []) + response.json().get('crew', [])# combina todos os filmes relacionados a Stephen King no cast ou crew
    dados_filmes = [] # lista vazia para armazenar os dados de cada filme

    for filme in filmes:  # itera sobre cada filme retornado pela API.
        detalhes = obter_detalhes_completos(filme['id'], API_KEY, BASE_URL) # obtem os detalhes completos do filme usando id e a função auxiliar obter_detalhes_completos
        keywords = obter_keywords(filme['id'], API_KEY, BASE_URL)  # obtem as palavras-chave associadas ao filme usando a função auxiliar obter_keywords
        diretor = obter_diretor(detalhes.get('credits', {}))   # identifica o diretor do filme a partir dos dados de créditos obtidos nos detalhes

        # puxar os dados de cada filme
        dados_filmes.append({
            "id": detalhes.get('id', 'N/A'),
            "production_companies": [p.get('name') for p in detalhes.get('production_companies', [])],
            "imdb_id": detalhes.get('imdb_id', 'N/A'),
            "popularity": detalhes.get('popularity', 'N/A'),
            "revenue": detalhes.get('revenue', 'N/A'),
            "budget": detalhes.get('budget', 'N/A'),
            "job": filme.get('job', 'N/A'),
            "department": filme.get('department', 'N/A'),
            "keywords": keywords,
            "director": diretor
        })
    
    upload_s3(
        dados=dados_filmes, # dados dos filmes processados que serão enviados para o S3.
        bucket_name='desafiofinal-filmeseseries', #nome do bucket
        base_path_s3='raw/tmdb/json', #caminho dentro do bucket
        nome_base_arquivo='filmes_stephen_king_brutos' #nome para salvar os arquivos
    )





def obter_detalhes_completos(filme_id, API_KEY, BASE_URL): # detalhes completos de um filme pelo id usando a api do tmdb
    
    url = f"{BASE_URL}/movie/{filme_id}" # url para buscar os detalhes de um filme com base no seu id
    params = {
        'api_key': API_KEY, #definicao de parametros 
        'language': 'pt-BR',
        'append_to_response': 'credits' # incluir informações adicionais, como os créditos do filme  diretor
    }
    response = requests.get(url, params=params) # requisição get para a api usando a URL e os parâmetros definidos anteriormente
    if response.status_code == 200: #verificar se a resposta foi sucesso (200)
        return response.json()  # Retorna os dados brutos da api em json
    else:
        print(f"Erro ao obter detalhes do filme {filme_id}: {response.status_code}")
        return {}

def obter_diretor(credits): # puxar nome do diretor dos créditos de um filme
    
    crew = credits.get('crew', []) # funcao get para membros da equipe técnica dos créditos se não, retorna uma lista vazia
    if not crew: 
        print("Nenhuma equipe técnica encontrada nos créditos")
    for pessoa in crew:
        if pessoa.get('job') == 'Director':  # verifica se a função da pessoa é director
            return pessoa.get('name', 'N/A')
    print("diretor não encontrado nos créditos") # retorna o nome do diretor ou que não exite
    return 'N/A'






def obter_keywords(filme_id, API_KEY, BASE_URL): # pega palavras-chave associadas a um filme pelo id
    
    url = f"{BASE_URL}/movie/{filme_id}/keywords" # url para buscar as palavras-chave de um filme com base no id
    params = {'api_key': API_KEY} #definicao de parametros 
    response = requests.get(url, params=params) # requisição get para a api usando a url e os parametros 
    if response.status_code == 200: # verificar se a resposta foi sucesso (200)
        return [kw['name'] for kw in response.json().get('keywords', [])] # extrai e retorna os nomes das palavras-chave da resposta JSON
        
    else:
        print(f"Erro ao obter keywords do filme {filme_id}: {response.status_code}") # se não retorna lista vazia 
        return []
    






def upload_s3(dados, bucket_name, base_path_s3, nome_base_arquivo, tamanho_grupo=100): # faz upload dos dados para o Amazon S3 em grupos de 100
    
    # Obtém a data atual para criar o esquema de pastas
    data_atual = datetime.now()
    ano = data_atual.strftime('%Y')
    mes = data_atual.strftime('%m')
    dia = data_atual.strftime('%d')

    
    caminho_base = f"{base_path_s3}/{ano}/{mes}/{dia}" # caminho para armazenar os arquivos no S3

    for i in range(0, len(dados), tamanho_grupo): # divide os dados em grupos menores de acordo com o tamanho especificado (100)
        grupo = dados[i:i + tamanho_grupo]
        nome_arquivo = f"{nome_base_arquivo}_{i // tamanho_grupo + 1}.json"  # cria o nome do arquivo, indicando o número do grupo
        caminho_s3 = f"{caminho_base}/{nome_arquivo}"

        
        json_data = json.dumps(grupo, ensure_ascii=False, indent=4) # converte o grupo de dados para JSON em memória

        try:
            # envia os JSON para S3 usando a boto3, mostra mensagem de erro caso aja algum 
            s3_client.put_object(
                Bucket=bucket_name,
                Key=caminho_s3,
                Body=json_data,
                ContentType='application/json' 
            )
            print(f"Arquivo salvo no bucket: s3://{bucket_name}/{caminho_s3}")
        except Exception as e:
            print(f"Erro ao salvar o arquivo {nome_arquivo} no S3 no bucket {bucket_name}: {e}")
