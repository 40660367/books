# Scipy 积分(integrate)

当一个函数不能被分析积分，或者很难分析积分时，通常会转向数值积分方法。 SciPy有许多用于执行数值积分的程序。 它们中的大多数都在同一个`scipy.integrate`库中。 下表列出了一些常用函数。

| 编号 | 示例         | 描述                   |
| ---- | ------------ | ---------------------- |
| 1    | `quad`       | 单积分                 |
| 2    | `dblquad`    | 二重积分               |
| 3    | `tplquad`    | 三重积分               |
| 4    | `nquad`      | n倍多重积分            |
| 5    | `fixed_quad` | 高斯积分，阶数`n`      |
| 6    | `quadrature` | 高斯正交到容差         |
| 7    | `romberg`    | Romberg积分            |
| 8    | `trapz`      | 梯形规则               |
| 9    | `cumtrapz`   | 梯形法则累计计算积分   |
| 10   | `simps`      | 辛普森的规则           |
| 11   | `romb`       | Romberg积分            |
| 12   | `polyint`    | 分析多项式积分(NumPy)  |
| 13   | `poly1d`     | 辅助函数polyint(NumPy) |

## 单积分

Quad函数是SciPy积分函数的主力。 数值积分有时称为正交积分，因此称为名称。 它通常是在`a`到`b`给定的固定范围内执行函数`f(x)`的单个积分的默认选择。
$$
\int_a^b{f(x)dx}
$$


`quad`的一般形式是`scipy.integrate.quad(f，a，b)`，其中`'f'`是要积分的函数的名称。 而`'a'`和`'b'`分别是下限和上限。 下面来看看一个高斯函数的例子，它的积分范围是`0`和`1`。

首先需要定义这个函数:
$$
f(x)=e^{-x^{2}}
$$
这可以使用`lambda`表达式完成，然后在该函数上调用四方法。

```python
import scipy.integrate
from numpy import exp
f= lambda x:exp(-x**2)
i = scipy.integrate.quad(f, 0, 1)
print(i)
```

四元函数返回两个值，其中第一个数字是积分值，第二个数值是积分值绝对误差的估计值。

> 注 - 由于`quad`需要函数作为第一个参数，因此不能直接将`exp`作为参数传递。 Quad函数接受正和负无穷作为限制。 Quad函数可以积分单个变量的标准预定义NumPy函数，如`exp`，`sin`和`cos`。

## 多重积分

双重和三重积分的机制已被包含到函数`dblquad`，`tplquad`和`nquad`中。 这些函数分别积分了四个或六个参数。 所有内积分的界限都需要定义为函数。

## 双重积分

`dblquad`的一般形式是`scipy.integrate.dblquad(func，a，b，gfun，hfun)`。 其中，`func`是要积分函数的名称，`'a'`和`'b'`分别是`x`变量的下限和上限，而`gfun`和`hfun`是定义变量`y`的下限和上限的函数名称。

看看一个执行双重积分方法的示例。
$$
\int_0^{1/2}dy\int_0^{\sqrt{1-4y^2}}16xydx
$$
使用`lambda`表达式定义函数`f`，`g`和`h`。 请注意，即使`g`和`h`是常数，它们可能在很多情况下必须定义为函数，正如在这里为下限所做的那样。

```python
import scipy.integrate
from numpy import exp
from math import sqrt
f = lambda x, y : 16*x*y
g = lambda x : 0
h = lambda y : sqrt(1-4*y**2)
i = scipy.integrate.dblquad(f, 0, 0.5, g, h)
print(i)
```

除上述例程外，`scipy.integrate`还有许多其他积分的程序，其中包括执行`n`次多重积分的nquad以及实现各种集成算法的其他例程。 但是，`quad`和`dblquad`将满足对数值积分的大部分需求。
<code class=gatsby-kernelname data-language=python></code>
