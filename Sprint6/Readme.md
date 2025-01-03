# Relatório da Sprint 6

## Introdução
Nesta Sprint, fomos introduzidos a vários serviços da AWS, incluindo Glue, Lambda e Athena. Também iniciamos o desafio final do programa de bolsas. 

Segue um breve resumo de cada curso realizado e as evidências dos exercícios concluídos.

---

## Resumo dos Cursos

### Noções Básicas de Analytics na AWS – Parte 1
- Conceitos fundamentais, como os tipos de análise de dados e os 5 Vs do Big Data.
- Desafios no processamento de grandes volumes de informações.
- Alinhamento dos serviços de analytics da AWS com os 5 Vs do Big Data.
- Destaque para a solução abrangente de análise da AWS.

### Fundamentos de Analytics na AWS – Parte 2
- Visão geral sobre data lakes, data warehouses e arquiteturas modernas na AWS.
- Apresentação dos principais serviços utilizados para criar esses ambientes.
- Casos de uso comuns e arquitetura de referência.
- Compreensão detalhada das soluções AWS para data lakes e data warehouses.

### Serverless Analytics
- Integração de fontes de dados usando ferramentas como AWS IoT Analytics, Amazon Cognito, AWS Lambda e Amazon SageMaker.
- Abordagem para agregar, processar, armazenar e disponibilizar dados de maneira eficiente.
- Transformar dados brutos em informações úteis.

### Introduction to Amazon Athena
- Introdução ao Amazon Athena, com visão geral do ambiente operacional e funcionalidades.
- Etapas para implementar o serviço com demonstração prática no Console da AWS.

### AWS Glue Getting Started
- Serviço de integração de dados sem servidor para análise, aprendizado de máquina e desenvolvimento de aplicações.
- Benefícios, casos de uso e conceitos técnicos.
- Uso do AWS Glue Studio e AWS Glue DataBrew para limpar e normalizar dados.

### Amazon EMR Getting Started
- Introdução ao Amazon EMR Serverless, que permite execução eficiente de aplicativos de big data.
- Benefícios, casos de uso e conceitos técnicos do Amazon EMR.

### Getting Started with Amazon Redshift
- Benefícios, casos de uso e conceitos técnicos do Amazon Redshift.
- Integração com data lakes no Amazon S3 e bancos de dados relacionais.
- Uso de modelos de machine learning (ML) com comandos SQL familiares.

### Best Practices for Data Warehousing with Amazon Redshift
- Implementação de data warehouse com Amazon Redshift.
- Design básico de tabelas, ingestão de dados e gerenciamento de workload.
- Impacto do dimensionamento de nós e clusters.

### Amazon QuickSight – Getting Started
- Benefícios e conceitos técnicos do Amazon QuickSight.
- Serviço de BI em nuvem para criação de painéis interativos.
- Integração de dados de diversas fontes com ferramentas de gerenciamento de usuários.

---

## Evidências dos Exercícios Concluídos

### Laboratórios
- **Athena**: Execução prática de consultas e manipulação de dados.

Criando DataBase
![athena1](../Sprint6/Exercicios/Athena/evidencias/consulta1.png)

![athena2](../Sprint6/Exercicios/Athena/evidencias/consulta1resultado.png)

Criando Tabela

![athena3](../Sprint6/Exercicios/Athena/evidencias/consulta2.png)

![athena4](../Sprint6/Exercicios/Athena/evidencias/consulta2resultado.png)

Testando os dados

![athena5](../Sprint6/Exercicios/Athena/evidencias/consulta3.png)

![athena6](../Sprint6/Exercicios/Athena/evidencias/consulta3resultado.png)

![athena7](../Sprint6/Exercicios/Athena/evidencias/consulta3resultado%20(2).png)

Criando uma consulta que lista os 3 nomes mais usados em cada década desde o 1950 até hoje

![athena8](../Sprint6/Exercicios/Athena/evidencias/consulta4.png)

![athena9](../Sprint6/Exercicios/Athena/evidencias/consulta4resultado.png)

O resultado Final do Bucket ficou dessa maneira

![athena10](../Sprint6/Exercicios/Athena/evidencias/bucket.png)

Aqui estão os codigos e arquivos gerados

consulta1:

[codigoconsulta1](../Sprint6/Exercicios/Athena/codigos%20e%20arquivos%20gerados/codigoconsulta1.txt)

Consulta2

[codigoconsulta2](../Sprint6/Exercicios/Athena/codigos%20e%20arquivos%20gerados/codigoconsulta2.txt)

Consulta3

[codigoconsulta3](../Sprint6/Exercicios/Athena/codigos%20e%20arquivos%20gerados/codigoconsulta3.txt)

[arquivogerado](../Sprint6/Exercicios/Athena/codigos%20e%20arquivos%20gerados/resultadoconsulta3.csv)

Consulta4

[codigoconsulta4](../Sprint6/Exercicios/Athena/codigos%20e%20arquivos%20gerados/codigoconsulta4.txt)

[arquivogerado](../Sprint6/Exercicios/Athena/codigos%20e%20arquivos%20gerados/resultadoconsulta4.csv)

- **Lambda**: Implementação de funções para processar dados em eventos.

Criando Funçao

![Lambda1](../Sprint6/Exercicios/Lambda/evidencias/lambda01.png)

Construindo o codigo

![Lambda2](../Sprint6/Exercicios/Lambda/evidencias/lambda02.png)

Criando Layer

![Lambda3](../Sprint6/Exercicios/Lambda/evidencias/lambda03.png)

Criando imagem no docker

![Lambda4](../Sprint6/Exercicios/Lambda/evidencias/lambda04.png)

![Lambda5](../Sprint6/Exercicios/Lambda/evidencias/lambda05.png)

Acessando a Shell

![Lambda6](../Sprint6/Exercicios/Lambda/evidencias/lambda06.png)

![Lambda7](../Sprint6/Exercicios/Lambda/evidencias/lambda07.png)

Copiando o zip do Container para a máquina local

![Lambda8](../Sprint6/Exercicios/Lambda/evidencias/lambda08.png)

![Lambda9](../Sprint6/Exercicios/Lambda/evidencias/lambda09.png)

Fazendo Upload para S3

![Lambda10](../Sprint6/Exercicios/Lambda/evidencias/lambda10.png)

![Lambda11](../Sprint6/Exercicios/Lambda/evidencias/lambda11.png)

Criando Layer

![Lambda12](../Sprint6/Exercicios/Lambda/evidencias/lambda12.png)

Utilizando a Layer

![Lambda13](../Sprint6/Exercicios/Lambda/evidencias/lambda13.png)

![Lambda14](../Sprint6/Exercicios/Lambda/evidencias/lambda14.png)

![Lambda15](../Sprint6/Exercicios/Lambda/evidencias/lambda15.png)

![Lambda16](../Sprint6/Exercicios/Lambda/evidencias/lambda16.png)

Aqui esta o arquivo Dockerfile e a camada pandas zipada

[Lambda17](../Sprint6/Exercicios/Lambda/arquivos%20gerados/Dockerfile)

[Lambda18](../Sprint6/Exercicios/Lambda/arquivos%20gerados/minha-camada-pandas.zip)

---

## Certificados

Os certificados gerados nesta Sprint estão anexados como evidência de conclusão dos cursos e laboratórios realizados.

[analytics1](../Sprint6/Certificados/(analytics1)AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)

[analytics2](../Sprint6/Certificados/(analytics2)AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)

[athena](../Sprint6/Certificados/(athena)AWS%20Course%20Completion%20Certificate.pdf)

[data warehousing](../Sprint6/Certificados/(boaspraticasredshift)_AWS%20Course%20Completion%20Certificate.pdf)

[emr](../Sprint6/Certificados/(emr)AWS%20Skill%20Builder%20Course%20Completion%20Certificate.pdf)

[glue](../Sprint6/Certificados/(glue)AWS%20Course%20Completion%20Certificate.pdf)

[anquicksight](../Sprint6/Certificados/(quicksight)AWS%20Course%20Completion%20Certificate.pdf)

[redshift](../Sprint6/Certificados//(redshift)AWS%20Course%20Completion%20Certificate.pdf)

[servless](../Sprint6/Certificados/(serverless%20analytics)AWS%20Course%20Completion%20Certificate.pdf)
