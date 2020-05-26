# Pandas boston房价预测

从Scikit-learn的数据集里载入波士顿的房价数据：

```python
import numpy as np
from sklearn import datasets
import sklearn

boston = datasets.load_boston()
```
波士顿数据集是一个具有13个特征的常见线性数据集，也是NG网课里的第一个例子。我们可以打印其描述文档来获取其各项属性：

```python
print(boston.DESCR)
```

>线性回归模型——手动分割训练集和测试集

我们先给定一个默认的采样频率，如0.5，用于将训练集和测试集分为两个相等的集合：
```python
sampleRatio = 0.5
n_samples = len(boston.target)
sampleBoundary = int(n_samples * sampleRatio)
```
接着，洗乱整个集合，并取出相应的训练集和测试集数据：
```python
shuffleIdx = range(n_samples)
np.random.shuffle(shuffleIdx) # 需要导入numpy
# 训练集的特征和回归值
train_features = boston.data[shuffleIdx[:sampleBoundary]]
train_targets = boston.target[shuffleIdx[:sampleBoundary]]
# 测试集的特征和回归值 
test_features = boston.data[shuffleIdx[sampleBoundary:]]
test_targets = boston.target[shuffleIdx[sampleBoundary:]]
```
接下来，获取回归模型，拟合并得到测试集的预测结果：
```python
lr = sklearn.linear_model.LinearRegression() # 需要导入sklearn的linear_model
lr.fit(train_features, train_targets) # 拟合
y = lr.predict(test_features) # 预测
```
最后，把预测结果通过matplotlib画出来：
```python
import matplotlib.pyplot as plt
plt.plot(y, test_targets, 'rx') # y = ωX
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'b-.', lw=4) # f(x)=x
plt.ylabel("Predieted Price")
plt.xlabel("Real Price")
plt.show()
```

在蓝线上的点是准确预测的点，而在蓝线以下及以上的点，分别是过低预测及过高预测的结果。

>线性回归模型——KFlod交叉验证

来自官方的样例：
```python
from sklearn import datasets
from sklearn.model_selection import cross_val_predict
from sklearn import linear_model
import matplotlib.pyplot as plt

lr = linear_model.LinearRegression()
boston = datasets.load_boston()
y = boston.target

# cross_val_predict returns an array of the same size as `y` where each entry
# is a prediction obtained by cross validation:
predicted = cross_val_predict(lr, boston.data, y, cv=10)

fig, ax = plt.subplots()
ax.scatter(y, predicted, edgecolors=(0, 0, 0))
ax.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', lw=4)
ax.set_xlabel('Measured')
ax.set_ylabel('Predicted')
plt.show()
```

主要用的是交叉验证模型中的cross_val_predict，同样给定了线性回归模型(linear_model.LinearRegression()，模型需要实现fit()方法)，并划分了cv=10个交叉验证集合。比起手动划分集合，代码更加简短且易读性更好，没什么好过多分析的。默认的是KFlod方式，结果如下：


>交叉验证模型的打分

考虑到使用了交叉验证，我们可以对一种估计模型（estimator）进行评分，需要用到sklearn.cross_validation的cross_val_score()：
```python
from sklearn import cross_validation
print cross_validation.cross_val_score(lr, boston.data, y, cv=10)
```