# Scipy 统计函数(stats)

所有的统计函数都位于子包`scipy.stats`中，并且可以使用`info(stats)`函数获得这些函数的完整列表。随机变量列表也可以从`stats`子包的`docstring`中获得。 该模块包含大量的概率分布以及不断增长的统计函数库。

每个单变量分布都有其自己的子类，如下表所述 -

| 编号 | 类              | 描述                           |
| ---- | --------------- | ------------------------------ |
| 1    | `rv_continuous` | 用于子类化的通用连续随机变量类 |
| 2    | `rv_discrete`   | 用于子类化的通用离散随机变量类 |
| 3    | `rv_histogram`  | 生成由直方图给出的分布         |

## 正态连续随机变量

随机变量X可以取任何值的概率分布是连续的随机变量。 位置(`loc`)关键字指定平均值。 比例(`scale`)关键字指定标准偏差。

作为`rv_continuous`类的一个实例，规范对象从中继承了一系列泛型方法，并通过特定于此特定分发的细节完成它们。

要计算多个点的CDF，可以传递一个列表或一个NumPy数组。 看看下面的一个例子。

```python
from scipy.stats import norm
import numpy as np
cdfarr = norm.cdf(np.array([1,-1., 0, 1, 3, 4, -2, 6]))
print(cdfarr)
```

要查找分布的中位数，可以使用百分点函数(PPF)，它是CDF的倒数。 可通过使用下面的例子来理解。

```python
from scipy.stats import norm
ppfvar = norm.ppf(0.5)
print(ppfvar)
```

要生成随机变量序列，应该使用`size`参数，如下例所示。

```python
from scipy.stats import norm
rvsvar = norm.rvs(size = 5)
print(rvsvar)
```

上述输出不可重现。 要生成相同的随机数，请使用`seed()`函数。

## 均匀分布

使用统一函数可以生成均匀分布。 参考下面的一个例子。

```python
from scipy.stats import uniform
cvar = uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)
print(cvar)
```

**构建离散分布**

生成随机样本，并将观察到的频率与概率进行比较。

**二项分布**
作为`rv_discrete`类的一个实例，`binom`对象从它继承了一个泛型方法的集合，并通过特定于这个特定分布的细节完成它们。 参考下面的例子。

```python
from scipy.stats import uniform
cvar = uniform.cdf([0, 1, 2, 3, 4, 5], loc = 1, scale = 4)

print(cvar)
```

## 描述性统计

如`Min`，`Max`，`Mean`和`Variance`等基本统计数据将NumPy数组作为输入并返回相应的结果。 下表描述了`scipy.stats`包中的一些基本统计函数。

| 编号 | 函数         | 描述                                            |
| ---- | ------------ | ----------------------------------------------- |
| 1    | `describe()` | 计算传递数组的几个描述性统计信息                |
| 2    | `gmean()`    | 计算沿指定轴的几何平均值                        |
| 3    | `hmean()`    | 计算沿指定轴的谐波平均值                        |
| 4    | `kurtosis()` | 计算峰度                                        |
| 5    | `mode()`     | 返回模态值                                      |
| 6    | `skew()`     | 测试数据的偏斜度                                |
| 7    | `f_oneway()` | 执行单向方差分析                                |
| 8    | `iqr()`      | 计算沿指定轴的数据的四分位数范围                |
| 9    | `zscore()`   | 计算样本中每个值相对于样本均值和标准偏差的`z`值 |
| 10   | `sem()`      | 计算输入数组中值的标准误差(或测量标准误差)      |

其中几个函数在`scipy.stats.mstats`中有一个类似的版本，它们用于掩码数组。 参考下面给出的例子来理解这一点。

```python
from scipy import stats
import numpy as np
x = np.array([1,2,3,4,5,6,7,8,9])
print(x.max(),x.min(),x.mean(),x.var())
```

**T-检验**

下面了解`T`检验在SciPy中是如何有用的。

**ttest_1samp**

计算一组分数平均值的`T`检验。 这是对零假设的双面检验，即独立观测值`'a'`样本的期望值(平均值)等于给定总体均值`popmean`，考虑下面的例子。

```python
from scipy import stats
rvs = stats.norm.rvs(loc = 5, scale = 10, size = (50,2))
sta = stats.ttest_1samp(rvs,5.0)
print(sta)
```

**比较两个样本**

在下面的例子中，有两个样本可以来自相同或不同的分布，想要测试这些样本是否具有相同的统计特性。

`ttest_ind` - 计算两个独立样本得分的T检验。 对于两个独立样本具有相同平均(预期)值的零假设，这是一个双侧检验。 该测试假设人口默认具有相同的差异。

如果观察到来自相同或不同人群的两个独立样本，可以使用这个测试。参考下面的例子。

```python
from scipy import stats
rvs1 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
rvs2 = stats.norm.rvs(loc = 5,scale = 10,size = 500)
print(stats.ttest_ind(rvs1,rvs2))
```

可以使用相同长度的新数组进行测试，但具有不同的含义。 在`loc`中使用不同的值并测试相同的值。
<code class=gatsby-kernelname data-language=python></code>
