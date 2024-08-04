from pyspark.sql import SparkSession
from pyspark.sql.functions import countDistinct
from pyspark.sql.functions import col

spark = SparkSession \
    .builder \
    .master("spark://192.168.1.110:7077") \
    .appName("myApp2") \
    .config("spark.jars.packages", "org.mongodb.spark:mongo-spark-connector_2.12:3.0.1") \
    .getOrCreate()

df1 = spark.read.csv("./data.csv", header=True)
df1.printSchema()
#df.show()

# dataframe with clean records only
dfc = df1.where(col('HPCP')!=999.99)
#dfc.where(col('HPCP')==999.99).show()


dfc.write.format("mongo").option("uri", "mongodb://127.0.0.1/precp.hpcp").mode("append").save()

df_station_counts = dfc.groupBy('STATION_NAME').count()
df_station_counts.write.format("mongo").option("uri", "mongodb://127.0.0.1/precp.stncnt").mode("append").save()
df2 = spark.read.format('mongo').option('uri','mongodb://127.0.0.1/precp.stncnt').load()
df2.show(57, truncate=False)

