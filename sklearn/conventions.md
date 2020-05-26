# sklearn 约定

Scikit-learn的对象共享一个统一的基本API，该API由以下三个互补接口组成-

- **估计器接口** -用于构建和拟合模型。
- **预测器接口** -用于进行预测。
- **转换器接口** -用于转换数据。

这些API采用简单的约定，并且以避免框架代码泛滥的方式对设计选择进行了指导。

## 公约目的

约定的目的是确保API遵循以下广泛原则-

**一致性** -所有对象（无论是基础对象还是复合对象）都必须共享一致的接口，该接口进一步由一组有限的方法组成。

**检查** -构造函数参数和由学习算法确定的参数值应存储并公开为公共属性。

**类的不扩散** -数据集应表示为NumPy数组或Scipy稀疏矩阵，而超参数名称和值应表示为标准Python字符串，以避免框架代码的泛滥。

**组合** -无论是将算法表达为数据转换的序列还是转换的组合，或者自然地视为在其他算法上参数化的元算法，都应从现有的构建模块中实施并组成。

**合理的默认值** -每当操作需要用户定义的参数时，在scikit-learn中，都会定义适当的默认值。此默认值应使操作以明智的方式执行，例如，为手头的任务提供基线解决方案。

## 各种约定

Sklearn中可用的约定在下面进行了解释-

### 类型转换

它指出输入应**强制转换**为**float64**。在下面的示例中，其中**sklearn.random_projection**模块用于减少数据的维数，将对此进行解释-

```python
import numpy as np
from sklearn import random_projection
range = np.random.RandomState(0)
X = range.rand(10,2000)
X = np.array(X, dtype = 'float32')
X.dtype
transformer_data = random_projection.GaussianRandomProjection()
X_new = transformer_data.fit_transform(X)
X_new.dtype
```

在上面的示例中，我们可以看到X是**float32**，它由**fit_transform（X）强制转换**为**float64**。

### 改装和更新参数

通过**set_params（）**方法构造估算器的超参数后，可以对其进行更新和调整。让我们看下面的例子来理解它-

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y = True)
clf = SVC()
clf.set_params(kernel = 'linear').fit(X, y)
clf.predict(X[:5])
```


一旦估计已经构造，上面的代码将更改默认内核**RBF**到线性经由**SVC.set_params（）** 。

现在，以下代码将把内核改回rbf，以重新拟合估算器并进行第二次预测。

```python
clf.set_params(kernel = 'rbf', gamma = 'scale').fit(X, y)
clf.predict(X[:5])
```

### 完整的代码

以下是完整的可执行程序-

```python
import numpy as np
from sklearn.datasets import load_iris
from sklearn.svm import SVC
X, y = load_iris(return_X_y = True)
clf = SVC()
 
#linear kernel
clf.set_params(kernel = 'linear').fit(X, y)
print(clf.predict(X[:5]))

#rbf kernel
clf.set_params(kernel = 'rbf', gamma = 'scale').fit(X, y)
print(clf.predict(X[:5]))
```

### 多类别和多标签拟合

在进行多类拟合的情况下，学习任务和预测任务都取决于适合的目标数据的格式。使用的模块是**sklearn.multiclass**。检查下面的示例，其中多类分类器适合一维数组。

```python
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
X = [[1, 2], [3, 4], [4, 5], [5, 2], [1, 1]]
y = [0, 0, 1, 1, 2]
classif = OneVsRestClassifier(estimator = SVC(gamma = 'scale',random_state = 0))
classif.fit(X, y).predict(X)
```


在上面的示例中，分类器适合多类标签的一维数组，并且**predict（）**方法因此提供了相应的多类预测。但另一方面，也可以将二进制标签指示符的二维数组拟合如下：

```python
from sklearn.svm import SVC
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
X = [[1, 2], [3, 4], [4, 5], [5, 2], [1, 1]]
y = LabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)
```


类似地，在多标签拟合的情况下，可以为一个实例分配多个标签，如下所示：

```python
from sklearn.preprocessing import MultiLabelBinarizer
y = [[0, 1], [0, 2], [1, 3], [0, 2, 3], [2, 4]]
y = MultiLabelBinarizer().fit_transform(y)
classif.fit(X, y).predict(X)
```

在上面的示例中，使用**sklearn.MultiLabelBinarizer**对要适合的多**标签**二维数组进行二值化。这就是为什么predict（）函数将二维数组作为输出，每个实例带有多个标签的原因。