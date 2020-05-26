# sklearn 线性建模之线性回归

本章将帮助您学习Scikit-Learn中的线性建模。让我们首先了解什么是Sklearn中的线性回归。

线性建模是研究因变量（Y）与给定的一组自变量（X）之间的关系的最佳统计模型之一。可以通过拟合最佳路线来建立关系。

**sklearn.linear_model.LinearRegression**是用于实现线性回归的模块。

## 参量

下表包含**线性回归**模块使用的参数-

| 序号 | 参数及说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***fit_intercept-**布尔值，可选，默认为True*用于计算模型的截距。如果将此设置为false，则不会在计算中使用截距。 |
| 2    | ***normalize-**布尔值，可选，默认为False*如果将此参数设置为True，则回归变量X将在回归之前进行标准化。通过减去平均值并将其除以L2范数来完成归一化。如果fit_intercept = False，则将忽略此参数。 |
| 3    | ***copy_X-**布尔值，可选，默认为True*默认情况下为true，这意味着将复制X。但是，如果将其设置为false，则X可能会被覆盖。 |
| 4    | ***n_jobs** -int或None，可选（默认= None）*它表示要用于计算的作业数。 |

## 属性

下表包含**线性回归**模块使用的属性-

| 序号 | 属性和说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***coef_-**数组，shape（n_features）或（n_targets，n_features）*它用于估计线性回归问题的系数。如果在拟合过程中传递了多个目标，则它将是一个二维形状数组（n_targets，n_features）。例如 （y 2D）。另一方面，如果在拟合过程中仅传递了一个目标，则它将是一维长度（n_features）的数组。 |
| 2    | ***Intercept_-**数组*这是此线性模型中的一个独立术语。        |

### 实施实例

首先，导入所需的软件包-

```python
import numpy as np
from sklearn.linear_model import LinearRegression
LinearRegression
```

现在，提供自变量X的值-

```python
X = np.array([[1,1],[1,2],[2,2],[2,3]])
X
```

接下来，可以如下计算因变量y的值-

```python
y = np.dot(X, np.array([1,2])) + 3
y
```

现在，创建一个线性回归对象，如下所示：

```python
regr = LinearRegression(fit_intercept = True, normalize = True, copy_X = True, n_jobs = 2).fit(X,y)
regr
```

使用predict）方法使用此线性模型进行预测，如下所示：

```python
regr.predict(np.array([[3,5]]))
```

要获取预测的确定系数，我们可以使用Score()方法，如下所示：

```python
regr.score(X,y)
```

我们可以通过使用名为“ coef”的属性来估计系数，如下所示：

```python
regr.coef_
```

我们可以通过使用名为“ intercept”的属性来计算截距，即当所有X = 0时Y的期望平均值，如下所示-

```python
regr.intercept_
```

### 实施示例的完整代码

```python
import numpy as np
from sklearn.linear_model import LinearRegression
X = np.array([[1,1],[1,2],[2,2],[2,3]])
y = np.dot(X, np.array([1,2])) + 3
regr = LinearRegression(fit_intercept = True, normalize = True, copy_X = True, n_jobs = 2).fit(X,y)

print('predict:',regr.predict(np.array([[3,5]])))
print('score:',regr.score(X,y))
print('coef_:',regr.coef_)
print('intercept_:',regr.intercept_)
```

