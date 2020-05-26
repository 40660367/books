# Scipy 特殊包(special)

特殊包中可用的功能是通用功能，它遵循广播和自动数组循环。

下面来看看一些最常用的特殊函数功能 -

- 立方根函数
- 指数函数
- 相对误差指数函数
- 对数和指数函数
- 兰伯特函数
- 排列和组合函数
- 伽马函数

下面来简单地了解这些函数。

**立方根函数**

这个立方根函数的语法是 - `scipy.special.cbrt(x)`。 这将获取`x`的基于元素的立方体根。

参考下面的一个例子 - 

```python
from scipy.special import cbrt
res = cbrt([10, 9, 0.1254, 234])
print(res)
```

**指数函数**

指数函数的语法是 - `scipy.special.exp10(x)`。 这将计算`10 ** x`的值。

参考下面的一个例子 - 

```python
from scipy.special import exp10
res = exp10([2, 4])
print(res)
```

**相对误差指数函数**

这个函数的语法是 - `scipy.special.exprel(x)`。 它生成相对误差指数，`(exp(x) - 1/x`。

当`x`接近零时，`exp(x)`接近`1`，所以`exp(x)-1`的数值计算可能遭受灾难性的精度损失。 然后`exprel(x)`被实现以避免精度的损失，这在`x`接近于零时发生。

参考下面的一个例子。

```python
from scipy.special import exprel
res = exprel([-0.25, -0.1, 0, 0.1, 0.25])
print(res)
```

**对数和指数函数**

这个函数的语法是 - `scipy.special.logsumexp(x)`。 它有助于计算输入元素指数总和的对数。

参考下面的一个例子 - 

```python
from scipy.special import logsumexp
import numpy as np
a = np.arange(10)
res = logsumexp(a)
print(res)
```

**兰伯特函数**

这个函数的语法是 - `scipy.special.lambertw(x)`。 它也被称为兰伯特W函数。 兰伯特W函数`W(z)`定义为`w * exp(w)`的反函数。 换句话说，对于任何复数`z`，`W(z)`的值都是`z = W(z)* exp(W(z))`。

兰伯特W函数是一个具有无限多分支的多值函数。 每个分支给出了方程`z = w exp(w)`的单独解。 这里，分支由整数k索引。

参考下面的一个例子。 这里，兰伯特W函数是`w exp(w)`的逆函数。

```python
from scipy.special import lambertw
w = lambertw(1)
print(w)
print(w * np.exp(w))
```

**排列和组合**

下面将分开讨论排列和组合，以便清楚地理解它们。

**组合** - 组合函数的语法是 - `scipy.special.comb(N，k)`。参考下面的一个例子 -

```python
from scipy.special import comb
res = comb(10, 3, exact = False,repetition=True)
print(res)
```

> 注 - 数组参数仅适用于`exact = False`大小写。 如果`k> N`，`N <0`或`k <0`，则返回`0`。

**排列** - 组合函数的语法是 - `scipy.special.perm(N，k)`。 一次取`k`个`N`个东西的排列，即`N`个`k`个排列。这也被称为“部分排列”。

参考下面的一个例子。

```python
from scipy.special import perm
res = perm(10, 3, exact = True)
print(res)
```

**伽马函数**
由于`z * gamma(z)= gamma(z + 1)`和`gamma(n + 1)= n！`，所以对于自然数`'n'`，伽马函数通常被称为广义阶乘。

组合函数的语法是 - `scipy.special.gamma(x)`。 一次取`k`个`N`个东西的排列，即`N`个`k`个排列。这也被称为“部分排列”。

组合函数的语法是 - `scipy.special.gamma(x)`。 一次取`k`个`N`个东西的排列，即`N`个`k`个排列。这也被称为“部分排列”。

```python
from scipy.special import gamma
res = gamma([0, 0.5, 1, 5])
print(res)
```
<code class=gatsby-kernelname data-language=python></code>
