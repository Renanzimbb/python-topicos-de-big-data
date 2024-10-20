from pyspark import SparkContext
#Para executar em um cluster, o SparkContext se conecta ao gerenciador de cluster e, em seguida, efetua as seguintes tarefas:
#Adquire executores em nós do cluster.
#Envia o código da aplicação para os executores, o qual pode ser definido por arquivos JAR ou Python passados para o SparkContext.
#SparkContext envia tarefas para que sejam processadas pelos executores.


spark_contexto = SparkContext()

lista = [1, 2, 3, 4, 5, 3]
lista_rdd = spark_contexto.parallelize((lista))
lista_rdd.count()

par_ordenado = lambda numero: (numero, numero*10)

# flatMap() Faz o nivelamento das colunas do conjunto de dados resultante depois de aplicar a
# função em cada elemento e retorna um novo conjunto de dados.
lista_rdd.flatMap(par_ordenado).collect()

#Para concluir, precisamos fechar a seção com o código abaixo:
spark_contexto.stop()