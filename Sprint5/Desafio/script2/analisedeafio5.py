#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import pandas as pd
import re

session = boto3.Session(profile_name='AdministratorAccess-794038242332')

s3 = session.client('s3')


# In[2]:


# Parâmetros do download
bucket_name = 'desafio-sprint5'  
s3_key = 'uploads/dadosogutratado.csv' 
local_file_path = 'C:/Users/sidci/OneDrive/Documentos/Bruna/compass/dadosok.csv'

try:
    s3.download_file(Bucket=bucket_name, Key=s3_key, Filename=local_file_path)
    print("Arquivo baixado com sucesso!")
except Exception as e:
    print("Erro ao baixar o arquivo:", e)


# A pergunta a ser respondida nessa analise é:
# No ano de 2018, quais foram as 10 cidades da região SUL, que mais tiveram imóveis concluídos e entregues subsidiados pela OGU , por intermedio de bancos públicos?

# In[3]:


dadosanalise = pd.read_csv ('dadosok.csv')


# In[4]:


dadosanalise


# In[5]:


dadosanalise.info ()


# Uma função de conversão (convertendo o campo dt_assinatura para formato datetime)

# In[6]:


dadosanalise['dt_assinatura'] = pd.to_datetime(dadosanalise['dt_assinatura'], format='%d/%m/%Y')


# In[66]:


dadosanalise.info()


# Uma função de String (convertendo para Maiusculas o campo txt_nome_municipio, txt_regiao, txt_nome_agente_financeiro)

# In[55]:


dadosanalise[['txt_nome_municipio', 'txt_regiao', 'txt_nome_agente_financeiro']] = \
dadosanalise[['txt_nome_municipio', 'txt_regiao', 'txt_nome_agente_financeiro']].apply(lambda col: col.str.upper())


# In[56]:


dadosanalise


# In[57]:


dadosanalise['ano_assinatura'] = dadosanalise['dt_assinatura'].dt.year
df_2018 = dadosanalise[dadosanalise['ano_assinatura'] == 2018]


# In[58]:


df_2018


# Função de condicional para txt_situacao_do_empreendimento, por condicionando á "Concluído"

# In[60]:


df_2018.loc[:,'concluido'] = df_2018['txt_situacao_empreendimento'].apply(lambda x: True if x == 'Concluído' else False)
df_concluidos = df_2018[df_2018['concluido']]


# In[61]:


df_concluidos


# In[ ]:


filtro de dados, com dois operadores lógicos, para bancos públicos (BB e CAIXA) e região SUL


# In[62]:


filtrologico = ((df_concluidos['txt_nome_agente_financeiro'] == 'CAIXA') | 
                (df_concluidos['txt_nome_agente_financeiro'] == 'BB')) & \
                (df_concluidos['txt_regiao'] == 'SUL')


# In[63]:


df_filtrado = df_concluidos[filtrologico]


# In[84]:


df_filtrado


# ao menos 2 funçoes de agregação (groupby e sum)

# In[95]:


df_resultado = df_filtrado.groupby(['txt_nome_municipio']).agg({
    'qtd_uh_entregues': 'sum',            
    'val_desembolsado': 'sum',  
     'txt_sigla_uf': 'first',    
   }).sort_values('qtd_uh_entregues', ascending=False)  # Ordena pela soma de qtd_uh_entregues


# In[96]:


df_resultado.head(10)


# In[86]:


df_analise = df_resultado.head(10)


# In[88]:


df_analise.to_csv('analisecidades.csv')


# In[89]:


bucket_name = 'desafio-sprint5'
file_path = "C:\\Users\\sidci\\OneDrive\\Documentos\\Bruna\\compass\\sprint5\\analisecidades.csv"
s3_key = 'uploads/analisecidades.csv'

try:
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key=s3_key)
    print("Arquivo enviado com sucesso para o S3!")
except Exception as e:
    print("Erro ao enviar o arquivo:", e)


# In[ ]:




