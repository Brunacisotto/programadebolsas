import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import functions as F

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# definindo os caminhos como variáveis
raw_path = "s3://desafiofinal-filmeseseries/raw/tmdb/json/2025/01/20/"
trusted_path = "s3://desafiofinal-filmeseseries/trusted/tmdb/parquet/movies/2025/01/20"

# carregarando os arquivos JSON da Raw Zone
datasource0 = glueContext.create_dynamic_frame.from_options(
    connection_type="s3",
    connection_options={"paths": [raw_path]},
    format="json"
)

# convertendo DynamicFrame para DataFrame 
df = datasource0.toDF()

# transformando 'production_companies' e 'keywords' de listas para strings
df = df.withColumn(
    "production_companies", 
    F.when(F.col("production_companies").isNotNull(), F.array_join(F.col("production_companies"), ","))
    .otherwise(F.lit(""))  # se a coluna for nula, cria uma string vazia
)

df = df.withColumn(
    "keywords", 
    F.when(F.col("keywords").isNotNull(), F.array_join(F.col("keywords"), ","))
    .otherwise(F.lit(""))  # se a coluna for nula, cria uma string vazia
)

# removendo as linhas onde 'imdb_id' é null
df_total = df.dropna(subset=['imdb_id'])

# escrevendo os dados transformados na camada trusted no formato parquet
df_total.write.format("parquet") \
    .mode("overwrite") \
    .option("path", trusted_path) \
    .save()

job.commit()
