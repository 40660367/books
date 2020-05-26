# sklearn 使用PCA减少维度

降维是一种无监督的机器学习方法，用于减少选择主要特征的每个数据样本的特征变量的数量。主成分分析（PCA）是降维的流行算法之一。

## 精确的PCA

**主成分分析**（PCA）用于线性降维，使用数据的**奇异值分解**（SVD）将其投影到较低维度的空间中。在使用PCA进行分解时，在应用SVD之前，输入数据将居中但未按比例缩放。

Scikit-learn ML库提供了**sklearn.decomposition.PCA**模块，该模块被实现为可在其fit（）方法中学习n个组件的转换器对象。也可以将其用于新数据，以将其投影到这些组件上。

### 实例

以下示例将使用sklearn.decomposition.PCA模块从Pima Indians Diabetes数据集中找到最佳的5个主要成分。

```python
from pandas import read_csv
from sklearn.decomposition import PCA
path = r'/share/datasets/pima-indians-diabetes.csv'
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', ‘class']
dataframe = read_csv(path)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
pca = PCA(n_components = 5)
#print('')
fit = pca.fit(X)
print(("Explained Variance: %s") % (fit.explained_variance_ratio_))
print(fit.components_)
```
## 增量式PCA

**增量主成分分析**（IPCA）用于解决主成分分析（PCA）的最大局限，即PCA仅支持批处理，这意味着要处理的所有输入数据都应适合内存。

Scikit-learn ML库提供了**sklearn.decomposition.IPCA**模块，该模块可以通过对依次提取的数据块使用**partial_fit**方法或启用内存映射文件**np.memmap**来实现核外PCA。，而不将整个文件加载到内存中。

与PCA相同，使用IPCA进行分解时，在应用SVD之前，输入数据居中但未按每个功能缩放。

### 实例

以下示例将在Sklearn数字数据集上使用**sklearn.decomposition.IPCA**模块。

执行以下代码将比较耗时，请耐心等待

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import IncrementalPCA
X, _ = load_digits(return_X_y = True)
transformer = IncrementalPCA(n_components = 10, batch_size = 100)
transformer.partial_fit(X[:100, :])
X_transformed = transformer.fit_transform(X)
X_transformed.shape
```
在这里，我们可以部分拟合较小的数据批处理（就像我们对每批100个数据所做的那样），也可以让**fit（）**函数将数据分成若干批。

## 内核PCA

内核主成分分析（PCA的扩展）使用内核实现了非线性降维。它同时支持**transform和inverse_transform**。

Scikit学习ML库提供了**sklearn.decomposition.KernelPCA**模块。

### 实例

以下示例将在Sklearn数字数据集上使用**sklearn.decomposition.KernelPCA**模块。我们正在使用sigmoid内核。

执行以下代码将比较耗时，请耐心等待

```python
from sklearn.datasets import load_digits
from sklearn.decomposition import KernelPCA
X, _ = load_digits(return_X_y = True)
transformer = KernelPCA(n_components = 10, kernel = 'sigmoid')
X_transformed = transformer.fit_transform(X)
X_transformed.shape
```


## 使用随机SVD的PCA

使用随机SVD的主成分分析（PCA）用于通过删除与较低奇异值关联的成分的奇异矢量来将数据投影到较低维空间，从而保留大部分方差。在这里，带有可选参数**svd_solver ='randomized'**的**sklearn.decomposition.PCA**模块将非常有用。

### 实例

以下示例将使用带有可选参数svd_solver ='randomized'的**sklearn.decomposition.PCA**模块从Pima Indians Diabetes数据集中找到最佳的7个主要成分。

```python
from pandas import read_csv
from sklearn.decomposition import PCA
path = r'/share/datasets/pima-indians-diabetes.csv'
#names = ['preg', 'plas', 'pres', 'skin', 'test', 'mass', 'pedi', 'age', 'class']
dataframe = read_csv(path)
array = dataframe.values
X = array[:,0:8]
Y = array[:,8]
pca = PCA(n_components = 7,svd_solver = 'randomized')
fit = pca.fit(X)
print(("Explained Variance: %s") % (fit.explained_variance_ratio_))
print(fit.components_)
```