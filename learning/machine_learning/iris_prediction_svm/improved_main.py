from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import classification_report

import pandas as pd

PLOT_BASE_PATH = 'plots'
iris = load_iris()
X, y = load_iris(return_X_y=True)

iris_df = pd.DataFrame(
  data = iris.data,
  columns = iris.feature_names
)

iris_df['target'] = iris.target
iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

dataset_test_percent=100/4

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=dataset_test_percent*(10**-2))

# Gamma between 0.3162 and 0.0013. If i need to choose some gamma, probably been close to 0.035
min = 50  # Overfit
max = 300 # Underfit
steps = (min+max)//20

for i in range(min, max, steps):
  gamma = 10**-(i/100)
  clf = svm.SVC(kernel='rbf', gamma=gamma)
  x = clf.fit(X_train, y_train)
  y_pred = clf.predict(X_test) 
  print(f'score:{clf.score(X_test, y_test)} \tGamma: {gamma}')

print(classification_report(y_test, y_pred, target_names=iris.target_names, zero_division=False))
