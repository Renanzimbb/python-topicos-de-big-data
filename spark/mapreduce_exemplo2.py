import numpy as np
from pyspark import SparkContext

spark_contexto = SparkContext()
vetor = np.array([10, 20, 30, 40, 50])

#Agora vamos criar um RDD por meio de um SparkContext com o seguinte código:
paralelo = spark_contexto.parallelize(vetor)

# map() É usada para aplicar a transformação em cada elemento de uma fonte de dados e retorna um novo conjunto de dados.
# Os dados podem ser RDD, DataFrame ou Dataset.
mapa = paralelo.map(lambda x: x**2+x)

# Retorna os elementos do conjunto de dados como um vetor.
mapa.collect()

from operator import add

# reduce() Faz a agregação dos elementos de um conjunto de dados por meio de funções.
somatorio = mapa.reduce(add)
print(somatorio)