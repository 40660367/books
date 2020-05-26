# Pandas 序列(series)	

序列(`Series`)是能够保存任何类型的数据(整数，字符串，浮点数，Python对象等)的一维标记数组。轴标签统称为索引。

## pandas.Series

*Pandas*序列可以使用以下构造函数创建 -

```
pandas.Series( data, index, dtype, copy)。
```

构造函数的参数如下 -

| 编号 | 参数    | 描述                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| 1    | `data`  | 数据采取各种形式，如：`ndarray`，`list`，`constants`         |
| 2    | `index` | 索引值必须是唯一的和散列的，与数据的长度相同。 默认`np.arange(n)`如果没有索引被传递。 |
| 3    | `dtype` | `dtype`用于数据类型。如果没有，将推断数据类型                |
| 4    | `copy`  | 复制数据，默认为`false`。                                    |

可以使用各种输入创建一个序列，如 -

- 数组
- 字典
- 标量值或常数

## 创建一个空的序列

创建一个基本序列是一个空序列。

**示例**

```python
#import the pandas library and aliasing as pd
import pandas as pd
s = pd.Series()
s
```

## 从ndarray创建一个序列

如果数据是`ndarray`，则传递的索引必须具有相同的长度。 如果没有传递索引值，那么默认的索引将是范围(`n`)，其中`n`是数组长度，即`[0,1,2,3…. range(len(array))-1] - 1]`。

**示例1**

```python
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data)
s
```

这里没有传递任何索引，因此默认情况下，它分配了从`0`到`len(data)-1`的索引，即：`0`到`3`。

**示例2**

```python
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = np.array(['a','b','c','d'])
s = pd.Series(data,index=[100,101,102,103])
s
```

在这里传递了索引值。现在可以在输出中看到自定义的索引值。

## 从字典创建一个序列

字典(`dict`)可以作为输入传递，如果没有指定索引，则按排序顺序取得字典键以构造索引。 如果传递了索引，索引中与标签对应的数据中的值将被拉出。

**示例2**

```python
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data)
s
```

> 注意 - 字典键用于构建索引。

**示例**

```python
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
data = {'a' : 0., 'b' : 1., 'c' : 2.}
s = pd.Series(data,index=['b','c','d','a'])
s
```

> 注意观察 - 索引顺序保持不变，缺少的元素使用NaN(不是数字)填充。

## 从标量创建一个序列

如果数据是标量值，则必须提供索引。将重复该值以匹配索引的长度。

```python
#import the pandas library and aliasing as pd
import pandas as pd
import numpy as np
s = pd.Series(5, index=[0, 1, 2, 3])
s
```

## 从具有位置的序列中访问数据

序列中的数据可以使用类似于访问`ndarray`中的数据来访问。

**示例-1**

检索第一个元素。比如已经知道数组从零开始计数，第一个元素存储在零位置等等。

```python
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first element
s[0]
```

**示例-2**

检索序列中的前三个元素。 如果`a:`被插入到其前面，则将从该索引向前的所有项目被提取。 如果使用两个参数(使用它们之间)，两个索引之间的项目(不包括停止索引)。

```python
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the first three element
s[:3]
```

**示例-3**

检索最后三个元素，参考以下示例代码 - 

```python
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve the last three element
s[-3:]
```

## 使用标签检索数据(索引)

一个序列就像一个固定大小的字典，可以通过索引标签获取和设置值。

**示例1**

使用索引标签值检索单个元素。

```python
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve a single element
s['a']
```

**示例2**

使用索引标签值列表检索多个元素。

```python
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
print(s[['a','c','d']])
```

**示例3**

如果不包含标签，则会出现异常。

```python
import pandas as pd
s = pd.Series([1,2,3,4,5],index = ['a','b','c','d','e'])

#retrieve multiple elements
s['f']
```