import requests
import pandas as pd
from IPython.display import display

api_key = 'coloquei aqui minha chave'

url = f"https://api.themoviedb.org/3/movie/top_rated?api_key={api_key}&language=pt-BR"

response = requests.get(url)
data = response.json()
filmes = []

for movie in data['results']:
   filme = {
      'Título': movie['title'],
      'Data de Lançamento': movie["release_date"],
      'Visão Geral': movie['overview'],
      'Votos': movie['vote_count'],
      'Média de Votos': movie['vote_average']
   }
   filmes.append(filme)

df = pd.DataFrame(filmes)

# Configurações para exibição completa no PyCharm
pd.set_option('display.max_rows', None)  # Exibe todas as linhas
pd.set_option('display.max_columns', None)  # Exibe todas as colunas
pd.set_option('display.width', None)  # Ajusta a largura 
pd.set_option('display.colheader_justify', 'center')  # Centraliza cabeçalhos

df.to_csv('filmes_top_rated.csv', index=False, encoding='utf-8')
print("Resultado salvo em 'filmes_top_rated.csv'.")

display(df)

