# Scipy 插值(interpolate)

在本章中，我们将讨论插值，及如何在SciPy中使用它。

## 插值是什么？

插值是在直线或曲线上的两点之间找到值的过程。 为了帮助记住它的含义，我们应该将“inter”这个词的第一部分想象为“输入”，表示要查看原来数据的“内部”。 这种插值工具不仅适用于统计学，而且在科学，商业或需要预测两个现有数据点内的值时也很有用。

下面创建一些数据，看看如何使用`scipy.interpolate`包进行插值。

```python
%matplotlib inline
import numpy as np
from scipy import interpolate
import matplotlib.pyplot as plt

x = np.linspace(0, 4, 12)
y = np.cos(x**2/3+4)
print(x,y)
```

现在，有两个数组。 假设这两个数组作为空间点的两个维度，使用下面的程序进行绘图，并看看它们的样子。

```python
plt.plot(x, y,’o’)
plt.show()
```

## 一维插值

`scipy.interpolate`中的`interp1d`类是一种创建基于固定数据点的函数的便捷方法，可以使用线性插值在给定数据定义的域内的任意位置评估该函数。

通过使用上述数据，创建一个插值函数并绘制一个新的插值图。

```python
f1 = interp1d(x, y,kind = 'linear')
f2 = interp1d(x, y, kind = 'cubic')
```

使用`interp1d`函数，创建了两个函数`f1`和`f2`。 这些函数对于给定的输入`x`返回`y`。 第三种变量类型表示插值技术的类型。 ‘线性’，’最近’，’零’，’线性’，’二次’，’立方’是一些插值技术。

现在，创建更多长度的新输入以查看插值的明显区别。 对新数据使用旧数据的相同功能。

```python
xnew = np.linspace(0, 4,30)
plt.plot(x, y, 'o', xnew, f1(xnew), '-', xnew, f2(xnew), '--')
plt.legend(['data', 'linear', 'cubic','nearest'], loc = 'best')
plt.show()
```

## 样条曲线

为了通过数据点画出平滑的曲线，绘图员曾经使用薄的柔性木条，硬橡胶，金属或塑料称为机械样条。 为了使用机械花键，在设计中沿着曲线明确选择了一些销钉，然后将花键弯曲，以便它们接触到每个销钉。

显然，在这种结构下，样条曲线在这些引脚上插入曲线。 它可以用来在其他图纸中重现曲线。 引脚所在的点称为结。 可以通过调整结点的位置来改变样条线所定义的曲线的形状。

**单变量样条**

一维平滑样条拟合一组给定的数据点。 `Scipy.interpolate`中的`UnivariateSpline`类是创建基于固定数据点类的函数的便捷方法 - `scipy.interpolate.UnivariateSpline(x，y，w = None，bbox = [None，None]，k = 3，s = None，ext = 0，check_finite = False)`。

下面来看看一个例子。

```python
%matplotlib inline
import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
x = np.linspace(-3, 3, 50)
y = np.exp(-x**2) + 0.1 * np.random.randn(50)
plt.plot(x, y, 'ro', ms = 5)
plt.show()
```

使用平滑参数的默认值。

```python
spl = UnivariateSpline(x, y)
xs = np.linspace(-3, 3, 1000)
plt.plot(xs, spl(xs), 'g', lw = 3)
plt.show()
```

手动更改平滑量。

```python
spl.set_smoothing_factor(0.5)
plt.plot(xs, spl(xs), 'b', lw = 3)
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
