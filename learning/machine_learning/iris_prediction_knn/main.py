from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report, confusion_matrix
import plotly.express as px

df = px.data.iris()
fig = px.scatter_3d(df, x='sepal_length', y='sepal_width', z='petal_width', color='species')
# fig.show()

PLOT_BASE_PATH = 'plots'

iris = load_iris()

X, y = load_iris(return_X_y=True)

# Test_size as percentage. To be more easier to read.
# Seed to generate same dataset
dataset_test_percent = 30
random_seed = 13

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=dataset_test_percent*(10**-2), random_state=random_seed)

# Number os neighbors to analyse
n_neighbors = 9
clf = KNeighborsClassifier(n_neighbors=n_neighbors)

clf.fit(X_train, y_train)

y_pred = clf.predict(X_test)

print(classification_report(y_test, y_pred, target_names= iris.target_names))

confusion_matrix(y_test, y_pred)