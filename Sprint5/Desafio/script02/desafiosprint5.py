#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import pandas as pd

session = boto3.Session(profile_name='AdministratorAccess-794038242332')

s3 = session.client('s3')


# In[2]:


# Parâmetros do download
bucket_name = 'desafio-sprint5'  
s3_key = 'uploads/dadosogu.csv' 
local_file_path = 'C:/Users/sidci/OneDrive/Documentos/Bruna/compass/sprint5/dadosogu_baixado.csv'

try:
    s3.download_file(Bucket=bucket_name, Key=s3_key, Filename=local_file_path)
    print("Arquivo baixado com sucesso!")
except Exception as e:
    print("Erro ao baixar o arquivo:", e)


# In[3]:


dadosgov = pd.read_csv('dadosogu_baixado.csv', sep='|', dtype={19: object})


# In[4]:


dadosgov


# In[5]:


dadosgov.shape


# In[6]:


dadosgov = dadosgov.drop_duplicates() ##apagar duplicadas


# In[7]:


dadosgov.shape


# In[8]:


dadosgov.info()


# In[9]:


dadosgov.nunique ()


# In[10]:


dadosgov.isnull().sum()


# In[11]:


dadosgov[dadosgov.txt_regiao.isnull()]


# In[12]:


estado_para_regiao = {
    'AC': 'Norte', 'AL': 'Nordeste', 'AP': 'Norte', 'AM': 'Norte',
    'BA': 'Nordeste', 'CE': 'Nordeste', 'DF': 'Centro-Oeste', 'ES': 'Sudeste',
    'GO': 'Centro-Oeste', 'MA': 'Nordeste', 'MT': 'Centro-Oeste', 'MS': 'Centro-Oeste',
    'MG': 'Sudeste', 'PA': 'Norte', 'PB': 'Nordeste', 'PR': 'Sul',
    'PE': 'Nordeste', 'PI': 'Nordeste', 'RJ': 'Sudeste', 'RN': 'Nordeste',
    'RS': 'Sul', 'RO': 'Norte', 'RR': 'Norte', 'SC': 'Sul',
    'SP': 'Sudeste', 'SE': 'Nordeste', 'TO': 'Norte'
}
dadosgov.loc[dadosgov['txt_regiao'].isna(), 'txt_regiao'] = dadosgov['txt_sigla_uf'].map(estado_para_regiao)


# In[13]:


dadosgov[dadosgov.txt_regiao.isnull()]


# In[14]:


dadosgov[dadosgov.val_desembolsado.isnull()]


# In[15]:


dadosgov.loc[dadosgov['val_desembolsado'].isna(), 'val_desembolsado'] = 0


# In[16]:


dadosgov[dadosgov.val_desembolsado.isnull()]


# In[17]:


dadosgov[dadosgov.qtd_uh_entregues.isnull()]


# In[18]:


dadosgov.loc[dadosgov.qtd_uh_entregues.isnull(), 'qtd_uh_entregues'] = 0.0


# In[19]:


dadosgov[dadosgov.qtd_uh_entregues.isnull()]


# In[20]:


dadosgov.info()


# In[21]:


dadosgov['data_referencia'].nunique()


# In[22]:


colunas_remover = [
    'data_referencia',
    'txt_cnpj_construtora_entidade',
    'txt_nome_construtora_entidade',
    'txt_endereco',
    'txt_cep'
]
dadosgov = dadosgov.drop(columns=colunas_remover)


# In[23]:


dadosgov.head(3)


# In[24]:


dadosgov.info()


# In[25]:


dadosgov


# In[26]:


dadosgov.info()


# In[27]:


dadosgov['qtd_uh'] = dadosgov['qtd_uh'].astype(int)


# In[28]:


dadosgov['qtd_uh_vigentes'] = dadosgov['qtd_uh_vigentes'].astype(int)


# In[29]:


dadosgov['qtd_uh_entregues'] = dadosgov['qtd_uh_entregues'].astype(float).astype(int)


# In[30]:


dadosgov['val_desembolsado'] = (dadosgov['val_desembolsado']
    .str.replace('.', '', regex=False) 
    .str.replace(',', '.', regex=False)  
    .astype(float))


# In[31]:


dadosgov['val_contratado_total'] = (
    dadosgov['val_contratado_total']
    .str.replace('.', '', regex=False) 
    .str.replace(',', '.', regex=False)  
    .astype(float))


# In[32]:


dadosgov.info()


# In[33]:


dadosgov.to_csv('dadosok.csv')


# In[34]:


bucket_name = 'desafio-sprint5'
file_path = "C:\\Users\\sidci\\OneDrive\\Documentos\\Bruna\\compass\\sprint5\\dadosok.csv"
s3_key = 'uploads/dadosogutratado.csv'

try:
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key=s3_key)
    print("Arquivo enviado com sucesso para o S3!")
except Exception as e:
    print("Erro ao enviar o arquivo:", e)


# A partir desse ponto começo a analise dos dados!

# In[35]:


bucket_name = 'desafio-sprint5'  
s3_key = 'uploads/dadosogutratado.csv' 
local_file_path = 'C:/Users/sidci/OneDrive/Documentos/Bruna/compass/dadosok.csv'

try:
    s3.download_file(Bucket=bucket_name, Key=s3_key, Filename=local_file_path)
    print("Arquivo baixado com sucesso!")
except Exception as e:
    print("Erro ao baixar o arquivo:", e)


# A pergunta a ser respondida nessa analise é: No ano de 2018, quais foram as 10 cidades da região SUL, que mais tiveram imóveis concluídos e entregues subsidiados pela OGU , por intermedio de bancos públicos?

# In[36]:


dadosanalise = pd.read_csv ('dadosok.csv')


# In[37]:


dadosanalise


# In[38]:


dadosanalise.info ()


# Uma função de conversão (convertendo o campo dt_assinatura para formato datetime)

# In[39]:


dadosanalise['dt_assinatura'] = pd.to_datetime(dadosanalise['dt_assinatura'], format='%d/%m/%Y')


# In[40]:


dadosanalise.info()


# Uma função de String (convertendo para Maiusculas o campo txt_nome_municipio, txt_regiao, txt_nome_agente_financeiro)

# In[41]:


dadosanalise[['txt_nome_municipio', 'txt_regiao', 'txt_nome_agente_financeiro']] = \
dadosanalise[['txt_nome_municipio', 'txt_regiao', 'txt_nome_agente_financeiro']].apply(lambda col: col.str.upper())


# In[42]:


dadosanalise


# Função de data isolando apenas o ano de 2018

# In[43]:


dadosanalise['ano_assinatura'] = dadosanalise['dt_assinatura'].dt.year
df_2018 = dadosanalise[dadosanalise['ano_assinatura'] == 2018]


# In[44]:


df_2018


# Função de condicional para txt_situacao_do_empreendimento, por condicionando á "Concluído"

# In[55]:


df_2018.loc[:,'concluido'] = df_2018['txt_situacao_empreendimento'].apply(lambda x: True if x == 'Concluído' else False)
df_concluidos = df_2018[df_2018['concluido']]


# In[56]:


df_concluidos


# filtro de dados, com dois operadores lógicos, para bancos públicos (BB e CAIXA) e região SUL

# In[47]:


filtrologico = ((df_concluidos['txt_nome_agente_financeiro'] == 'CAIXA') | 
                (df_concluidos['txt_nome_agente_financeiro'] == 'BB')) & \
                (df_concluidos['txt_regiao'] == 'SUL')


# In[48]:


df_filtrado = df_concluidos[filtrologico]


# In[49]:


df_filtrado


# ao menos 2 funçoes de agregação (groupby e sum)

# In[50]:


df_resultado = df_filtrado.groupby(['txt_nome_municipio']).agg({
    'qtd_uh_entregues': 'sum',            
    'val_desembolsado': 'sum',  
     'txt_sigla_uf': 'first',    
   }).sort_values('qtd_uh_entregues', ascending=False) 


# In[51]:


df_resultado.head(10)


# In[52]:


df_analise = df_resultado.head(10)


# In[53]:


df_analise.to_csv('analisecidades.csv')


# In[54]:


bucket_name = 'desafio-sprint5'
file_path = "C:\\Users\\sidci\\OneDrive\\Documentos\\Bruna\\compass\\sprint5\\analisecidades.csv"
s3_key = 'uploads/analisecidades.csv'

try:
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key=s3_key)
    print("Arquivo enviado com sucesso para o S3!")
except Exception as e:
    print("Erro ao enviar o arquivo:", e)

