# sklearn 线性建模之逻辑回归

逻辑回归尽管有其名称，但它是一种分类算法，而不是回归算法。基于给定的一组独立变量，它可用于估计离散值（0或1，是/否，是/否）。也称为logit或MaxEnt分类器。

基本上，它通过使用事件的后勤函数估计事件发生的可能性，来测量分类因变量和一个或多个自变量之间的关系。

**sklearn.linear_model.LogisticRegression**是用于实现逻辑回归的模块。

## 参量

下表列出了**Logistic回归**模块使用的参数-

| 序号 | 参数及说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***惩罚** -str，'L1'，'L2'，'elasticnet'或无，可选，默认='L2'*此参数用于指定惩罚（正则化）中使用的标准（L1或L2）。 |
| 2    | ***dual-**布尔值，可选，默认= False*它用于双重或原始制剂，而双重制剂仅用于L2罚分。 |
| 3    | ***tol-**浮动，可选，默认值= 1e-4*它代表停止标准的容限。     |
| 4    | ***C-**浮动，可选，默认= 1.0*它表示正则化强度的倒数，必须始终为正浮点数。 |
| 5    | ***fit_intercept-**布尔值，可选，默认= True*此参数指定应将常量（偏差或截距）添加到决策函数。 |
| 6    | ***intercept_scaling-**浮点数，可选，默认= 1*此参数在以下情况下很有用该**解算器“liblinear”**是用于***fit_intercept\***设置为true |
| 7    | ***class_weight** -dict或'balanced'可选，默认= none*它表示与类关联的权重。如果我们使用默认选项，则意味着所有类都应具有权重一。另一方面，如果选择class_weight：balanced，它将使用y的值自动调整权重。 |
| 8    | ***random_state** -int，RandomState实例或无，可选，默认=无*此参数表示生成的伪随机数的种子，在对数据进行混洗时会使用该种子。以下是选项**INT** -在这种情况下，random_state是由随机数生成所使用的种子。**RandomState实例** -在这种情况下，*random_state*是随机数生成器。**无** -在这种情况下，随机数生成器是np.random使用的RandonState实例。 |
| 9    | ***求解器** -str，{'newton-cg'，'lbfgs'，'liblinear'，'saag'，'saga'}，可选，默认='liblinear'*此参数表示在优化问题中使用哪种算法。以下是此参数下选项的属性-**liblinear-**对于小型数据集，这是一个不错的选择。它还处理L1罚款。对于多类问题，它仅限于一个休息方案。**newton-cg-**仅处理L2罚款。**lbfgs-**对于多类问题，它处理多项式损失。它还仅处理L2罚款。**saga-**对于大型数据集，这是一个不错的选择。对于多类问题，它还处理多项式损失。除了L1罚款外，它还支持“弹性网”罚款。**sag-**也用于大型数据集。对于多类问题，它还处理多项式损失。 |
| 10   | ***max_iter** -int，可选，默认= 100*顾名思义，它表示求解器收敛所需的最大迭代次数。 |
| 11   | ***multi_class** − str，{'ovr'，'multinomial'，'auto'}，可选，默认='ovr'***ovr-**对于此选项，每个标签都适合二进制问题。**multimonial** -对于此选项，最小的损失是整个概率分布的多项损失配合。如果solver ='liblinear'，则无法使用此选项。**自动** -如果solver ='liblinear'或数据为二进制，则此选项将选择'ovr'，否则将选择'多项式'。 |
| 12   | ***详细** -int，可选，默认= 0*默认情况下，此参数的值为0，但对于liblinear和lbfgs求解器，我们应将verbose设置为任何正数。 |
| 13   | ***warm_start** -bool，可选，默认= false*通过将此参数设置为True，我们可以重用上一个调用的解决方案以适合初始化。如果我们选择默认值，即false，它将删除先前的解决方案。 |
| 14   | ***n_jobs** -int或None，可选，默认= None*如果multi_class ='ovr'，则此参数表示在对类进行并行化时使用的CPU内核数。当solver ='liblinear'时，它将被忽略。 |
| 15   | ***l1_ratio-**浮动或无，可选，dgtefault =无*当惩罚='elasticnet'时使用。它基本上是0 <= l1_ratio> = 1的Elastic-Net混合参数。 |

## 属性

跟随表包括**逻辑回归**模块使用的属性-

| 序号 | 属性和说明                                                   |
| ---- | ------------------------------------------------------------ |
| 1个  | ***coef_-**数组，shape（n_features，）或（n_classes，n_features）*它用于估计决策函数中特征的系数。当给定问题为二进制时，其形状为（1，n_features）。 |
| 2    | ***Intercept_-**数组，shape（1）或（n_classes）*它表示添加到决策函数的常数（也称为偏差）。 |
| 3    | ***classes_-**数组，形状（n_classes）*它将提供分类器已知的类标签列表。 |
| 4    | ***n_iter_-**数组，形状（n_classes）或（1）*它返回所有类的实际迭代数。 |

### 实施实例

以下Python脚本提供了在scikit-learn的**IRIS**数据集上实现逻辑回归的简单示例-

```python
from sklearn import datasets
from sklearn import linear_model
from sklearn.datasets import load_iris
X, y = load_iris(return_X_y = True)
LRG = linear_model.LogisticRegression(random_state = 0,solver ='liblinear',multi_class='auto').fit(X, y)
LRG.score(X, y)
```