### Sprint 9 - Desafio

Na Sprint 9, avançamos para a **parte 4** de um total de 5 etapas do desafio "Filmes e Séries". O objetivo desta etapa era obter os arquivos armazenados na camada **Trusted** na sprint anterior, transformá-los e criar a camada **Refined** no **bucket S3**, garantindo que os dados fossem devidamente persistidos. Para alcançar esse objetivo, utilizamos o **Apache Spark** por meio de um **job do AWS Glue**.

A modelagem dos dados foi realizada de forma multidimensional, permitindo que as informações fossem consultadas sob diferentes perspectivas.

A seguir, detalho os passos que executei para concluir este desafio:

#### Passo 1 (desenvolvendo o job no Glue)

Iniciando o Job no Glue e importando as bibliotecas necessárias.

![jobglue01](../Evidencias/codigo/codigo01.png)

Apontando o bucket de origem dos dados 

![jobglue02](../Evidencias/codigo/codigo02.png)

Carregando os arquivos parquet tanto local como do tmdb

![jobglue03](../Evidencias/codigo/codigo03.png)

Fazendo o join das duas fontes de dados (local e tmdb), para fazer esse join escolhi a id_tmdb, que foi um campo que já trouxe da api do tmdb na sprint 7, já pensando em nessa fase usar com esse fim, aqui também escolhi de fato os dados que seriam usados na minha analise.

![jobglue04](../Evidencias/codigo/codigo04.png)

Filtrando os dados de receita e orçamento que não deveriam ser nulos ou iguais a zero, pois dependo desses dados terem valores para fazer a minha analise de quanto os filmes faturaram, também acrescentei aqui a coluna lucro_liquido que faz a subtracao entre orcamento e receita.

![jobglue05](../Evidencias/codigo/codigo05.png)

![jobglue06](../Evidencias/codigo/codigo06.png)

Decidi criar uma dimensao de tempo e por isso criei um id para cada ano, e apontei qual a decada que cada filme foi lançado, pois irei analisar se houve alguma década em que os filmes do autor foram mais populares.

 ![jobglue07](../Evidencias/codigo/codigo07.png)

Criando uma dimensão para filmes, com os campos que achei oportunos para essa tabela

![jobglue08](../Evidencias/codigo/codigo08.png)

Algumas colunas eram multivaloradas (generos e produtoras) explodi elas.

![jobglue09](../Evidencias/codigo/codigo09.png)

Criando as tabelas de dimesões necessárias para analise, sendo elas produtoras, generos, diretores e departamentos

![jobglue10](../Evidencias/codigo/codigo10.png)

Fazendo os joins dessas colunas com a tabela fato

![jobglue11](../Evidencias/codigo/codigo11.png)

Agrupando pelo id_imdb e agrupando as colunas que são multivaloradas, usei o set porque elas algumas vezes se repetiam na fato, com o uso do set esse problema foi resolvido 

![jobglue12](../Evidencias/codigo/codigo12.png)

Salvando as tabelas de dimensoes na camada refined 

![jobglue13](../Evidencias/codigo/codigo13.png)

![jobglue14](../Evidencias/codigo/codigo14.png)

#### Passo 2 (rodando o job)

Após algumas tentativas o job rodou e salvou os arquivos parquet no bucket.

![jobglue15](../Evidencias/crawler/glue02.png)

![jobglue16](../Evidencias/crawler/glue01.png)

Aqui está a estrutura que ficou o bucket 

![bucket01](../Evidencias/bucket/bucket01.png)

![bucket02](../Evidencias/bucket/bucket02.png)

![bucket03](../Evidencias/bucket/bucket03.png)

dim_departamento 

![bucket04](../Evidencias/bucket/bucket04.png)

dim_diretor

![bucket05](../Evidencias/bucket/bucket05.png)

dim_filme

![bucket06](../Evidencias/bucket/bucket06.png)

dim_genero

![bucket07](../Evidencias/bucket/bucket07.png)

dim_produtora

![bucket08](../Evidencias/bucket/bucket08.png)

dim_tempo

![bucket09](../Evidencias/bucket/bucket09.png)

fato_filme

![bucket10](../Evidencias/bucket/bucket10.png)


#### Passo 3 (fazendo o crawler e criando as tabelas no Glue Data Catalog)

Executando o Crawler 

![crawler](../Evidencias/crawler/crawler.png)

DataCatalogs criadas

![database1](../Evidencias/crawler/database.png)

![database2](../Evidencias/crawler/datacatalog.png)


#### Passo 4 (executando consultas no Athena)

Com as tabelas criadas consultei as mesmas no Athena e esses foram os resultados.

![dim_departamento](../Evidencias/athena/athenadepartamento.png)

![dim_tempo](../Evidencias/athena/athenatempo.png)

![dim_filme](../Evidencias/athena/athenafilme.png)

![dim_produtoras](../Evidencias/athena/athenaprodutora.png)

![dim_diretor](../Evidencias/athena/athenadiretor.png)

![dim_genero](../Evidencias/athena/athenagenero.png)

![fato_filme](../Evidencias/athena/athenafato.png)

Aqui estão os arquivos csv dessas tabelas 

[dim_departamento](../Desafio/csvs%20tabelas/dim_departamento.csv)

[dim_tempo](../Desafio/csvs%20tabelas/dim_tempo.csv)

[dim_filme](../Desafio/csvs%20tabelas/dim_filme.csv)

[dim_produtora](../Desafio/csvs%20tabelas/dim_produtora.csv)

[dim_diretor](../Desafio/csvs%20tabelas/dim_diretor.csv)

[dim_genero](../Desafio/csvs%20tabelas/dim_genero.csv)

[fato_filme](../Desafio/csvs%20tabelas/fato_filme.csv)

Aqui está o arquivo PY com o código que usei no Glue 

[arquivopy](../Desafio/codigo%20glue/jobdesafio.py)

Meu diagrama dimensional ficou assim 

[dimensional](../Desafio/dimensional/dimensionlfinal.png)

[dimensional](../Desafio/dimensional/dimensionaldesafio.mwb)





