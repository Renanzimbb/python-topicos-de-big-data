from pyspark.sql import SparkSession
spark = SparkSession.builder.getOrCreate() # Create my_spark
dataset = spark.read.csv('california_housing_test.csv',inferSchema=True, header =True)
print(dataset.count())

dataset.createOrReplaceTempView('tabela_temporaria')
print(spark.catalog.listTables())

query = 'FROM tabela_temporaria SELECT longitude, latitude LIMIT 3'
saida = spark.sql(query)
saida.show()
