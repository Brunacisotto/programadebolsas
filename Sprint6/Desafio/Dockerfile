FROM python:3.11-slim 
# escolhendo o diretório no container como /app
WORKDIR /app 
#copiando os arquivos desafio e requirements para o diretório do container 
COPY desafio.py requirements.txt ./
#copiando a pasta data para o diretório /app/data no container
COPY data/ ./data/
#instala as libs listadas no arquivo requirements (boto3 e pandas)
RUN pip install --no-cache-dir -r requirements.txt
# criando um volume para o diretório /app/data
VOLUME /app/data
#executa o script desafio.py com Python, quando rodo o container
CMD ["python", "desafio.py"]
