#!/usr/bin/env python
# coding: utf-8

# In[1]:


import boto3
import pandas as pd

session = boto3.Session(profile_name='AdministratorAccess-794038242332')

s3 = session.client('s3')


# In[3]:


# Parâmetros do download
bucket_name = 'desafio-sprint5'  
s3_key = 'uploads/dadosogu.csv' 
local_file_path = 'C:/Users/sidci/OneDrive/Documentos/Bruna/compass/sprint5/dadosogu_baixado.csv'

try:
    s3.download_file(Bucket=bucket_name, Key=s3_key, Filename=local_file_path)
    print("Arquivo baixado com sucesso!")
except Exception as e:
    print("Erro ao baixar o arquivo:", e)


# In[4]:


dadosgov = pd.read_csv('dadosogu_baixado.csv', sep='|', dtype={19: object})


# In[5]:


dadosgov


# In[6]:


dadosgov.shape


# In[7]:


dadosgov = dadosgov.drop_duplicates() ##apagar duplicadas


# In[8]:


dadosgov.shape


# In[9]:


dadosgov.info()


# In[10]:


dadosgov.nunique ()


# In[11]:


dadosgov.isnull().sum()


# In[12]:


dadosgov[dadosgov.txt_regiao.isnull()]


# In[13]:


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


# In[14]:


dadosgov[dadosgov.txt_regiao.isnull()]


# In[15]:


dadosgov[dadosgov.val_desembolsado.isnull()]


# In[16]:


dadosgov.loc[dadosgov['val_desembolsado'].isna(), 'val_desembolsado'] = 0


# In[17]:


dadosgov[dadosgov.val_desembolsado.isnull()]


# In[18]:


dadosgov[dadosgov.qtd_uh_entregues.isnull()]


# In[19]:


dadosgov.loc[dadosgov.qtd_uh_entregues.isnull(), 'qtd_uh_entregues'] = 0.0


# In[20]:


dadosgov[dadosgov.qtd_uh_entregues.isnull()]


# In[21]:


dadosgov.info()


# In[22]:


dadosgov['data_referencia'].nunique()


# In[23]:


colunas_remover = [
    'data_referencia',
    'txt_cnpj_construtora_entidade',
    'txt_nome_construtora_entidade',
    'txt_endereco',
    'txt_cep'
]
dadosgov = dadosgov.drop(columns=colunas_remover)


# In[24]:


dadosgov.head(3)


# In[25]:


dadosgov.info()


# In[26]:


dadosgov


# In[27]:


dadosgov.info()


# In[28]:


#dadosgov['dt_assinatura'] = pd.to_datetime(dadosgov['dt_assinatura'], format='%d/%m/%Y')


# In[29]:


dadosgov['qtd_uh'] = dadosgov['qtd_uh'].astype(int)


# In[30]:


dadosgov['qtd_uh_vigentes'] = dadosgov['qtd_uh_vigentes'].astype(int)


# In[31]:


dadosgov['qtd_uh_entregues'] = dadosgov['qtd_uh_entregues'].astype(float).astype(int)


# In[32]:


dadosgov['val_desembolsado'] = (dadosgov['val_desembolsado']
    .str.replace('.', '', regex=False) 
    .str.replace(',', '.', regex=False)  
    .astype(float))


# In[33]:


dadosgov['val_contratado_total'] = (
    dadosgov['val_contratado_total']
    .str.replace('.', '', regex=False) 
    .str.replace(',', '.', regex=False)  
    .astype(float))


# In[34]:


dadosgov.info()


# In[35]:


dadosgov.to_csv('dadosok.csv')


# In[37]:


bucket_name = 'desafio-sprint5'
file_path = "C:\\Users\\sidci\\OneDrive\\Documentos\\Bruna\\compass\\sprint5\\dadosok.csv"
s3_key = 'uploads/dadosogutratado.csv'

try:
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key=s3_key)
    print("Arquivo enviado com sucesso para o S3!")
except Exception as e:
    print("Erro ao enviar o arquivo:", e)


# In[ ]:




