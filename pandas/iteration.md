# Pandas 迭代

`Pandas`对象之间的基本迭代的行为取决于类型。当迭代一个系列时，它被视为数组式，基本迭代产生这些值。其他数据结构，如：`DataFrame`和`Panel`，遵循类似惯例迭代对象的键。

简而言之，基本迭代(对于`i`在对象中)产生 -

- *Series* - 值
- *DataFrame* - 列标签
- *Pannel* - 项目标签

## 迭代DataFrame

迭代`DataFrame`提供列名。现在来看看下面的例子来理解这个概念。

```python
import pandas as pd
import numpy as np

N=20

df = pd.DataFrame({
    'A': pd.date_range(start='2016-01-01',periods=N,freq='D'),
    'x': np.linspace(0,stop=N-1,num=N),
    'y': np.random.rand(N),
    'C': np.random.choice(['Low','Medium','High'],N).tolist(),
    'D': np.random.normal(100, 10, size=(N)).tolist()
    })

for col in df:
   print(col)
```

要遍历数据帧(DataFrame)中的行，可以使用以下函数 -

- `iteritems()` - 迭代`(key，value)`对
- `iterrows()` - 将行迭代为(索引，系列)对
- `itertuples()` - 以`namedtuples`的形式迭代行

**iteritems()示例**

将每个列作为键，将值与值作为键和列值迭代为Series对象。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns=['col1','col2','col3'])
for key,value in df.iteritems():
   print(key,value)
```

观察一下，单独迭代每个列作为系列中的键值对。

**iterrows()示例**

`iterrows()`返回迭代器，产生每个索引值以及包含每行数据的序列。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row_index,row in df.iterrows():
   print(row_index,row)
```

> 注意 - 由于`iterrows()`遍历行，因此不会跨该行保留数据类型。`0`,`1`,`2`是行索引，`col1`，`col2`，`col3`是列索引。

**itertuples()示例**

`itertuples()`方法将为`DataFrame`中的每一行返回一个产生一个命名元组的迭代器。元组的第一个元素将是行的相应索引值，而剩余的值是行值。

**示例**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])
for row in df.itertuples():
    print(row)
```

> 注意 - 不要尝试在迭代时修改任何对象。迭代是用于读取，迭代器返回原始对象(视图)的副本，因此更改将不会反映在原始对象上。

**示例代码**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(4,3),columns = ['col1','col2','col3'])

for index, row in df.iterrows():
   row['a'] = 10
print(df)
```

注意观察结果，修改变化并未反映出来。