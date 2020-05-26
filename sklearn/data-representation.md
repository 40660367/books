# sklearn 数据表示

学习即将根据数据创建模型。为此，计算机必须首先了解数据。接下来，我们将讨论表示数据的各种方式，以便计算机可以理解-

在Scikit学习中表示数据的最佳方法是表格。表格表示数据的二维网格，其中行表示数据集的各个元素，列表示与这些单个元素相关的数量。

### 例

通过下面给出的示例，我们可以借助python ***sklearn***库以Pandas DataFrame的形式下载***IRIS数据集\***。

```python
from sklearn import datasets
iris = datasets.load_iris()
iris.head()
```


从上面的输出中，我们可以看到数据的每一行代表一个观察到的花朵，行数代表数据集中的花朵总数。通常，我们将矩阵的行称为样本。

另一方面，数据的每一列代表描述每个样品的定量信息。通常，我们将矩阵的列称为特征。

## 数据作为特征矩阵

特征矩阵可以定义为表格布局，其中信息可以被认为是二维矩阵。它存储在名为**X**的变量中，并假定是二维的，形状为[n_samples，n_features]。通常，它包含在NumPy数组或Pandas DataFrame中。如前所述，样本始终代表数据集描述的单个对象，而要素代表以定量方式描述每个样本的不同观察结果。

## 数据作为目标数组

除了用X表示的功能矩阵外，我们还有目标数组。也称为标签。用y表示。标签或目标数组通常是一维，长度为n_samples。它通常包含在NumPy ***数组***或Pandas ***系列中***。目标数组可以同时具有值，连续数值和离散值。

### 目标数组与功能列有何不同？

我们可以通过一点来区分两者，即目标数组通常是我们要从数据中预测的数量，即，从统计角度来说，它是因变量。

### 例

在下面的示例中，我们从IRIS数据集中基于其他测量值来预测花朵的种类。在这种情况下，“种类”列将被视为要素。

```python
%matplotlib inline
import seaborn as sns
import pandas as pd

iris = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sns.set()

#画图时间较久，需要稍等半分钟左右
sns.pairplot(iris, hue='species', height=3);
```