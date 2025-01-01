import os
import pandas as pd
import boto3
from datetime import datetime

#CONFIGURAÇOES E AUTENTICACAO 

# autenticação na AWS com variaveis de ambiente
aws_access_key = os.getenv("AWS_ACCESS_KEY_ID")
aws_secret_key = os.getenv("AWS_SECRET_ACCESS_KEY")
aws_session_token = os.getenv("AWS_SESSION_TOKEN")

# criando sessao AWS e cliente
session = boto3.Session(
    aws_access_key_id=aws_access_key,
    aws_secret_access_key=aws_secret_key,
    aws_session_token=aws_session_token
)
s3 = session.client('s3')

## LEITURA DOS DADOS 
data_folder = "data" #pasta em que se encontram os arquivos movies e series
movies_path = os.path.join(data_folder, 'movies.csv') #criando caminho completo a partir da pasta data
series_path = os.path.join(data_folder, 'series.csv')

movies = pd.read_csv(movies_path, sep='|', low_memory=False) #lendo os arquivos
series = pd.read_csv(series_path, sep='|', low_memory=False)

##DEFINICAO DE FUNCOES
def upload_s3(nome_do_bucket, camada_armazenamento, local, origem_dados, caminhos_arquivos): # definindo função para fazer upload para o bucket
    data_processamento = datetime.now().strftime("%Y-%m-%d") #pegando a data atual do sistema
    for caminho_arquivo in caminhos_arquivos: #enviar vários arquivos em uma execucao 
        try:
            nome_arquivo = caminho_arquivo.split('/')[-1] #pegamendo só o nome do arquivo a partir do caminho completo
            chave_s3 = f"{camada_armazenamento}/{local}/{origem_dados}/{data_processamento}/{nome_arquivo}" #criando caminho de pastas no bucket

            print(f"Enviando {caminho_arquivo} para s3://{nome_do_bucket}/{chave_s3}...") 
            s3.upload_file(caminho_arquivo, nome_do_bucket, chave_s3) #usando a funcao upload_file para enviar o arquivo, usando o nome do ucket e o caminho de pastas
            print(f"Envio bem-sucedido de {nome_arquivo} para {nome_do_bucket}/{chave_s3}")

        except Exception as e:
            print(f"Ocorreu um erro: {e}") #exibir mensagem de erro, caso haja algum 

##EXECUCAO DO SCRIPT
if __name__ == "__main__": #executando o codigo apenas quando o script é rodado diretamente, e não se ele for importado como um módulo em outro script
    bucket = "desafiofinal-filmeseseries"
    camada = "raw"
    local = "local"

    upload_s3(bucket, camada, local, "csv/movies", [movies_path]) #enviando csv movies 

    upload_s3(bucket, camada, local, "csv/series", [series_path]) #enviando csv series
