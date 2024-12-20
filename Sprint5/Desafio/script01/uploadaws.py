#!/usr/bin/env python
# coding: utf-8

# In[26]:


import boto3
import pandas as pd

session = boto3.Session(profile_name='AdministratorAccess-794038242332')

s3 = session.client('s3')


# In[27]:


# Listar buckets disponíveis
buckets = s3.list_buckets()
print("Buckets disponíveis:")
for bucket in buckets['Buckets']:
    print(f"- {bucket['Name']}")


# In[23]:


bucket_name = 'desafio-sprint5'
file_path = "C:\\Users\\sidci\\OneDrive\\Documentos\\Bruna\\compass\\sprint5\\view_dados_abertos_ogu_2024091\\view_dados_abertos_ogu_202411051652.csv"
s3_key = 'uploads/dadosogu.csv'

# Upload do arquivo
try:
    s3.upload_file(Filename=file_path, Bucket=bucket_name, Key=s3_key)
    print("Arquivo enviado com sucesso para o S3!")
except Exception as e:
    print("Erro ao enviar o arquivo:", e)


# In[ ]:




