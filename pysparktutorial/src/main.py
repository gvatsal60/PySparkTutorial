from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .master('local[*]') \
    .appName('SparkApp') \
    .getOrCreate()

df = spark.createDataFrame([[1], [2], [3], [4], [5]])

print(df.count())

df.show()
