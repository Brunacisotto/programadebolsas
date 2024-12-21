# Desafio - Sprint 5

O desafio da Sprint 5 solicitava que, no site [dados.gov.br](https://dados.gov.br), encontrássemos uma base de dados para análise. Essa base de dados deveria estar no formato CSV ou JSON e ser carregada em um bucket S3. Posteriormente, os dados deveriam ser tratados, analisados, e os resultados desse processo também deveriam ser armazenados no bucket. Para isso, utilizamos as bibliotecas **Pandas** e **BOTO3**.

## Escolha da Base de Dados

Escolhi uma base de dados referente ao programa Minha Casa Minha Vida, do Ministério das Cidades, disponível no seguinte endereço:  
[**Bases de Dados do Programa Minha Casa Minha Vida**](https://www.gov.br/cidades/pt-br/acesso-a-informacao/acoes-e-programas/habitacao/programa-minha-casa-minha-vida/bases-de-dados-do-programa-minha-casa-minha-vida)

Esse dataset contém informações sobre operações contratadas no âmbito do Programa Minha Casa Minha Vida, utilizando recursos do Orçamento Geral da União (OGU).  
A tabela com o dicionário dos dados pode ser encontrada [dicionáriodedados](../Desafio/arquivoscsv/dicionariodedados/Dicionario_dos_conjuntos_de_dados_MCMV__FGTS_e_OGU.pdf)

### Pergunta para Análise

Na análise proposta, busquei responder à seguinte questão:  
**No ano de 2018, quais foram as 10 cidades da região Sul do Brasil que mais tiveram imóveis concluídos e entregues subsidiados pela OGU, por intermédio de bancos públicos (Caixa ou BB)?**

---

## Primeiros Passos

1. **Carregamento do Arquivo no S3**  
   - Autenticação através do AWS CLI.  
   - Listagem dos buckets disponíveis na AWS.  
   - Definição de parâmetros para upload do arquivo.  

   ![criaçaobucket](../Evidencias/tratamento%20de%20dados/criacaobucket.png)

   ![passo1](../Evidencias/tratamento%20de%20dados/tratamento00.png)

   
2. **Tratamento de Dados**  

 Em outro Script 
   - Download do arquivo do S3 para análise.  

   ![passo2](../Evidencias/tratamento%20de%20dados/tratamento1.png)


   - Exploração inicial do dataset.  

   ![passo3](../Evidencias/tratamento%20de%20dados/tratamento2.png)


   - Limpeza e preparação dos dados:
  
     - Remoção de linhas duplicadas.  

     ![passo4](../Evidencias/tratamento%20de%20dados/tratamento3.png)


     - Tratamento de valores nulos (NaN), preenchendo-os conforme os padrões observados.  

     ![passo5](../Evidencias/tratamento%20de%20dados/tratamento4.png)
     ![passo6](../Evidencias/tratamento%20de%20dados/tratamento5.png)
     ![passo7](../Evidencias/tratamento%20de%20dados/tratamento6.png)
     ![passo8](../Evidencias/tratamento%20de%20dados/tratamento7.png)
     ![passo9](../Evidencias/tratamento%20de%20dados/tratamento8.png)

     - Exclusão de colunas irrelevantes para a análise.  

     ![passo10](../Evidencias/tratamento%20de%20dados/tratamento9.png)


     - Conversão de campos numéricos que estavam configurados como `object` para o formato adequado.

     ![passo11](../Evidencias/tratamento%20de%20dados/tratamento10.png)

     - Upload do arquivo tratado de volta ao bucket S3.  
     ![passo12](../Evidencias/tratamento%20de%20dados/tratamento11.png)

   

---

## Análise dos Dados

Para responder à pergunta proposta, utilizei as seguintes manipulações propostas no desafio, seguindo os  passos:

1. **Preparação dos Dados**  
   - Baixei o arquivo tratado do bucket S3.  

   ![passo13](../Evidencias/analise%20de%20dados/analise1.png) 

   ![passo14](../Evidencias/analise%20de%20dados/analise2.png) 



   -1 Função de conversão: Converti o campo `dt_assinatura` para o formato `datetime`, pois estava configurado como `object`. 

   ![passo15](../Evidencias/analise%20de%20dados/analise3.png) 

   - 1 Função de String: Padronizei todos os nomes de cidades, regiões e agentes financeiros em letras maiúsculas para facilitar os filtros.  

   ![passo16](../Evidencias/analise%20de%20dados/analise4.png) 

   - 1 Função de data: Extraí apenas o ano do campo `dt_assinatura` e selecionei registros de 2018.  

   ![passo17](../Evidencias/analise%20de%20dados/analise5.png) 

   - 1 Função de condicional: Considerei apenas os empreendimentos com a situação marcada como "Concluído".  

   ![passo18](../Evidencias/analise%20de%20dados/analise6.png) 

   -Clausula utilizando dois operadores lógicos: Filtrei os dados para instituições financeiras públicas, restringindo à "CAIXA" ou (|) "BB".  

   - (&)Limitei a análise à região Sul do Brasil.  

   ![passo19](../Evidencias/analise%20de%20dados/analise7.png) 
   
   - 2 funções de agregação: Agrupei os dados por nome dos municípios utilizando `groupby`.  
   - Calculei o total de unidades entregues em cada cidade (`SUM`).  
   - Incluí a soma do valor total desembolsado e o estado de cada cidade para enriquecer a análise.  

   ![passo20](../Evidencias/analise%20de%20dados/analise8.png) 
  

---

## Resultados da Análise

As 10 cidades da região Sul que mais tiveram imóveis concluídos e subsidiados pela OGU, por intermédio de bancos públicos (Caixa e BB), no ano de 2018, são:  

![listafinal](../Evidencias/analise%20de%20dados/listafinal.png) 

---

## Conclusão

Com essa análise, foi possível identificar as cidades que mais se beneficiaram do programa no ano de 2018 na região Sul do Brasil. O município de **Foz do Iguaçu (PR)** destacou-se como o principal beneficiário, com 916 unidades entregues, com um valor investido pelo governo de R$ 73.280.000.00. Observa-se que a 50% das das cidades listadas são do estado do Paraná, e que a diferença entre a primeira e a última cidade no ranking foi de 762 moradias.  

O arquivo final gerado foi enviado de volta ao bucket S3 para armazenamento.

 ![passo21](../Evidencias/analise%20de%20dados/analise9.png) 

 O resultado do Bucket após as manipulaçõs ficou assim:

 ![bucket](../Evidencias/tratamento%20de%20dados/bucket.png)
 ![bucket](../Evidencias/tratamento%20de%20dados/bucket2.png)

 Os arquivos csv utilizados se encontram aqui:

 [csvbruto](../Desafio/arquivoscsv/1arquivobaixado/dadosogu_baixado.csv)
 [csvlimpo](../Desafio/arquivoscsv/2arquivotratado/dadosok.csv)
 [csvfinal](../Desafio/arquivoscsv/3arquivoanalise/analisecidades.csv)

 Os scripts gerados se encontram aqui:

[script1py](../Desafio/script01/upload.py)
[script1ipynb](../Desafio/script01/upload.ipynb)

[script2py](../Desafio/script02/desafiosprint5.py)
[script2ipynb](../Desafio/script02/desafiosprint5.ipynb)


O Link para meu bucket da AWS:

[txtlink](../Desafio/linkparabucket.txt)
[linkbucket](https://desafio-sprint5.s3.us-east-1.amazonaws.com/uploads/)
[arn](arn:aws:s3:::desafio-sprint5)





--- 

