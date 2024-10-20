import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.datasets import make_classification

from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC

clf = make_pipeline(StandardScaler(), SVC(gamma='auto'))
# Conjunto artificial de dados feito através do make classfication. Faz conjuntos artificiais para classificação.
X, y = make_classification(n_samples=100, random_state=1)
X_train, X_test, y_train, y_test = train_test_split(X, y, stratify =y, random_state=1)
clf.fit(X_train, y_train)

tdf = pd.DataFrame(X_train)
tdf['target'] = y_train
tdf['target'] = tdf['target'].astype('str')
print(tdf.head())

print('Prediction: ', clf.predict(X_test[:5, :]))
print('Model Accuracy: ', clf.score(X_test, y_test))