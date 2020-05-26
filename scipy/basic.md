# Scipy 基本功能

默认情况下，所有的NumPy函数都可以通过SciPy命名空间获得。 当导入SciPy时，不需要显式导入NumPy函数。 NumPy的主要目标是均匀多维数组。 它是一个元素表(通常是数字)，都是相同类型，由正整数的元组索引。 在NumPy中，大小(尺寸)被称为轴。 轴的数量称为等级。

现在，让修改NumPy中的Vectors和Matrices的基本功能。 由于SciPy构建在NumPy数组之上，因此需要了解NumPy基础知识。 由于线性代数的大多数部分只处理矩阵。

**NumPy向量**

向量(Vector)可以通过多种方式创建。 其中一些描述如下。

将Python数组类对象转换为NumPy中的数组，看看下面的例子。

```python
import numpy as np
list = [1,2,3,4]
arr = np.array(list)
print(arr)
```

## 内在NumPy数组创建

NumPy有从头开始创建数组的内置函数。 其中一些函数解释如下。

**使用zeros()**

`zeros(shape)`函数将创建一个用指定形状(shape)填充`0`值的数组。 默认`dtype`是`float64`。 看看下面的例子。

```python
import numpy as np
print(np.zeros((2, 3)))
```

**使用ones()**

`ones(shape)`函数将创建一个填充`1`值的数组。 它在所有其他方面与`0`相同。 看看下面的例子。

```python
import numpy as np
print(np.ones((2, 3)))
```

**使用arange()**

`arange()`函数将创建具有有规律递增值的数组。 看看下面的例子。

```python
import numpy as np
print(np.arange(7))
```

**定义值的数据类型**

看看下面一段示例代码 - 

```python
import numpy as np
arr = np.arange(2, 10, dtype = np.float)
print(arr)
print()"Array Data Type :",arr.dtype)
```

**使用linspace()**

`linspace()`函数将创建具有指定数量元素的数组，这些元素将在指定的开始值和结束值之间平均间隔。 看看下面的例子。

```python
import numpy as np
print(np.linspace(1., 4., 6))
```

## 矩阵

矩阵是一个专门的二维数组，通过操作保留其`2-D`特性。 它有一些特殊的运算符，如`*`(矩阵乘法)和`**`(矩阵幂值)。 看看下面的例子。

```python
import numpy as np
print(np.matrix('1 2; 3 4'))
```

**矩阵的共轭转置**

此功能返回自我的(复数)共轭转置。 看看下面的例子。

```python
import numpy as np
mat = np.matrix('1 2; 3 4')
print(mat.H)
```

**矩阵的转置**

此功能返回自身的转置。看看下面的例子。

```python
import numpy as np
mat = np.matrix('1 2; 3 4')
print(mat.T)
```

当转置一个矩阵时，我们创建一个新的矩阵，其行是原始的列。 另一方面，共轭转置为每个矩阵元素交换行和列索引。 矩阵的逆矩阵是一个矩阵，如果与原始矩阵相乘，则产生一个单位矩阵。
<code class=gatsby-kernelname data-language=python></code>
