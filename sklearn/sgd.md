# sklearn 随机梯度下降(sgd)

在这里，我们将学习Sklearn中的优化算法，称为随机梯度下降（SGD）。

随机梯度下降法（SGD）是一种简单而有效的优化算法，用于查找使成本函数最小化的函数参数/系数值。换句话说，它用于凸损失函数（例如SVM和Logistic回归）下的线性分类器的判别学习。它已成功应用于大型数据集，因为是针对每个训练实例（而不是在实例结束时）执行系数更新。

## SGD分类器

随机梯度下降（SGD）分类器基本上实现了简单的SGD学习例程，该例程支持各种损失函数和分类惩罚。Scikit-learn提供了**SGDClassifier**模块来实现SGD分类。

### 参量

下表包含**SGDClassifier**模块使用的参数-

| 序号 | 参数及说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***损失** -str，默认='铰链'*它表示实现时要使用的损失函数。默认值为“ hinge”，这将为我们提供线性SVM。可以使用的其他选项是-**log-**这种损失将使我们进行逻辑回归，即概率分类器。**modified_huber-**平滑损失，对异常值和概率估计值具有容忍度。**squared_hinge-**与'hinge'损失相似，但二次惩罚。**感知器** -顾名思义，这是感知器算法使用的线性损耗。 |
| 2    | ***惩罚** -str，'none'，'l2'，'l1'，'elasticnet'*它是模型中使用的正则化术语。默认情况下为L2。我们可以使用L1或'elasticnet; 同样，但是两者都可能给模型带来稀疏性，因此L2无法实现。 |
| 3    | ***alpha-**浮点数，默认= 0.0001*Alpha（乘以正则项的常数）是调整参数，它决定了我们要对模型进行多少惩罚。默认值为0.0001。 |
| 4    | ***l1_ratio-**浮点数，默认= 0.15*这称为ElasticNet混合参数。其范围为0 <= l1_ratio <=1。如果l1_ratio = 1，则惩罚为L1惩罚。如果l1_ratio = 0，则惩罚为L2惩罚。 |
| 5    | ***fit_intercept-**布尔值，默认为True*此参数指定应将常量（偏差或截距）添加到决策函数。如果将其设置为false，则不会在计算中使用截距，并且将假定数据已经居中。 |
| 6    | ***tol-**浮点或无，可选，默认= 1.e-3*此参数表示迭代的停止标准。其默认值为False，但如果设置为None，则当n ***损失\*** > ***best_loss-\***连续***n_iter_no_change个周期的tol\***时，迭代将停止。 |
| 7    | ***shuffle-**布尔值，可选，默认= True*此参数表示我们是否希望在每个时期之后对训练数据进行混洗。 |
| 8    | ***详细** -整数，默认= 0*它代表了详细程度。其默认值为0。     |
| 9    | ***epsilon-**浮动，默认= 0.1*此参数指定不敏感区域的宽度。如果损失=“对ε不敏感”，则当前预测与正确标签之间的任何差异（小于阈值）将被忽略。 |
| 10   | ***max_iter** -int，可选，默认= 1000*顾名思义，它代表历时的最大通过次数，即训练数据。 |
| 11   | ***warm_start** -bool，可选，默认= false*通过将此参数设置为True，我们可以重用上一个调用的解决方案以适合初始化。如果我们选择默认值，即false，它将删除先前的解决方案。 |
| 12   | ***random_state** -int，RandomState实例或无，可选，默认=无*此参数表示生成的伪随机数的种子，在对数据进行混洗时会使用该种子。以下是选项。**INT** -在这种情况下，***random_state\***是由随机数生成所使用的种子。**RandomState实例** -在这种情况下，**random_state**是随机数生成器。**无** -在这种情况下，随机数生成器是np.random使用的RandonState实例。 |
| 13   | ***n_jobs** − int或无，可选，默认=无*它表示用于多类问题的OVA（一个对所有）计算中使用的CPU数量。默认值为none，表示1。 |
| 14   | ***learning_rate-**字符串，可选，默认='最优'*如果学习速率为“恒定”，则eta = eta0;如果学习率是“最佳”，则eta = 1.0 /（alpha *（t + t0）），其中t0由Leon Bottou选择；如果学习率='invscalling'，则eta = eta0 / pow（t，power_t）。如果学习率=“自适应”，则eta = eta0。 |
| 15   | ***eta0-**两倍，默认= 0.0*它代表上述学习率选项（即“恒定”，“渐进”或“自适应”）的初始学习率。 |
| 16   | ***power_t** -idouble，默认= 0.5*它是“增加”学习率的指数。    |
| 17   | ***early_stopping** − bool，默认= False*此参数表示当验证分数没有提高时，使用早期停止来终止训练。它的默认值是false，但是当设置为true时，它会自动将训练数据的分层部分留作验证，并在验证得分没有提高时停止训练。 |
| 18岁 | ***validation_fraction-**浮点数，默认= 0.1*仅当early_stopping为true时使用。它代表将训练数据设置为辅助参数以尽早终止训练数据的比例。 |
| 19   | ***n_iter_no_change-**整数，默认= 5*它表示迭代次数，如果算法在尽早停止之前运行，则没有任何改善。 |
| 20   | ***classs_weight** -dict，{class_label：weight}或“ balanced”，或者“无”，可选*此参数表示与类关联的权重。如果未提供，则该类的权重应为1。 |
| 20   | ***warm_start** -bool，可选，默认= false*通过将此参数设置为True，我们可以重用上一个调用的解决方案以适合初始化。如果我们选择默认值，即false，它将删除先前的解决方案。 |
| 21   | ***平均值** -iBoolean或int，可选，默认= false*它表示用于多类问题的OVA（一个对所有）计算中使用的CPU数量。默认值为none，表示1。 |

### 属性

下表包含**SGDClassifier**模块使用的属性-

| 序号 | 属性和说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***coef_-**数组，如果n_classes == 2，则形状为（1，n_features），否则为（n_classes，n_features）*此属性提供分配给要素的权重。 |
| 2    | ***intercept_** -阵列的形状（1）如果n_classes == 2，否则（n_classes，）*它代表决策功能中的独立项。 |
| 3    | ***n_iter_-**整数*它给出了达到停止标准的迭代次数。           |

**实施实例**

像其他分类器一样，随机梯度下降（SGD）必须配备以下两个数组-

- 存放训练样本的数组X。它的大小为[n_samples，n_features]。
- 保存目标值的数组Y，即训练样本的类别标签。它的大小为[n_samples]。

**例**

以下Python脚本使用SGDClassifier线性模型-

```python
import numpy as np
from sklearn import linear_model
X = np.array([[-1, -1], [-2, -1], [1, 1], [2, 1]])
Y = np.array([1, 1, 2, 2])
SGDClf = linear_model.SGDClassifier(max_iter = 1000, tol=1e-3,penalty = "elasticnet")
SGDClf.fit(X, Y)
```

现在，一旦拟合，模型可以预测新值，如下所示：

```python
SGDClf.predict([[2.,2.]])
```

对于上面的示例，我们可以借助以下python脚本获取权重向量-

```python
SGDClf.coef_
```

同样，我们可以在以下python脚本的帮助下获取拦截的值-

```python
SGDClf.intercept_
```

我们可以使用以下python脚本中使用的**SGDClassifier.decision_function**来获得到超平面的签名距离-

```python
SGDClf.decision_function([[2., 2.]])
```


## SGD回归器

随机梯度下降（SGD）回归器基本上实现了简单的SGD学习例程，该例程支持各种损失函数和惩罚以适应线性回归模型。Scikit-learn提供了**SGDRegressor**模块来实现SGD回归。

### 参量

**SGDRegressor**使用的参数与SGDClassifier模块中使用的参数几乎相同。区别在于“损失”参数。对于**SGDRegressor**模块的loss参数，正值如下所示-

- **squared_loss-**它是指普通的最小二乘拟合。
- **Huber：SGDRegressor-**通过从平方损失切换到线性损失超过ε距离来校正异常值。“休伯”的工作是修改“ squared_loss”，以使算法较少关注校正异常值。
- **epsilon_insensitive-**实际上，它忽略小于epsilon的错误。
- **squared_epsilon_insensitive-**与epsilon_insensitive相同。唯一的区别是，它变成超过ε容差的平方损耗。

另一个区别是名为'power_t'的参数的默认值是0.25，而不是**SGDClassifier中的** 0.5 。此外，它没有'class_weight'和'n_jobs'参数。

### 属性

SGDRegressor的属性也与SGDClassifier模块的属性相同。相反，它具有三个额外的属性，如下所示：

- **average_coef_** −数组，形状（n_features，）

顾名思义，它提供分配给功能的平均权重。

- **average_intercept_-**数组，shape（1，）

顾名思义，它提供了平均截距项。

- **t_-**整数

它提供了在训练阶段执行的体重更新次数。

**注意** -在将参数“ average”启用为True之后，属性average_coef_和average_intercept_将起作用。

**实施实例**

以下Python脚本使用**SGDRegressor**线性模型-

```python
import numpy as np
from sklearn import linear_model
n_samples, n_features = 10, 5
rng = np.random.RandomState(0)
y = rng.randn(n_samples)
X = rng.randn(n_samples, n_features)
SGDReg =linear_model.SGDRegressor(
   max_iter = 1000,penalty = "elasticnet",loss = 'huber',tol = 1e-3, average = True
)
SGDReg.fit(X, y)
```

现在，一旦拟合，我们就可以在以下python脚本的帮助下获得权重向量-

```python
SGDReg.coef_
```

同样，我们可以在以下python脚本的帮助下获取截距值-

```python
SGDReg.intercept_
```

我们可以通过以下python脚本获取训练阶段体重更新的次数-

```python
SGDReg.t_
```

## SGD的优点和缺点

遵循SGD的优点-

- 随机梯度下降（SGD）非常有效。
- 这很容易实现，因为有很多代码调优的机会。

遵循SGD的缺点-

- 随机梯度下降（SGD）需要一些超参数，例如正则化参数。
- 它对特征缩放很敏感。