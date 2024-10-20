import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.tree import DecisionTreeClassifier, plot_tree

clf = DecisionTreeClassifier(random_state=0)
# Conjunto artificial de dados feito através do make classfication. Faz conjuntos artificiais para classificação.
X, y = make_classification(n_samples=100, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify =y, random_state=1)
clf.fit(X_train, y_train)

print('Prediction: ', clf.predict(X_test[:5, :]))
print('Model Accuracy: ', clf.score(X_test, y_test))
print('Detailed Prediction: ', cross_val_score(clf, X_train, y_train, cv=10))


plot_tree(clf)
plt.show()