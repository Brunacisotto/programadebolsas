import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# caminhos dos dados
raw_path = "s3://desafiofinal-filmeseseries/raw/local/csv/movies/2024/12/31/movies.csv"
trusted_path = "s3://desafiofinal-filmeseseries/trusted/local/parquet/movies/"

# lendo os dados do CSV da camada raw
raw_df = spark.read.format("csv") \
    .option("header", "true") \
    .option("inferSchema", "true") \
    .option("sep", "|") \
    .load(raw_path)

# removendo colunas que não usarei na analise
colunas_para_remover = [
    "tempoMinutos",
    "generoArtista",
    "personagem",
    "nomeArtista",
    "anoNascimento",
    "anoFalecimento",
    "profissao",
    "titulosMaisConhecidos"
]
tratado_df = raw_df.drop(*colunas_para_remover)

# removendo linhas duplicatas 
tratado_df = tratado_df.dropDuplicates()

# removendo de valores nulos
tratado_df = tratado_df.na.drop()

# convertendo a coluna anoLancamento para inteiro
tratado_df = tratado_df.withColumn("anoLancamento", col("anoLancamento").cast("int"))

# filtrando apenas os filmes lançados a partir de 1960 (stephen king nasceu em 1947)
tratado_df = tratado_df.filter(col("anoLancamento") >= 1960)

# escrevendo os dados transformados na camada trusted no formato parquet
tratado_df.write.format("parquet") \
    .mode("overwrite") \
    .save(trusted_path)

job.commit()
