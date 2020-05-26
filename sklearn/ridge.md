# sklearn 线性建模之岭回归

Ridge回归或Tikhonov正则化是执行L2正则化的正则化技术。它通过添加等于系数幅度平方的损失（收缩量）来修改损耗函数。
$$
\displaystyle\sum\limits_{j=1}^m\left(Y_{i}-W_{0}-\displaystyle\sum\limits_{i=1}^nW_{i}X_{ji} \right)^{2}+\alpha\displaystyle\sum\limits_{i=1}^nW_i^2=loss_{-}function+\alpha\displaystyle\sum\limits_{i=1}^nW_i^2
$$
**sklearn.linear_model.Ridge**是用于求解回归模型的模块，其中损失函数为线性最小二乘法，正则**化为** L2。

## 参量

下表包含**Ridge**模块使用的参数-

| 序号 | 参数及说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***alpha-** {float，like-array}，shape（n_targets）*Alpha是调整参数，它决定了我们要对模型进行多少惩罚。 |
| 2    | ***fit_intercept-**布尔值*此参数指定应将常量（偏差或截距）添加到决策函数。如果将其设置为false，则不会在计算中使用截距。 |
| 3    | ***tol-**浮动，可选，默认值= 1e-4*它代表了解决方案的精度。   |
| 4    | ***normalize-**布尔值，可选，默认= False*如果将此参数设置为True，则回归变量X将在回归之前进行标准化。通过减去平均值并将其除以L2范数来完成归一化。如果**fit_intercept = False**，则将忽略此参数。 |
| 5    | ***copy_X-**布尔值，可选，默认= True*默认情况下为true，这意味着将复制X。但是，如果将其设置为false，则X可能会被覆盖。 |
| 6    | ***max_iter** -int，可选*顾名思义，它表示共轭梯度求解器的最大迭代次数。 |
| 7    | ***求解器** -str，{'auto'，'svd'，'cholesky'，'lsqr'，'sparse_cg'，'sag'，'saga'}'*此参数表示在计算例程中使用哪个求解器。以下是此参数下选项的属性**自动** -可以根据数据类型自动选择求解器。**svd-**为了计算Ridge系数，此参数使用X的奇异值分解。**cholesky-**此参数使用标准的**scipy.linalg.solve（）**函数获取封闭形式的解决方案。**lsqr-**它是最快的，并使用专用的正则化最小二乘例程scipy.sparse.linalg.lsqr。**松弛** -它使用迭代过程和随机平均梯度下降。**saga-**还使用了迭代过程和改进的随机平均梯度下降。 |
| 8    | ***random_state** -int，RandomState实例或无，可选，默认=无*此参数表示生成的伪随机数的种子，在对数据进行混洗时会使用该种子。以下是选项-**INT** -在这种情况下，**random_state**是由随机数生成所使用的种子。**RandomState实例** -在这种情况下，**random_state**是随机数生成器。**无** -在这种情况下，随机数生成器是np.random使用的RandonState实例。 |

## 属性

跟随表包含**Ridge**模块使用的属性-

| 序号 | 属性和说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***coef_-**数组，shape（n_features）或（n_target，n_features）*此属性提供权重向量。 |
| 2    | ***截距** -浮动\| 数组，形状=（n_targets）*它代表决策功能中的独立项。 |
| 3    | ***n_iter_-**数组或无，形状（n_targets）*仅适用于“ sag”和“ lsqr”求解器，返回每个目标的实际迭代数。 |

### 实施实例

以下Python脚本提供了实现Ridge回归的简单示例。我们正在使用15个示例和10个功能。在我们的例子中，alpha的值为0.5。有两种方法，分别是**fit（）**和**score（）**来拟合该模型并计算分数。

```python
from sklearn.linear_model import Ridge
import numpy as np
n_samples, n_features = 15, 10
rng = np.random.RandomState(0)
y = rng.randn(n_samples)
X = rng.randn(n_samples, n_features)
rdg = Ridge(alpha = 0.5)
rdg.fit(X, y)
rdg.score(X,y)
```

输出显示，上面的Ridge回归模型给出的得分约为76％。为了获得更高的准确性，我们可以增加样本和特征的数量。

对于上面的示例，我们可以借助以下python脚本获取权重向量-

```python
rdg.coef_
```

同样，我们可以在以下python脚本的帮助下获取拦截的值-

```python
rdg.intercept_
```

