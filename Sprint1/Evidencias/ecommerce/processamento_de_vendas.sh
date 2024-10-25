######################################
#Arquivo: processamento_de_vendas_.sh#
#Autora: Bruna Cisotto               #
#Data de criacaoo:20/10/2024         #
#                                    #
# Desafio Sprint 1                   #
######################################

#!/bin/bash

cd /home/bruna/ecommerce
mkdir vendas #criando diretorio vendas
cp dados_de_vendas.csv vendas #copiando o arquivo dados_de_vendas para diretorio vendas
mkdir vendas/backup #criando diretorio backup dentro do diretorio vendas
cp dados_de_vendas.csv vendas/backup/dados-$(date +%Y%m%d).csv #copiando o arquivo dados de vendas para o diretorio vendas/backup e alterando o nome para dados -data do sistema.csv
cd vendas/backup #entrando no diretorio vendas/backup
mv dados-$(date +%Y%m%d).csv backup-dados-$(date +%Y%m%d).csv #mudando o nome de data para backup dados data
echo "$(date +'%Y/%m/%d %H:%M')" > relatorio-$(date +%Y%m%d).txt #adicionando data e hora para o arquivo relatorio
head -2 ../../dados_de_vendas.csv | tail -1 |awk -F , '{print $5}' >> relatorio-$(date +%Y%m%d).txt #adiocionando no arquivo relatorio a data do primeiro registro de venda
tail -1 ../../dados_de_vendas.csv |awk -F , '{print $5}' >> relatorio-$(date +%Y%m%d).txt  #adicionando ao arquivo relatorio a ultima data de venda
echo "$(( $(cat ../../dados_de_vendas.csv | awk -F , '{print $2}' | uniq -u | wc -l) - 1 ))" >> relatorio-$(date +%Y%m%d).txt #lendo o arquivo, separando apenas a coluna produtos, deixando apenas itens unicos, contando os itens e ecluindo o cabecalho
head -10 backup-dados-$(date +%Y%m%d).csv >> relatorio-$(date +%Y%m%d).txt #copiando 10 primeiras linhas
zip backup-dados-$(date +%Y%m%d).zip backup-dados-$(date +%Y%m%d).csv #compactando
rm backup-dados-$(date +%Y%m%d).csv #apagando backup-dados.csv 
cd ..
rm dados_de_vendas.csv #apagando_dados_de_vendas.csv
