# sklearn 建模过程

本章介绍Sklearn中涉及的建模过程。让我们详细了解一下，并从数据集加载开始。

## 数据集加载

数据的集合称为数据集。它具有以下两个组成部分-

**特征** -数据的变量称为其特征。它们也称为预测变量，输入或属性。

- **特征矩阵** -如果有多个特征，它是特征的集合。
- **功能名称** -这是所有**功能名称**的列表。

**响应** -基本取决于特征变量的是输出变量。它们也称为目标，标签或输出。

- **响应向量** -用于表示响应列。通常，我们只有一个响应列。
- **目标名称** -它表示响应向量可能采用的值。

Scikit-learn几乎没有示例数据集，例如用于分类的IRIS和Digital以及用于回归的**波士顿房价**。

### 例

以下是加载**iris**数据集的示例-

```python
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
feature_names = iris.feature_names
target_names = iris.target_names
print("Feature names:", feature_names)
print("Target names:", target_names)
print("\nFirst 10 rows of X:\n", X[:10])
```


## 分割数据集

为了检查模型的准确性，我们可以将数据集分为两部分**：训练集**和**测试集**。使用训练集训练模型，并使用测试集测试模型。之后，我们可以评估模型的效果。

### 例

以下示例将数据分成70:30的比例，即70％的数据将用作训练数据，而30％的数据将用作测试数据。数据集是IRIS数据集，如上例所示。

```python
from sklearn.datasets import load_iris
iris = load_iris()

X = iris.data
y = iris.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size = 0.3, random_state = 1
)

print(X_train.shape)
print(X_test.shape)

print(y_train.shape)
print(y_test.shape)
```


如上面的示例所示，它使用scikit-learn的**train_test_split（）**函数来拆分数据集。此函数具有以下参数-

- **X，y-**在这里，**X**是**特征矩阵**，y是**响应向量**，需要进行拆分。
- **test_size-**这表示测试数据与总给定数据的比率。如上例所示，我们为150行X 设置了**test_data = 0.3**。它将产生150 * 0.3 = 45行的测试数据。
- **random_size-**用于确保拆分将始终相同。在需要可重现结果的情况下，这很有用。

## 训练模型

接下来，我们可以使用我们的数据集来训练一些预测模型。如所讨论的，scikit-learn具有广泛的**机器学习（ML）算法**，这些**算法**具有一致的接口，可用于拟合，预测准确性，召回率等。

### 例

在下面的示例中，我们将使用KNN（K个最近邻居）分类器。无需赘述KNN算法的细节，因为将有单独的章节。本示例仅用于使您理解实现部分。

```python
from sklearn.datasets import load_iris
iris = load_iris()
X = iris.data
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(
   X, y, test_size = 0.4, random_state=1
)


from sklearn.neighbors import KNeighborsClassifier
from sklearn import metrics
classifier_knn = KNeighborsClassifier(n_neighbors = 3)
classifier_knn.fit(X_train, y_train)
y_pred = classifier_knn.predict(X_test)
# Finding accuracy by comparing actual response values(y_test)with predicted response value(y_pred)
print("Accuracy:", metrics.accuracy_score(y_test, y_pred))
# Providing sample data and the model will make prediction out of that data

sample = [[5, 5, 3, 2], [2, 4, 3, 5]]
preds = classifier_knn.predict(sample)
pred_species = [iris.target_names[p] for p in preds]
print("Predictions:", pred_species)
```

## 模型持久性

训练完模型后，最好保留模型以备将来使用，这样我们就不必一次又一次地重新训练它。可以借助***joblib\***软件包的**转储**和**加载**功能来***完成\***。

考虑下面的示例，在该示例中，我们将保存上面训练的模型（classifier_knn）供以后使用-

```python
from sklearn.externals import joblib
joblib.dump(classifier_knn, 'iris_classifier_knn.joblib')
```

上面的代码会将模型保存到名为`iris_classifier_knn.joblib`的文件中。现在，可以在以下代码的帮助下从文件中重新加载对象-

```python
joblib.load('iris_classifier_knn.joblib')
```

## 预处理数据

由于我们要处理大量数据并且该数据是原始格式，因此在将该数据输入到机器学习算法之前，我们需要将其转换为有意义的数据。此过程称为预处理数据。为此，Scikit-learn具有名为**预处理的**软件包。该**预处理**封装具有以下技术-

## 二值化

当我们需要将数值转换为布尔值时，可以使用这种预处理技术。

### 例

```python
import numpy as np
from sklearn import preprocessing
input_data = np.array(
  [
   [2.1, -1.9, 5.5],
   [-1.5, 2.4, 3.5],
   [0.5, -7.9, 5.6],
   [5.9, 2.3, -5.8]
  ]
)
data_binarized = preprocessing.Binarizer(threshold=0.5).transform(input_data)
print("\nBinarized data:\n", data_binarized)
```

在上面的示例中，我们使用**阈值** = 0.5，这就是为什么将所有大于0.5的值都转换为1，而将所有小于0.5的值都转换为0的原因。


## 均值去除

该技术用于消除特征向量的均值，以便每个特征都以零为中心。

### 例

```python
import numpy as np
from sklearn import preprocessing
input_data = np.array(
   [
      [2.1, -1.9, 5.5],
      [-1.5, 2.4, 3.5],
      [0.5, -7.9, 5.6],
      [5.9, 2.3, -5.8]
   ]
)
#displaying the mean and the standard deviation of the input data
print("Mean =", input_data.mean(axis=0))
print("Stddeviation = ", input_data.std(axis=0))
#Removing the mean and the standard deviation of the input data

data_scaled = preprocessing.scale(input_data)
print("Mean_removed =", data_scaled.mean(axis=0))
print("Stddeviation_removed =", data_scaled.std(axis=0))
```

## 缩放比例

我们使用这种预处理技术来缩放特征向量。特征向量的缩放很重要，因为特征不应该合成的大或小。

### 例

```python
import numpy as np
from sklearn import preprocessing
input_data = np.array(
   [
      [2.1, -1.9, 5.5],
      [-1.5, 2.4, 3.5],
      [0.5, -7.9, 5.6],
      [5.9, 2.3, -5.8]
   ]
)
data_scaler_minmax = preprocessing.MinMaxScaler(feature_range=(0,1))
data_scaled_minmax = data_scaler_minmax.fit_transform(input_data)
print("\nMin max scaled data:\n", data_scaled_minmax)
```


## 正常化

我们使用这种预处理技术来修改特征向量。特征向量的归一化是必要的，以便可以在公共尺度上测量特征向量。标准化有以下两种类型-

### L1归一化

也称为最小绝对偏差。它以使绝对值的总和在每一行中始终保持最大为1的方式修改值。以下示例显示了对输入数据进行L1标准化的实现。

### 例

```python
import numpy as np
from sklearn import preprocessing
input_data = np.array(
   [
      [2.1, -1.9, 5.5],
      [-1.5, 2.4, 3.5],
      [0.5, -7.9, 5.6],
      [5.9, 2.3, -5.8]
   ]
)
data_normalized_l1 = preprocessing.normalize(input_data, norm='l1')
print("\nL1 normalized data:\n", data_normalized_l1)
```


### L2归一化

也称为最小二乘。它以使平方和在每一行中始终保持最大为1的方式修改值。以下示例显示了对输入数据进行L2标准化的实现。

### 例

```python
import numpy as np
from sklearn import preprocessing
input_data = np.array(
   [
      [2.1, -1.9, 5.5],
      [-1.5, 2.4, 3.5],
      [0.5, -7.9, 5.6],
      [5.9, 2.3, -5.8]
   ]
)
data_normalized_l2 = preprocessing.normalize(input_data, norm='l2')
print("\nL1 normalized data:\n", data_normalized_l2)
```