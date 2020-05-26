# 集成学习方法之随机森林

## 什么是集成学习方法

集成学习通过建立几个模型组合的来解决单一预测问题。它的工作原理是**生成多个分类器/模型**，各自独立地学习和作出预测。**这些预测最后结合成组合预测，因此优于任何一个单分类的做出预测。**

## 什么是随机森林

在机器学习中，**随机森林是一个包含多个决策树的分类器**，并且其输出的类别是由个别树输出的类别的众数而定。

![随机森林](./images/随机森林.png)

例如, 如果你训练了5个树, 其中有4个树的结果是True, 1个数的结果是False, 那么最终投票结果就是True

![投票](./images/投票.png)

## 随机森林原理过程

学习算法根据下列算法而建造每棵树：

- 用N来表示训练用例（样本）的个数，M表示特征数目。
  - 1、一次随机选出一个样本，重复N次， （有可能出现重复的样本）
  - 2、随机去选出m个特征, m <<M，建立决策树
- 采取bootstrap抽样

### 为什么采用BootStrap抽样

- 为什么要随机抽样训练集？　　
  - 如果不进行随机抽样，每棵树的训练集都一样，那么最终训练出的树分类结果也是完全一样的
- 为什么要有放回地抽样？
  - 如果不是有放回的抽样，那么每棵树的训练样本都是不同的，都是没有交集的，这样每棵树都是“有偏的”，都是绝对“片面的”（当然这样说可能不对），也就是说每棵树训练出来都是有很大的差异的；而随机森林最后分类取决于多棵树（弱分类器）的投票表决。

**API**

- `class sklearn.ensemble.RandomForestClassifier(n_estimators=10, criterion=’gini’, max_depth=None, bootstrap=True, random_state=None, min_samples_split=2)`
  - 随机森林分类器
  - n_estimators：integer，optional（default = 10）森林里的树木数量120,200,300,500,800,1200
  - criteria：string，可选（default =“gini”）分割特征的测量方法
  - max_depth：integer或None，可选（默认=无）树的最大深度 5,8,15,25,30
  - max_features="auto”,每个决策树的最大特征数量
    - If "auto", then `max_features=sqrt(n_features)`.
    - If "sqrt", then `max_features=sqrt(n_features)` (same as "auto").
    - If "log2", then `max_features=log2(n_features)`.
    - If None, then `max_features=n_features`.
  - bootstrap：boolean，optional（default = True）是否在构建树时使用放回抽样
  - min_samples_split:节点划分最少样本数
  - min_samples_leaf:叶子节点的最小样本数

- 超参数：n_estimator, max_depth, min_samples_split,min_samples_leaf

### 代码

```python
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
iris = load_iris()
x_train, x_test, y_train, y_test = train_test_split(iris.data, iris.target, random_state=22)
```



```python
from sklearn.ensemble import RandomForestClassifier  
from sklearn.model_selection import GridSearchCV

# 随机森林去进行预测
rf = RandomForestClassifier()

param = {"n_estimators": [120,200,300,500,800,1200], "max_depth": [5, 8, 15, 25, 30]}

# 超参数调优
gc = GridSearchCV(rf, param_grid=param, cv=2)

gc.fit(x_train, y_train)

print("随机森林预测的准确率为：", gc.score(x_test, y_test))
```

## 总结

- 在当前所有算法中，具有极好的准确率
- 能够有效地运行在大数据集上，处理具有高维特征的输入样本，而且不需要降维
- 能够评估各个特征在分类问题上的重要性

## 作业：

- 说名随机森林每棵决策树的建立过程
- 知道为什么需要随机有放回(Bootstrap)的抽样
- 说明随机森林的超参数