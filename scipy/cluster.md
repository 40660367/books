# Scipy 簇聚(cluster)

K均值聚类是一种在一组未标记数据中查找聚类和聚类中心的方法。 直觉上，我们可以将一个群集(簇聚)看作 - 包含一组数据点，其点间距离与群集外点的距离相比较小。 给定一个K中心的初始集合，K均值算法重复以下两个步骤 -

- 对于每个中心，比其他中心更接近它的训练点的子集(其聚类)被识别出来。
- 计算每个聚类中数据点的每个要素的平均值，并且此平均向量将成为该聚类的新中心。

重复这两个步骤，直到中心不再移动或分配不再改变。 然后，可以将新点`x`分配给最接近的原型的群集。 SciPy库通过集群包提供了K-Means算法的良好实现。 下面来了解如何使用它。

## SciPy中实现K-Means

我们来看看并理解如何在SciPy中实现K-Means。

**导入K-Means**

下面来看看每个导入的函数的实现和用法。

```python
from scipy.cluster.vq import kmeans,vq,whiten
```

**数据生成**

我们需要生成(模拟)一些数据来探索聚类。参考以下代码 - 

```python
from numpy import vstack,array
from numpy.random import rand

# data generation with three features
data = vstack((rand(100,3) + array([.5,.5,.5]),rand(100,3)))
data
```

现在，我们来看看生成的模拟数据，根据每个要素标准化一组观察值。 

在运行K-Means之前，使用白化重新缩放观察集的每个特征维度是有好处的。 每个特征除以所有观测值的标准偏差以给出其单位差异。

**美化数据**

我们可使用以下代码来美白数据。

```python
# whitening of data
data = whiten(data)
print(data)
```

## 用三个集群计算K均值

现在使用以下代码计算三个群集的K均值。

```python
# computing K-Means with K = 3 (2 clusters)
centroids,_ = kmeans(data,3)
```

上述代码对形成K个簇的一组观测向量执行K均值。 K-Means算法调整质心直到不能获得足够的进展，即失真的变化，因为最后一次迭代小于某个阈值。 在这里，可以通过使用下面给出的代码打印`centroids`变量来观察簇。

```python
print(centroids)
```

使用下面给出的代码将每个值分配给一个集群。

```python
# assign each sample to a cluster
clx,_ = vq(data,centroids)
```

`vq`函数将`'M'`中的每个观察向量与`'N'` `obs`数组与`centroids`进行比较，并将观察值分配给最近的聚类。 它返回每个观察和失真的聚类。 我们也可以检查失真。使用下面的代码检查每个观察的聚类。

```python
# check clusters of observation
print(clx)
```

上述数组的不同值 - `0`,`1`,`2`表示簇。
<code class=gatsby-kernelname data-language=python></code>
