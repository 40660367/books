# sklearn 线性建模之贝叶斯岭回归

贝叶斯回归允许自然机制通过使用概率分布而不是点估计来制定线性回归来生存数据不足或分布不良的数据。假定输出或响应“ y”是从概率分布中得出的，而不是估计为单个值。

在数学上，为了获得完全概率模型，假定响应y是围绕X的高斯分布$X_{w}$如下


$$
p\left(y\arrowvert X,w,\alpha\right)=N\left(y\arrowvert X_{w},\alpha\right)
$$

贝叶斯回归最有用的一种类型是贝叶斯岭回归，它估计了回归问题的概率模型。在这里，系数w的先验由球面高斯给出，如下所示-


$$
p\left(w\arrowvert \lambda\right)=N\left(w\arrowvert 0,\lambda^{-1}I_{p}\right)
$$

### 实施实例

以下Python脚本提供了使用sklearn **BayesianRidge**模块拟合Bayesian Ridge回归模型的简单示例。

```python
from sklearn import linear_model
X = [[0, 0], [1, 1], [2, 2], [3, 3]]
Y = [0, 1, 2, 3]
BayReg = linear_model.BayesianRidge()
BayReg.fit(X, Y)
```

从上面的输出中，我们可以检查计算中使用的模型参数。

现在，一旦拟合，模型可以预测新值，如下所示：

```python
BayReg.predict([[1,1]])
```

类似地，我们可以如下访问模型的系数w-

```python
BayReg.coef_
```