# sklearn 决策树(decision tree)

在本章中，我们将学习称为决策树的Sklearn中的学习方法。

决策树（DT）是最强大的非参数有监督学习方法。它们可用于分类和回归任务。DT的主要目标是通过学习从数据特征推导出的简单决策规则来创建预测目标变量值的模型。决策树有两个主要实体。一个是根节点，数据在其中拆分，另一个是决策节点或叶子，在此处获得最终输出。

## 决策树算法

下面解释了不同的决策树算法-

### ID3

它由Ross Quinlan在1986年开发。它也称为ID3。此算法的主要目的是为每个节点找到那些分类特征，这些分类特征将为分类目标产生最大的信息增益。

它使树生长到最大大小，然后为了提高树在看不见的数据上的能力，请执行修剪步骤。该算法的输出将是多路树。

### C4.5

它是ID3的后继者，并动态定义一个离散属性，该属性将连续属性值划分为一组离散的间隔。这就是它消除了分类功能限制的原因。它将经过ID3训练的树转换为“ IF-THEN”规则集。

为了确定应用这些规则的顺序，将首先评估每个规则的准确性。

### C5.0

它的工作方式与C4.5类似，但是它使用较少的内存并构建较小的规则集。它比C4.5更准确。

### cart

这称为分类和回归树算法。它基本上通过使用特征和阈值生成二进制拆分，从而在每个节点上产生最大的信息增益（称为基尼索引）。

同质性取决于基尼系数，基尼系数的值越高，同质性越高。它类似于C4.5算法，但不同之处在于它不计算规则集，也不支持数字目标变量（回归）。

## 决策树分类

在这种情况下，决策变量是分类的。

**Sklearn模块** -Scikit-learn库提供模块名称**DecisionTreeClassifier，**用于对数据集执行多类分类。

### 实施实例

下面的Python脚本将使用**sklearn.tree.DecisionTreeClassifier**模块构造一个分类器，根据我们的数据集中的25个样本和两个特征（“身高”和“头发长度”）来预测男性或女性-

```python
from sklearn import tree
from sklearn.model_selection import train_test_split


X=[[165,19],[175,32],[136,35],[174,65],[141,28],[176,15]\
,[131,32],[166,6],[128,32],[179,10],[136,34],[186,2],[126,25],\
   [176,28],[112,38],[169,9],[171,36],[116,25],[196,25], \
   [196,38], [126,40], [197,20], [150,25], [140,32],[136,35]]


Y=['Man','Woman','Woman','Man','Woman','Man','Woman','Man','Woman','Man',\
   'Woman','Man','Woman','Woman','Woman','Man','Woman','Woman','Man', 'Woman', \
   'Woman', 'Man', 'Man', 'Woman', 'Woman']


data_feature_names = ['height','length of hair']


X_train, X_test, y_train, y_test = train_test_split(X, Y, test_size = 0.3, random_state = 1)
DTclf = tree.DecisionTreeClassifier()
DTclf = DTclf.fit(X,Y)
prediction = DTclf.predict([[135,29]])
print(prediction)
```

我们还可以通过使用以下python Forecast_proba（）方法来预测每个类别的概率，如下所示：

```python
prediction = DTclf.predict_proba([[135,29]])
print(prediction)
```
## 决策树回归

在这种情况下，决策变量是连续的。

**Sklearn模块** -Scikit-learn库提供模块名称**DecisionTreeRegressor，**用于将决策树应用于回归问题。

### 参量

**DecisionTreeRegressor**使用的参数与**DecisionTreeClassifier**模块中使用的参数几乎相同。区别在于“标准”参数。对于**DecisionTreeRegressor**模块的**'criterion**：string，可选的default =“ mse”'参数具有以下值-

- **mse-**代表均方误差。它等于减少方差作为特征选择准则。它使用每个终端节点的平均值将L2损耗降至最低。
- **freidman_mse-**它也使用均方误差，但具有弗里德曼的改善得分。
- **mae-**代表平均绝对误差。它使用每个终端节点的中值将L1损耗最小化。

另一个区别是它没有***'class_weight'\***参数。

### 属性

**DecisionTreeRegressor的**属性也与**DecisionTreeClassifier**模块的属性相同。区别在于它不具有**'classes_'**和**'n_classes_** '属性。

### 方法

**DecisionTreeRegressor的**方法也与**DecisionTreeClassifier**模块的方法相同。区别在于它不具有**'predict_log_proba（）'**和**'predict_proba（）'** '属性。

### 实施实例

决策树回归模型中的fit（）方法将采用y的浮点值。我们来看一个使用**Sklearn.tree.DecisionTreeRegressor**的简单实现示例-

```python
from sklearn import tree
X = [[1, 1], [5, 5]]
y = [0.1, 1.5]
DTreg = tree.DecisionTreeRegressor()
DTreg = DTreg.fit(X, y)
DTreg
```

拟合后，我们可以使用此回归模型进行预测，如下所示：

```python
DTreg.predict([[4, 5]])
```