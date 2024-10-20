from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification

clf = MLPClassifier(random_state=1, max_iter=300)
# Conjunto artificial de dados feito através do make classfication. Faz conjuntos artificiais para classificação.
X, y = make_classification(n_samples=100, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify =y, random_state=1)
clf.fit(X_train, y_train)


print('Detailed Prediction: ', clf.predict_proba(X_test[:1]))
print('Prediction: ', clf.predict(X_test[:5, :]))
print('Model Accuracy: ', clf.score(X_test, y_test))