# 岭回归

## 带有L2正则化的线性回归-岭回归

岭回归，其实也是一种线性回归。只不过在算法建立回归方程时候，加上正则化的限制从而达到解决过拟合的效果

**API**

- `sklearn.linear_model.Ridge(alpha=1.0, fit_intercept=True,solver="auto", normalize=False)`
- 具有l2正则化的线性回归
- alpha:正则化力度，也叫 λ
  - **λ取值：0~1 1~10**
- solver:会根据数据自动选择优化方法
  - **sag:如果数据集、特征都比较大，选择该随机梯度下降优化**
- normalize:数据是否进行标准化
  - normalize=False:可以在fit之前调用preprocessing.StandardScaler标准化数据
- Ridge.coef_:回归权重
- Ridge.intercept_:回归偏置

> All last four solvers support both dense and sparse data. However,only 'sag' supports sparse input when `fit_intercept` is True.

#### Ridge方法相当于SGDRegressor(penalty='l2', loss="squared_loss"),只不过SGDRegressor实现了一个普通的随机梯度下降学习，推荐使用Ridge(实现了SAG)

- `sklearn.linear_model.RidgeCV(_BaseRidgeCV, RegressorMixin)`
- 具有l2正则化的线性回归，可以进行交叉验证
- coef_:回归系数

```
class _BaseRidgeCV(LinearModel):
  def __init__(self, alphas=(0.1, 1.0, 10.0),
               fit_intercept=True, normalize=False, scoring=None,
             cv=None, gcv_mode=None,
               store_cv_values=False):
```

#### 练习：波士顿房价预测为例 ，观察正则化程度的变化，对结果的影响

![正则化力度](./images/正则化力度.png)

- 正则化力度越大，权重系数会越小

- 正则化力度越小，权重系数会越大


```python
from sklearn import datasets
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

#先用key方法查看数据集
print(boston.keys())

#查看feature_names
print(boston['feature_names'])

#这里的data有13个维度，target就是我们要预测的房价，接下来再查看feature_names
print(boston['feature_names'])

#其中'RM'列就是我们需要的房间数，接下为了方便处理，我们将其转为DataFrame类型，并进行数据划分得到训练集和测试集

data = pd.DataFrame(boston['data'],columns=boston['feature_names'])
x = pd.DataFrame(data['RM'],columns=['RM'])
y = pd.DataFrame(boston['target'],columns=['target'])
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33, random_state=42)
```

  ```python
from sklearn.linear_model import Ridge
rd = Ridge(alpha=1.0)
  
rd.fit(x_train, y_train)
print("岭回归的权重参数为：", rd.coef_)

y_predict = rd.predict(x_test)

print("岭回归的预测的结果为：", y_predict)


print("岭回归的均方误差为：", mean_squared_error(y_test, y_predict))
  ```

## 作业：

- 说明岭回归的原理即与线性回归的不同之处
- 说明正则化对于权重参数的影响
- 说明L1和L2正则化的区别
- 复现波士顿房价预测