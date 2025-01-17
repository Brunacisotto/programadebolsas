# Sprint 7

Nesta sprint, fomos introduzidos ao Apache Spark, utilizamos a API do TMDb para a segunda parte do desafio final e trabalhamos com o AWS Glue em uma atividade prática. A seguir, apresento um resumo das atividades realizadas:

## Curso de Formação com PySpark

No curso que fiz sobre Apache Spark, aprendi do zero como usar essa ferramenta essencial para o mundo do "Big Data". O Spark se destaca pela capacidade de processar grandes volumes de dados de forma rápida e eficiente, graças à sua arquitetura distribuída, que utiliza paralelismo e memória. Descobri que ele permite importar dados de diversas fontes, exportar resultados para os formatos mais usados e até criar modelos de Machine Learning com suas bibliotecas integradas.

O curso foi fundamental para ampliar minha compreensão sobre processamento de dados distribuídos e integração com Python através do PySpark.

---

## Exercício com a API do TMDb
Neste exercício, trabalhamos com um modelo de requisição à API do TMDb, praticando a interação com endpoints e manipulação de dados retornados. 

- **Documentação Gerada:** Disponibilizo o código implementado e o relatório produzido durante o exercício.

[arquivopytmdb](../Sprint7/Exercicios/exercicio%20tmdb/extmdb.py)

[arquivogerado](../Sprint7/Exercicios/exercicio%20tmdb/filmes_top_rated.csv)

---

## Exercício com AWS Glue
Recebemos um modelo passo a passo para criar um job no Glue. Posteriormente, desenvolvemos um código personalizado para processar informações sobre os nomes mais comuns em cada ano nos EUA.

- **Evidências:** Incluo os arquivos gerados durante a execução do exercício, o código implementado e os resultados obtidos.

### Executando passo a passo o modelo fornecido

![gluemodelo](../Sprint7/Exercicios/exercicio%20glue/glue01.png)

![gluemodelo2](../Sprint7/Exercicios/exercicio%20glue/glue02.png)

![gluemodelo3](../Sprint7/Exercicios/exercicio%20glue/glue03.png)

![gluemodelo4](../Sprint7/Exercicios/exercicio%20glue/glue04.png)

![gluemodelo5](../Sprint7/Exercicios/exercicio%20glue/glue05.png)

![gluemodelo6](../Sprint7/Exercicios/exercicio%20glue/glue06.png)

![gluemodelo7](../Sprint7/Exercicios/exercicio%20glue/glue07.png)

![gluemodelo8](../Sprint7/Exercicios/exercicio%20glue/glue08.png)

![gluemodelo9](../Sprint7/Exercicios/exercicio%20glue/glue09.png)

![gluemodelo10](../Sprint7/Exercicios/exercicio%20glue/glue10.png)

![gluemodelo11](../Sprint7/Exercicios/exercicio%20glue/glue11.png)

![gluemodelo12](../Sprint7/Exercicios/exercicio%20glue/glue12.png)

![gluemodelo13](../Sprint7/Exercicios/exercicio%20glue/glue13.png)

![gluemodelo14](../Sprint7/Exercicios/exercicio%20glue/glue14.png)

![gluemodelo15](../Sprint7/Exercicios/exercicio%20glue/glue15.png)

![gluemodelo16](../Sprint7/Exercicios/exercicio%20glue/glue16.png)

![gluemodelo17](../Sprint7/Exercicios/exercicio%20glue/glue17.png)

![gluemodelo18](../Sprint7/Exercicios/exercicio%20glue/glue18.png)

![gluemodelo19](../Sprint7/Exercicios/exercicio%20glue/glue19.png)

![gluemodelo20](../Sprint7/Exercicios/exercicio%20glue/glue20.png)

Resultado no Bucket

![gluemodelo21](../Sprint7/Exercicios/exercicio%20glue/glue21.png)

Configurações para frequencia de nomes 

![glue01](../Sprint7/Exercicios/exercicio%20glue/glue22.png)

![glue02](../Sprint7/Exercicios/exercicio%20glue/glue23.png)

![glue03](../Sprint7/Exercicios/exercicio%20glue/glue24.png)

![glue04](../Sprint7/Exercicios/exercicio%20glue/glue25.png)

![glue05](../Sprint7/Exercicios/exercicio%20glue/glue26.png)

![glue06](../Sprint7/Exercicios/exercicio%20glue/glue27.png)

![glue07](../Sprint7/Exercicios/exercicio%20glue/glue28.png)

Athena 

![glue08](../Sprint7/Exercicios/exercicio%20glue/glue29.png)

Resultado Athena 

![glue09](../Sprint7/Exercicios/exercicio%20glue/glue30.png)

Resultado Glue no bucket

![glue10](../Sprint7/Exercicios/exercicio%20glue/glue31.png)

![glue11](../Sprint7/Exercicios/exercicio%20glue/glue32.png)

### Arquivos e códigos gerados

#### Modelo 

[gluemodelocodigo](../Sprint7/Exercicios/exercicio%20glue/codigos/job_aws_glue_lab_4.py)

[arquivogeradomodelo](../Sprint7/Exercicios/exercicio%20glue/arquivos/part-00000-05d91e13-499c-4d99-8a8a-40eafcd22793-c000.snappy.parquet)

#### Meu código

[gluemeucodigo](../Sprint7/Exercicios/exercicio%20glue/codigos/exglue.py)

[arquivosgerados](../Sprint7/Exercicios/exercicio%20glue/arquivos/1b413f4c-92a2-4c66-9495-4e89978551dd.csv)

[arquivosgerados2](../Sprint7/Exercicios/exercicio%20glue/arquivos/91a3d5fe-9d4b-4adf-80cd-4b1ddde2e966.csv)


---

## Exercício com Spark
Concluí um exercício prático utilizando Spark, no qual implementei um contador de palavras aplicado ao arquivo `README`. 

- **Resultados:** Disponibilizo as evidências da execução e o arquivo de saída gerado.

![exerciciospark](../Sprint7/Exercicios/execicio%20docker/docker01.png)

![exerciciospark2](../Sprint7/Exercicios/execicio%20docker/docker02.png)

![exerciciospark3](../Sprint7/Exercicios/execicio%20docker/docker03.png)

![exerciciospark4](../Sprint7/Exercicios/execicio%20docker/docker04.png)

![exerciciospark5](../Sprint7/Exercicios/execicio%20docker/docker05.png)

![exerciciospark6](../Sprint7/Exercicios/execicio%20docker/docker06.png)

![exerciciospark7](../Sprint7/Exercicios/execicio%20docker/docker07.png)

![exerciciospark8](../Sprint7/Exercicios/execicio%20docker/docker08.png)

![exerciciospark9](../Sprint7/Exercicios/execicio%20docker/docker09.png)

[arquivocontadordepalavras](../Sprint7/Exercicios/execicio%20docker/contadordepalavras.txt)
---

## Certificados
Nesta sprint, não foram realizados cursos externos á Udemy, e, portanto, não houve emissão de certificados.

---
