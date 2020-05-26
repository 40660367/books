# Pandas 函数应用(apply)			

要将自定义或其他库的函数应用于*Pandas*对象，有三个重要的方法，下面来讨论如何使用这些方法。使用适当的方法取决于函数是否期望在整个`DataFrame`，行或列或元素上进行操作。

- 表合理函数应用：`pipe()`
- 行或列函数应用：`apply()`
- 元素函数应用：`applymap()`

## 表格函数应用

可以通过将函数和适当数量的参数作为管道参数来执行自定义操作。 因此，对整个`DataFrame`执行操作。

例如，为`DataFrame`中的所有元素相加一个值`2`。

**adder 函数**

`adder`函数将两个数值作为参数相加并返回总和。

```python
def adder(ele1,ele2):
    return ele1+ele2
```

现在将使用自定义函数对DataFrame进行操作。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
```

下面来看看完整的程序 -

```python
import pandas as pd
import numpy as np

def adder(ele1,ele2):
   return ele1+ele2

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.pipe(adder,2)
df
```

## 行或列合理函数应用

可以使用`apply()`方法沿`DataFrame`或`Panel`的轴应用任意函数，它与描述性统计方法一样，采用可选的`axis`参数。 默认情况下，操作按列执行，将每列列为数组。

**示例**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean)
df
```

通过传递`axis`参数，可以在行上执行操作。

**示例-2**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(np.mean,axis=1)
df
```

**示例-3**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.apply(lambda x: x.max() - x.min())
df
```

## 元素合理函数应用

并不是所有的函数都可以向量化(也不是返回另一个数组的`NumPy`数组，也不是任何值)，在`DataFrame`上的方法`applymap()`和类似于在Series上的`map()`接受任何Python函数，并且返回单个值。

**示例-1**

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])

# My custom function
df['col1'].map(lambda x:x*100)
df
```

**示例-2**

```python
import pandas as pd
import numpy as np

# My custom function
df = pd.DataFrame(np.random.randn(5,3),columns=['col1','col2','col3'])
df.applymap(lambda x:x*100)
df
```

