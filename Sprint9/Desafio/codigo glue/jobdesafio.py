import sys
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import col, split, explode, trim, monotonically_increasing_id, when, row_number, lit, collect_list, array, first, concat_ws
from pyspark.sql.window import Window
from pyspark.sql import functions as F
from pyspark.sql.functions import collect_list, first
from pyspark.sql.functions import collect_set, first, col

args = getResolvedOptions(sys.argv, ['JOB_NAME'])

sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# caminho de origem dos arquivos no bucket
s3_path_local = "s3://desafiofinal-filmeseseries/trusted/local/parquet/movies/"
s3_path_tmdb = "s3://desafiofinal-filmeseseries/trusted/tmdb/parquet/movies/2025/01/20/"

# carregando os arquivos parquet
df_local = spark.read.parquet(s3_path_local)
df_tmdb = spark.read.parquet(s3_path_tmdb)

# join entre as duas fontes de dados usando o imdb_id
df_joined = df_tmdb.join(df_local, df_tmdb["imdb_id"] == df_local["id"], "inner") \
    .select(
        df_tmdb["id"].alias("id_tmdb"),
        df_tmdb["imdb_id"],
        df_local["titulooriginal"].alias("titulo"),
        df_local["anolancamento"].alias("ano_lancamento"),
        df_local["genero"],
        df_local["notamedia"].alias("nota_media"),
        df_tmdb["production_companies"].alias("produtoras"),
        df_tmdb["popularity"].alias("popularidade_tmdb"),
        df_tmdb["revenue"].alias("receita"),
        df_tmdb["budget"].alias("orcamento"),
        df_tmdb["director"].alias("diretor"),
        df_tmdb["department"].alias("departamento"),
        df_tmdb["keywords"].alias("palavras_chave")  
    )

# filtrando as linhas onde receita e orcamento são diferentes de zero
df_filtered = df_joined.filter((col("receita") != 0) & (col("orcamento") != 0))

# adicionando coluna lucro_liquido após a filtragem
df_with_lucro = df_filtered.withColumn(
    "lucro_liquido", 
    when((col("receita").isNull()) | (col("orcamento").isNull()) | (col("orcamento") == 0), lit(None))
    .otherwise(col("receita") - col("orcamento"))
)

# adicionando coluna de row_number para particionar pelo imdb_id
window_spec = Window.partitionBy("imdb_id").orderBy("id_tmdb")
df_with_row_number = df_with_lucro.withColumn("rn", row_number().over(window_spec))

# filtrando os dados onde row_number = 1 e lucro_liquido não é nulo
df_filtered = df_with_row_number.filter((col("rn") == 1) & (col("lucro_liquido").isNotNull()))

# criaando  tabela de anos com a coluna decada
df_anos_distintos = df_filtered.select("ano_lancamento").distinct() \
    .withColumn("decada", (col("ano_lancamento") - (col("ano_lancamento") % 10)).cast("int"))

# criar um id único para a tabela dim_tempo
window_spec = Window.orderBy("ano_lancamento")
df_anos_distintos = df_anos_distintos.withColumn("id_ano", row_number().over(window_spec))

# criar a tabela de dim_filme 
df_filme = df_filtered.withColumn(
    "palavras_chave", when(col("palavras_chave").isNotNull(), concat_ws(", ", col("palavras_chave"))).otherwise(lit(""))
).select(
    "id_tmdb",
    "titulo",
    "ano_lancamento",
    "palavras_chave"
).distinct()

# explodindo colunas multivaloradas
df_exploded = df_filtered.withColumn("genero", explode(split(col("genero"), ","))) \
                         .withColumn("produtoras", explode(split(col("produtoras"), ",")))

# criando tabelas de dimensão para produtoras/generos/diretores/departamentos
def process_column(df, column_name, id_column_name):
    df_exploded = df.withColumn(column_name, explode(split(col(column_name), ",")))
    df_exploded = df_exploded.withColumn(column_name, trim(col(column_name)))
    df_distinct = df_exploded.select(column_name).distinct().filter(col(column_name).isNotNull())
    window_spec = Window.orderBy(column_name)
    df_distinct = df_distinct.withColumn(id_column_name, F.row_number().over(window_spec))
    return df_distinct

df_produtoras_distintas = process_column(df_filtered, "produtoras", "id_produtoras")
df_generos_distintos = process_column(df_filtered, "genero", "id_genero")
df_diretores_distintos = process_column(df_filtered, "diretor", "id_diretor")
df_departamentos_distintos = process_column(df_filtered, "departamento", "id_departamento")

# join com as tabelas de dimensão
df_fato_prep = df_exploded \
    .join(df_produtoras_distintas, on="produtoras", how="left") \
    .join(df_generos_distintos, on="genero", how="left") \
    .join(df_diretores_distintos, on="diretor", how="left") \
    .join(df_departamentos_distintos, on="departamento", how="left") \
    .join(df_anos_distintos, on="ano_lancamento", how="left")

from pyspark.sql.functions import collect_list, first

# agrupando por imdb_id e agregando colunas multivaloradas
df_fato = df_fato_prep.groupBy("imdb_id", "id_tmdb", "id_diretor", "id_departamento", "id_ano") \
    .agg(
        collect_set("id_produtoras").alias("id_produtoras"),  # collect_set para remover duplicatas, em genero e produtoras
        collect_set("id_genero").alias("id_genero"),  
        first("popularidade_tmdb").alias("popularidade_tmdb"),
        first("receita").alias("receita"),
        first("orcamento").alias("orcamento"),
        first("lucro_liquido").alias("lucro_liquido"),
        first("nota_media").alias("nota_media")
    )

# salvando as dimensoes
df_produtoras_distintas.write.format("parquet").mode("overwrite").save("s3://desafiofinal-filmeseseries/refined/dim_produtora")
df_generos_distintos.write.format("parquet").mode("overwrite").save("s3://desafiofinal-filmeseseries/refined/dim_genero")
df_diretores_distintos.write.format("parquet").mode("overwrite").save("s3://desafiofinal-filmeseseries/refined/dim_diretor")
df_departamentos_distintos.write.format("parquet").mode("overwrite").save("s3://desafiofinal-filmeseseries/refined/dim_departamento")
df_anos_distintos.write.format("parquet").mode("overwrite").save("s3://desafiofinal-filmeseseries/refined/dim_tempo")
df_filme.write.format("parquet").mode("overwrite").save("s3://desafiofinal-filmeseseries/refined/dim_filme")

df_fato.write.format("parquet") \
    .option("compression", "snappy") \
    .mode("overwrite") \
    .save("s3://desafiofinal-filmeseseries/refined/fato_filme/")

job.commit()
