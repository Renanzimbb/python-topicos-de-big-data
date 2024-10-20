import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score
from sklearn.tree import DecisionTreeClassifier, plot_tree


clf = DecisionTreeClassifier(max_depth=3, random_state=0)
iris = load_iris()

# A validação cruzada é um dos modos mais comuns de se treinar nossos modelos, pois ela divide o conjunto de dados
# em (k-1)/k partições de treinamento e 1/k de teste de maneira circular e interativa, tendo assim todas as 1/k
# possíveis partições, podendo ser testadas contra o resto.
cross_val_score(clf, iris.data, iris.target, cv=10)

clf.fit(iris.data, iris.target)
plot_tree(clf, filled=True)
plt.show()