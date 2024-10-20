# Tema 2

from mrjob.job import MRJob
import re

# A linha de código a seguir recebe uma linha de texto como entrada e retorna uma lista de palavras sem os espaços.
palavra_regex = re.compile(r"[\w']+")

class QuantidadePalavras(MRJob):
    def mapper(self,_, linha):
        for p in palavra_regex.findall(linha):
            yield(p.lower(),1)

    def reducer(self, p, qtd):
        yield (p, sum(qtd))


if __name__ == '__main__':
    QuantidadePalavras.run()


    #Para executar o programa, devemos escrever e executar a linha de comando abaixo no terminal:

# Para executar o programa, devemos escrever e executar a linha de comando abaixo no terminal: