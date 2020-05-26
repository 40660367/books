# sklearn 朴素贝叶斯分类(NBC)

朴素贝叶斯方法是一组基于贝叶斯定理的有监督学习算法，其中强烈假设所有预测变量彼此独立，即，一个类中某个特征的存在独立于同一类中任何其他特征的存在类。这是天真的假设，因此将这些方法称为天真贝叶斯方法。

贝叶斯定理陈述以下关系，以便找到类别的后验概率，即标签的概率和某些观察到的特征

$$
P\left(\begin{array}{c} Y\arrowvert features\end{array}\right)=\left(\frac{P\lgroup Y\rgroup P\left(\begin{array}{c} features\arrowvert Y\end{array}\right)}{P\left(\begin{array}{c} features\end{array}\right)}\right)
$$


## 建立朴素贝叶斯分类器

我们也可以在Scikit学习数据集上应用朴素贝叶斯分类器。在下面的示例中，我们将应用GaussianNB并拟合Scikit-leran的breast_cancer数据集。

### 例

```python
import sklearn
from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import train_test_split
data = load_breast_cancer()
label_names = data['target_names']
labels = data['target']
feature_names = data['feature_names']
features = data['data']

print(label_names)
print(labels[0])
print(feature_names[0])
print(features[0])
print('\n')
train, test, train_labels, test_labels = train_test_split(features,labels,test_size = 0.40, random_state = 42)
from sklearn.naive_bayes import GaussianNB
GNBclf = GaussianNB()
model = GNBclf.fit(train, train_labels)
preds = GNBclf.predict(test)
print(preds)
```

以上输出由一系列0和1组成，它们基本上是来自肿瘤类别的预测值，即恶性和良性。