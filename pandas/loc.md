# Pandas 索引和选择数据

在本章中，我们将讨论如何切割和丢弃日期，并获取*Pandas*中大对象的子集。

Python和NumPy索引运算符`"[]"`和属性运算符`"."`。 可以在广泛的用例中快速轻松地访问*Pandas*数据结构。然而，由于要访问的数据类型不是预先知道的，所以直接使用标准运算符具有一些优化限制。对于生产环境的代码，我们建议利用本章介绍的优化*Pandas*数据访问方法。

*Pandas*现在支持三种类型的多轴索引; 这三种类型在下表中提到 -

| 编号 | 索引      | 描述           |
| ---- | --------- | -------------- |
| 1    | `.loc()`  | 基于标签       |
| 2    | `.iloc()` | 基于整数       |
| 3    | `.ix()`   | 基于标签和整数 |

## .loc()

*Pandas*提供了各种方法来完成基于标签的索引。 切片时，也包括起始边界。整数是有效的标签，但它们是指标签而不是位置。

`.loc()`具有多种访问方式，如 -

- 单个标量标签
- 标签列表
- 切片对象
- 一个布尔数组

`loc`需要两个单/列表/范围运算符，用`","`分隔。第一个表示行，第二个表示列。

**示例1**

```python
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

#select all rows for a specific column
print(df.loc[:,'A'])
```

**示例2**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])
```

**示例3**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select few rows for multiple columns, say list[]
print(df.loc[['a','b','f','h'],['A','C']])
# Select all rows for multiple columns, say list[]
print(df.loc[:,['A','C']])
```

**示例4**

```python
# import the pandas library and aliasing as pd
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# Select range of rows for all columns
print(df.loc['a':'h'])
```

**示例5**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4),
index = ['a','b','c','d','e','f','g','h'], columns = ['A', 'B', 'C', 'D'])

# for getting values with a boolean array
print(df.loc['a']>0)
```

## .iloc()

*Pandas*提供了各种方法，以获得纯整数索引。像python和numpy一样，第一个位置是基于`0`的索引。

各种访问方式如下 -

- 整数
- 整数列表
- 系列值

**示例1**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# select all rows for a specific column
print(df.iloc[:4])
```

**示例2**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print(df.iloc[:4])
print(df.iloc[1:5, 2:4])
```

**示例3**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Slicing through list of values
print(df.iloc[[1, 3, 5], [1, 3]])
print(df.iloc[1:3, :])
print(df.iloc[:,1:3])
```

## .ix()

除了基于纯标签和整数之外，*Pandas*还提供了一种使用`.ix()`运算符进行选择和子集化对象的混合方法。

**示例1**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

# Integer slicing
print(df.ix[:4])
```

**示例2**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
# Index slicing
print(df.ix[:,'A'])
```

## 使用符号

使用多轴索引从Pandas对象获取值可使用以下符号 -

| 对象      | 索引                                         | 描述                                       |
| --------- | -------------------------------------------- | ------------------------------------------ |
| Series    | `s.loc[indexer]`                             | 标量值                                     |
| DataFrame | `df.loc[row_index,col_index]`                | 标量对象                                   |
| Panel     | `p.loc[item_index,major_index, minor_index]` | p.loc[item_index,major_index, minor_index] |

> 注意 - `.iloc()`和`.ix()`应用相同的索引选项和返回值。

现在来看看如何在DataFrame对象上执行每个操作。这里使用基本索引运算符`[]` -

**示例1**

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print(df['A'])
```

**示例2**

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print(df[['A','B']])
```

**示例3**

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])
print(df[2:2])
```

## 属性访问

可以使用属性运算符`.`来选择列。

**示例**

```python
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(8, 4), columns = ['A', 'B', 'C', 'D'])

print(df.A)
```

