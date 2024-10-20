from pyspark import SparkContext
import numpy as np


spark_contexto = SparkContext()
paralelo = spark_contexto.parallelize(['distribuida', 'distribuida', 'spark', 'rdd', 'spark','spark'])
# função lambda que simplesmente associa o número “1” a uma palavra.
funcao_lambda = lambda x:(x,1)

from operator import add
#Fazemos o mapeamento dos dados da variável “paralelo” para a função lambda, ou seja, para cada palavra criamos um par (palavra, 1).
#Em seguida, aplicamos a redução com a função “reduceKey”, que soma as ocorrências e as agrupa pela chave, no caso, pelas palavras.
#Na etapa final, dada pela função “collect”, fazemos a coleta dos dados em uma lista que chamamos de “mapa”.
mapa = paralelo.map(funcao_lambda).reduceByKey(add).collect()

#Esse código percorre a lista “mapa” e imprime cada par formado pela palavra e sua respectiva ocorrência. Abaixo, apresentamos a saída:
for (w, c) in mapa:
     print('{}: {}'.format(w, c))

#Para concluir, precisamos fechar a seção com o seguinte código:
spark_contexto.stop()