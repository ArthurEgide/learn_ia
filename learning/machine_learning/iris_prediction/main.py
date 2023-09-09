from sklearn.datasets import load_iris
import pandas as pd
import matplotlib
from sklearn.model_selection import train_test_split

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
iris_df['target_names'] = pd.Categorical.from_codes(iris.target, iris.target_names)

# iris_df.head()
# As we are running on container, to avoid harder configurations to plot at display, i'm plotting at file
iris_scatter = iris_df.plot.scatter('sepal length (cm)', 'sepal width (cm)', c='target')
iris_scatter.get_figure().savefig('plots/test1.png')

# Test_size as percentage. To be more easier to read.
dataset_test_percent = 30
# Seed to generate same dataset
random_seed = 42
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=dataset_test_percent*(10**-2), random_state=random_seed)

X_train.shape
