from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from sklearn import tree
import pandas as pd
import matplotlib.pyplot as plt

PLOT_BASE_PATH = 'plots'

iris = load_iris()
iris.target[[10, 25, 50]]

X, y = load_iris(return_X_y=True)

iris_df = pd.DataFrame(
  data = iris.data,
  columns = iris.feature_names
)

iris_df.dtypes
# Test_size as percentage. To be more easier to read.
# Seed to generate same dataset
dataset_test_percent = 33.3
random_seed = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=dataset_test_percent*(10**-2), random_state=random_seed)

dtree = DecisionTreeClassifier(criterion='entropy', max_depth=4, splitter='best')
dtree.fit(X_train, y_train)

y_pred_train = dtree.predict(X_train)
y_pred_test = dtree.predict(X_test)

scikit_score_train = dtree.score(X_test, y_test)
scikit_score_test = dtree.score(X_train, y_train)

cm = confusion_matrix(y_test, y_pred_test, labels= dtree.classes_)

disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=iris.target_names)
disp.plot().figure_.savefig(f'{PLOT_BASE_PATH}/decision_tree_confusion_matrix.png',dpi=300)

plt.figure(figsize=(20,15))
tree.plot_tree(dtree, fontsize=10)
plt.savefig(f'{PLOT_BASE_PATH}/decision_tree', dpi=300)