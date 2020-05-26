# sklearn 随机决策树(random forest)

本章将帮助您了解Sklearn中的随机决策树。

## 随机决策树算法

众所周知，DT通常是通过递归拆分数据来训练的，但是容易过度拟合，通过对数据的各个子样本训练许多树，它们已转变为随机森林。该**sklearn.ensemble**模块具有基于随机决策树以下两种算法-

## 随机森林算法

对于考虑中的每个特征，它都会计算局部最优特征/分割组合。在随机森林中，集合中的每个决策树都是根据从训练集中替换得到的样本构建的，然后从每个样本中获取预测，最后通过投票选择最佳解决方案。它可用于分类以及回归任务。

### 随机森林分类

为了创建随机森林分类器，Scikit-learn模块提供了**sklearn.ensemble.RandomForestClassifier**。在构建随机森林分类器时，此模块使用的主要参数是**'max_features'**和**'n_estimators'**。

在这里，**“ max_features”**是分割节点时要考虑的特征随机子集的大小。如果我们将此参数的值选择为none，则它将考虑所有功能，而不是随机子集。另一方面，**n_estimators**是森林中树木的数量。树的数量越多，结果越好。但是计算也需要更长的时间。

### 实例

在以下示例中，我们将使用**sklearn.ensemble.RandomForestClassifier**构建一个随机森林分类器，并通过使用**cross_val_score**模块来检查其准确性。

```python
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import RandomForestClassifier
X, y = make_blobs(n_samples = 10000, n_features = 10, centers = 100,random_state = 0) 
RFclf = RandomForestClassifier(n_estimators = 10,max_depth = None,min_samples_split = 2, random_state = 0)
scores = cross_val_score(RFclf, X, y, cv = 5)
scores.mean()
```


### 实例

我们还可以使用sklearn数据集构建随机森林分类器。如以下示例所示，我们使用虹膜数据集。我们还将找到其准确性得分和混淆矩阵。

```python
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

path = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
headernames = ['sepal-length', 'sepal-width', 'petal-length', 'petal-width', 'Class']
dataset = pd.read_csv(path, names = headernames)
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, 4].values
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.30)
RFclf = RandomForestClassifier(n_estimators = 50)
RFclf.fit(X_train, y_train)
y_pred = RFclf.predict(X_test)
result = confusion_matrix(y_test, y_pred)
print("Confusion Matrix:")
print(result)
result1 = classification_report(y_test, y_pred)
print("Classification Report:",)
print(result1)
result2 = accuracy_score(y_test,y_pred)
print("Accuracy:",result2)
```
## 随机森林回归

为了创建随机森林回归，Scikit-learn模块提供了**sklearn.ensemble.RandomForestRegressor**。在构建随机森林回归器时，它将使用与**sklearn.ensemble.RandomForestClassifier**相同的参数。

### 实例

在以下示例中，我们将使用**sklearn.ensemble.RandomForestregressor**构建一个随机森林回归器，并且还将通过使用predict（）方法预测新值。

```python
from sklearn.ensemble import RandomForestRegressor
from sklearn.datasets import make_regression
X, y = make_regression(n_features = 10, n_informative = 2,random_state = 0, shuffle = False)
RFregr = RandomForestRegressor(max_depth = 10,random_state = 0,n_estimators = 100)
RFregr.fit(X, y)
```

拟合后，我们可以从回归模型进行预测，如下所示：

```python
print(RFregr.predict([[0, 2, 3, 0, 1, 1, 1, 1, 2, 2]]))
```


## 额外树方法

对于正在考虑的每个功能，它都会为分割选择一个随机值。使用额外的树方法的好处在于，它可以进一步减少模型的方差。使用这些方法的缺点是它会稍微增加偏差。

### 额外树法分类

为了使用Extra-tree方法创建分类器，Scikit-learn模块提供了**sklearn.ensemble.ExtraTreesClassifier**。它使用与**sklearn.ensemble.RandomForestClassifier**相同的参数。唯一的区别在于，它们在构建树木的方式（如上所述）。

### 实例

在以下示例中，我们将使用**sklearn.ensemble.ExtraTreeClassifier**构建一个随机森林分类器，并使用**cross_val_score**模块检查其准确性。

```python
from sklearn.model_selection import cross_val_score
from sklearn.datasets import make_blobs
from sklearn.ensemble import ExtraTreesClassifier
X, y = make_blobs(n_samples = 10000, n_features = 10, centers=100,random_state = 0)
ETclf = ExtraTreesClassifier(n_estimators = 10,max_depth = None,min_samples_split = 10, random_state = 0)
scores = cross_val_score(ETclf, X, y, cv = 5)
scores.mean()
```
### 实例

我们还可以使用sklearn数据集通过Extra-Tree方法构建分类器。

如以下示例所示，我们使用的是Pima-Indian数据集。

```python
from pandas import read_csv

from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.ensemble import ExtraTreesClassifier
path = r"/share/datasets/pima-indians-diabetes.csv"
data = read_csv(path)
array = data.values
X = array[:,0:8]
Y = array[:,8]
seed = 7
kfold = KFold(n_splits=10, random_state=seed)
num_trees = 150
max_features = 5
ETclf = ExtraTreesClassifier(n_estimators=num_trees, max_features=max_features)
results = cross_val_score(ETclf, X, Y, cv=kfold)
print(results.mean())
```
### 额外树法回归

为了创建**Extra-Tree**回归，Scikit-learn模块提供了**sklearn.ensemble.ExtraTreesRegressor**。在构建随机森林回归器时，它将使用与**sklearn.ensemble.ExtraTreesClassifier**相同的参数。

### 实例

在下面的示例中，我们将**sklearn.ensemble.ExtraTreesregressor**应用于创建随机森林回归器时所使用的相同数据。让我们看看输出的区别

```python
from sklearn.ensemble import ExtraTreesRegressor
from sklearn.datasets import make_regression
X, y = make_regression(n_features = 10, n_informative = 2,random_state = 0, shuffle = False)
ETregr = ExtraTreesRegressor(max_depth = 10,random_state = 0,n_estimators = 100)
ETregr.fit(X, y)
```

拟合后，我们可以从回归模型进行预测，如下所示：

```python
print(ETregr.predict([[0, 2, 3, 0, 1, 1, 1, 1, 2, 2]]))
```