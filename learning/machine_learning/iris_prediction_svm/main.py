from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn import svm

import pandas as pd
import matplotlib
import seaborn as sns

PLOT_BASE_PATH = 'plots'

iris = load_iris()
iris.target[[10, 25, 50]]

# X = Data. 
# y = Target.

X, y = load_iris(return_X_y=True)

iris_df = pd.DataFrame(
  data = iris.data,
  columns = iris.feature_names
)

iris_df['target'] = iris.target
iris_df['species'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# iris_df.head()
# As we are running on container, to avoid harder configurations to plot at display, i'm plotting at file
iris_scatter = iris_df.plot.scatter('sepal length (cm)', 'sepal width (cm)', c='target')
iris_scatter.get_figure().savefig(f'{PLOT_BASE_PATH}/iris_scatter_1.png')

# Test_size as percentage. To be more easier to read.
# Seed to generate same dataset
dataset_test_percent = 30
random_seed = 3

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=dataset_test_percent*(10**-2), random_state=random_seed)

# Getting the pairplot to figure out the relations between features
# iris_pairs = sns.pairplot(
#   data = iris_df[['sepal length (cm)', 'sepal width (cm)', 'petal length (cm)', 'petal width (cm)', 'species']],
#   hue='species'
# )
# iris_pairs.get_figure()
# iris_pairs.savefig(f"{PLOT_BASE_PATH}/iris_pair_1.png") 


# Model usage and results
C = 1.0  # SVM regularization parameter
clf = svm.SVC(kernel='linear', C=C)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test) 
scikit_score = clf.score(X_test, y_test)

# Don't use this never loL. Only for didatic learning
# Getting the index of relational X and Y of test and train, respectively
results_pairs = []
for source_index, source_vector in enumerate(X):
  for test_index, test_vector in enumerate(X_test):
    if((test_vector == source_vector).all()):
      results_pairs.append([y[source_index], y_pred[test_index]])

success = 0
size = len(X_test)
for rp in results_pairs:
  if(rp[0]==rp[1]):
    success+=1

manual_score = success/size

# Yeah, i found! I just used the wrong variable loL
print(f"Scikit Score: {scikit_score}\nManual Score: {manual_score}")
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred, target_names=iris.target_names))