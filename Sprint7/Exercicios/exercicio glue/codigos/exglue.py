import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import upper  # função upper para transformar em maiusculas

args = getResolvedOptions(sys.argv, ['JOB_NAME',"S3_INPUT_PATH","S3_TARGET_PATH"])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

source_file = args["S3_INPUT_PATH"]
target_path = args["S3_TARGET_PATH"]

# Ler o arquivo CSV do S3
datasource = glueContext.create_dynamic_frame.from_options(
    "s3",
    {
        "paths":[source_file]
    },
    "csv",
    {"withHeader":True, "separator": ","},
)

# Convertendo DynamicFrame para DataFrame
df = datasource.toDF()

# Exibir o schema
print("Schema do DataFrame:")
df.printSchema()

# Coluna nome para maiúsculo
df = df.withColumn('nome', upper(df['nome']))
print("Schema do DataFrame após a transformação:")
df.printSchema()

# Contar o número de linhas
linha_count = df.count()
print(f"Contagem de linhas no DataFrame: {linha_count}")

# Contagem de nomes, agrupando por ano e sexo e ordenando por ano
grouped_df = df.groupBy('ano', 'sexo').count()
# Ordenar os resultados por ano de forma decrescente 
grouped_df_sorted = grouped_df.orderBy('ano', ascending=False)
# Exibir os resultados
print("Contagem de nomes agrupada por 'ano' e 'sexo' (ordenada por ano mais recente):")
grouped_df_sorted.show()

# Filtro considerando apenas sexo F
df_feminino = df.filter(df['sexo'] == 'F')  
# Agrupar por nome e ano, contando as ocorrencias
grouped_df_feminino = df_feminino.groupBy('nome', 'ano').count()
# Ordenar os resultados pela contagem para pegar o nome mais frequente
sorted_grouped_df_feminino = grouped_df_feminino.orderBy('count', ascending=False)
# Selecionar o nome feminino com mais registros
top_nome_feminino = sorted_grouped_df_feminino.first()
# Exibir o nome feminino com mais registros e o ano que ocorreu
print(f"Nome feminino com mais registros: {top_nome_feminino['nome']}")
print(f"Ano em que ocorreu: {top_nome_feminino['ano']}")
print(f"Contagem de registros: {top_nome_feminino['count']}")

# Filtro considerando apenas sexo M
df_masculino = df.filter(df['sexo'] == 'M') 
# Agrupar por nome e ano, contando as ocorrencias
grouped_df_masculino = df_masculino.groupBy('nome', 'ano').count()
# Ordenar os resultados pela contagem  para pegar o nome mais frequente
sorted_grouped_df_masculino = grouped_df_masculino.orderBy('count', ascending=False)
# Selecionar o nome masculino com mais registros
top_nome_masculino = sorted_grouped_df_masculino.first()
# Exibir o nome masculino com mais registros e o ano que ocorreu
print(f"Nome masculino com mais registros: {top_nome_masculino['nome']}")
print(f"Ano em que ocorreu: {top_nome_masculino['ano']}")
print(f"Contagem de registros: {top_nome_masculino['count']}")

# Agrupar por ano e contar as ocorrencias
grouped_by_year = df.groupBy('ano').count()
# Ordenar por ano de forma crescente
sorted_by_year = grouped_by_year.orderBy('ano', ascending=True)
# Exibir as primeiras 10 linhas
print("Total de registros para cada ano (top 10 ordenado por ano):")
sorted_by_year.show(10)

# Gravar no S3 com particionamento pelas colunas sexo e ano
df.write \
    .mode("overwrite") \
    .partitionBy('sexo', 'ano') \
    .json(target_path)

job.commit()
