# Scipy 优化算法(optimize) 			

`scipy.optimize`包提供了几种常用的优化算法。 该模块包含以下几个方面 -

- 使用各种算法(例如BFGS，Nelder-Mead单纯形，牛顿共轭梯度，COBYLA或SLSQP)的无约束和约束最小化多元标量函数(`minimize()`)
- 全局(蛮力)优化程序(例如，`anneal()`，`basinhopping()`)
- 最小二乘最小化(`leastsq()`)和曲线拟合(`curve_fit()`)算法
- 标量单变量函数最小化(`minim_scalar()`)和根查找(`newton()`)
- 使用多种算法(例如，Powell，Levenberg-Marquardt混合或Newton-Krylov等大规模方法)的多元方程系统求解(root)

**多变量标量函数的无约束和约束最小化**

`minimize()`函数为`scipy.optimize`中的多变量标量函数提供了无约束和约束最小化算法的通用接口。 为了演示最小化函数，考虑使`NN`变量的`Rosenbrock`函数最小化的问题 
$$
f(x)=\sum_{i=1}^{N-1}100(x_i-x^2_{i-1})
$$
这个函数的最小值是`0`，当`xi = 1`时达到。

## Nelder–Mead单纯形算法

在下面的例子中，`minimize()`例程与Nelder-Mead单纯形算法(`method ='Nelder-Mead'`)一起使用(通过方法参数选择)。参考下面的例子。

```python
import numpy as np
from scipy.optimize import minimize

def rosen(x):

x0 = np.array([1.3, 0.7, 0.8, 1.9, 1.2])
res = minimize(rosen, x0, method='nelder-mead')

print(res.x)
```

简单算法只需要函数评估，对于简单的最小化问题是一个不错的选择。 但是，由于它不使用任何梯度评估，因此可能需要较长时间才能找到最小值。

另一种只需要函数调用来寻找最小值的优化算法就是鲍威尔方法，它可以通过在`minimize()`函数中设置`method ='powell'`来实现。

## 　最小二乘

求解一个带有变量边界的非线性最小二乘问题。 给定残差`f(x)`(n个实变量的m维实函数)和损失函数`rho(s)`(标量函数)，最小二乘法找到代价函数`F(x)`的局部最小值。 看看下面的例子。

在这个例子中，`Rosenbrock`函数的最小值不受自变量的限制。

```python
#Rosenbrock Function
def fun_rosenbrock(x):
   return np.array([10 * (x[1] - x[0]**2), (1 - x[0])])

from scipy.optimize import least_squares
input = np.array([2, 2])
res = least_squares(fun_rosenbrock, input)

print(res)
```

请注意，我们只提供残差的向量。 该算法将成本函数构造为残差的平方和，这给出了`Rosenbrock()`函数。 确切的最小值是`x = [1.0,1.0]`。

## 求根

让我们了解求根如何在SciPy中使用。

**标量函数**

如果有一个单变量方程，则可以尝试四种不同的寻根算法。 这些算法中的每一个都需要预期根的时间间隔的端点(因为函数会改变符号)。 一般来说，`brentq`是最好的选择，但其他方法可能在某些情况下或学术目的有用。

**定点求解**

与找到函数零点密切相关的问题是找到函数的固定点的问题。 函数的固定点是函数评估返回点的点:`g(x)= x`。 显然，`gg`的不动点是`f(x)= g(x)-x`的根。 等价地，`ff`的根是`g(x)= f(x)+ x`的固定点。 例程`fixed_point`提供了一个简单的迭代方法，使用`Aitkens`序列加速度来估计`gg`的固定点，如果给出起点的话。

**方程组**
使用`root()`函数可以找到一组非线性方程的根。 有几种方法可供选择，其中`hybr`(默认)和`lm`分别使用`Powell`的混合方法和`MINPACK`中的Levenberg-Marquardt方法。

下面的例子考虑了单变量超越方程。
$$
x^2+2cos(x)=0
$$
其根可以求解如下 -

```python
import numpy as np
from scipy.optimize import root
def func(x):
   return x*2 + 2 * np.cos(x)
sol = root(func, 0.3)
print(sol)
```
<code class=gatsby-kernelname data-language=python></code>
