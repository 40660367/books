# Pandas 数据帧(DataFrame)	

数据帧(DataFrame)是二维数据结构，即数据以行和列的表格方式排列。

数据帧(DataFrame)的功能特点：

- 潜在的列是不同的类型
- 大小可变
- 标记轴(行和列)
- 可以对行和列执行算术运算

**结构体**

假设要创建一个包含学生数据的数据帧。参考以下图示 - 

![img](../images/dataframe.jpg)

可以将上图表视为SQL表或电子表格数据表示。

## pandas.DataFrame

*pandas*中的`DataFrame`可以使用以下构造函数创建 -

```
pandas.DataFrame( data, index, columns, dtype, copy)
```

构造函数的参数如下 -  

| 编号 | 参数      | 描述                                                         |
| ---- | --------- | ------------------------------------------------------------ |
| 1    | `data`    | 数据采取各种形式，如:`ndarray`，`series`，`map`，`lists`，`dict`，`constant`和另一个`DataFrame`。 |
| 2    | `index`   | 对于行标签，要用于结果帧的索引是可选缺省值`np.arrange(n)`，如果没有传递索引值。 |
| 3    | `columns` | 对于列标签，可选的默认语法是 - `np.arange(n)`。 这只有在没有索引传递的情况下才是这样。 |
| 4    | `dtype`   | 每列的数据类型。                                             |
| 5    | `copy`    | 如果默认值为`False`，则此命令(或任何它)用于复制数据。        |

## 创建DataFrame

Pandas数据帧(*DataFrame*)可以使用各种输入创建，如 - 

- 列表
- 字典
- 系列
- Numpy ndarrays
- 另一个数据帧(*DataFrame*)

在本章的后续章节中，我们将看到如何使用这些输入创建数据帧(*DataFrame*)。

## 创建一个空的DataFrame

创建基本数据帧是空数据帧。
**示例**

```python
#import the pandas library and aliasing as pd
import pandas as pd
df = pd.DataFrame()
df
```

## 从列表创建DataFrame

可以使用单个列表或列表列表创建数据帧(*DataFrame*)。

**实例-1**

```python
import pandas as pd
data = [1,2,3,4,5]
df = pd.DataFrame(data)
df
```

**实例-2**

```python
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'])
df
```

**实例-3**

```python
import pandas as pd
data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['Name','Age'],dtype=float)
df
```

> 注意 - 可以观察到，`dtype`参数将`Age`列的类型更改为浮点。

## 从ndarrays/Lists的字典来创建DataFrame

所有的`ndarrays`必须具有相同的长度。如果传递了索引(`index`)，则索引的长度应等于数组的长度。

如果没有传递索引，则默认情况下，索引将为`range(n)`，其中`n`为数组长度。

**实例-1**

```python
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data)
df
```

> 注 - 观察值`0`,`1`,`2`,`3`。它们是分配给每个使用函数`range(n)`的默认索引。

**示例-2**

使用数组创建一个索引的数据帧(*DataFrame*)。

```python
import pandas as pd
data = {'Name':['Tom', 'Jack', 'Steve', 'Ricky'],'Age':[28,34,29,42]}
df = pd.DataFrame(data, index=['rank1','rank2','rank3','rank4'])
df
```

> 注意 - `index`参数为每行分配一个索引。

## 从列表创建数据帧DataFrame

字典列表可作为输入数据传递以用来创建数据帧(*DataFrame*)，字典键默认为列名。

**实例-1**

以下示例显示如何通过传递字典列表来创建数据帧(*DataFrame*)。

```python
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data)
df
```

> 注意 - 观察到，NaN(不是数字)被附加在缺失的区域。

**示例-2**

以下示例显示如何通过传递字典列表和行索引来创建数据帧(*DataFrame*)。

```python
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]
df = pd.DataFrame(data, index=['first', 'second'])
df
```

**实例-3**

以下示例显示如何使用字典，行索引和列索引列表创建数据帧(*DataFrame*)。

```python
import pandas as pd
data = [{'a': 1, 'b': 2},{'a': 5, 'b': 10, 'c': 20}]

#With two column indices, values same as dictionary keys
df1 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b'])

#With two column indices with one index with other name
df2 = pd.DataFrame(data, index=['first', 'second'], columns=['a', 'b1'])

print(df1)
print(df2)
```

> 注意 - 观察，`df2`使用字典键以外的列索引创建`DataFrame`; 因此，附加了NaN到位置上。 而`df1`是使用列索引创建的，与字典键相同，所以也附加了NaN。

## 从系列的字典来创建DataFrame

字典的系列可以传递以形成一个DataFrame。 所得到的索引是通过的所有系列索引的并集。

**示例**

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df
```

> 注意 - 对于第一个系列，观察到没有传递标签`'d'`，但在结果中，对于`d`标签，附加了NaN。

现在通过实例来了解列选择，添加和删除。

### 列选择

下面将通过从数据帧(DataFrame)中选择一列。

示例

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
df['one']
```

### 列添加

下面将通过向现有数据框添加一个新列来理解这一点。

**示例**

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
      'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)

# Adding a new column to an existing DataFrame object with column label by passing new series

print("Adding a new column by passing as Series:")
df['three']=pd.Series([10,20,30],index=['a','b','c'])
print(df)

print("Adding a new column using the existing columns in DataFrame:")
df['four']=df['one']+df['three']
print(df)
```

### 列删除

列可以删除或弹出; 看看下面的例子来了解一下。

**例子**

```python
# Using the previous DataFrame, we will delete a column
# using del function
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd']), 
     'three' : pd.Series([10,20,30], index=['a','b','c'])}

df = pd.DataFrame(d)
print("Our dataframe is:")
print(df)

# using del function
print("Deleting the first column using DEL function:")
del df['one']
print(df)

# using pop function
print("Deleting another column using POP function:")
df.pop('two')
print(df)
```

## 行选择，添加和删除

现在将通过下面实例来了解行选择，添加和删除。我们从选择的概念开始。

**标签选择**

可以通过将行标签传递给`loc()`函数来选择行。参考以下示例代码 - 

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.loc['b'])
```

结果是一系列标签作为`DataFrame`的列名称。 而且，系列的名称是检索的标签。

**按整数位置选择**

可以通过将整数位置传递给`iloc()`函数来选择行。参考以下示例代码 - 

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']),
     'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df.iloc[2])
```

## 行切片

可以使用`:`运算符选择多行。参考以下示例代码 - 

```python
import pandas as pd

d = {'one' : pd.Series([1, 2, 3], index=['a', 'b', 'c']), 
    'two' : pd.Series([1, 2, 3, 4], index=['a', 'b', 'c', 'd'])}

df = pd.DataFrame(d)
print(df[2:4])
```

**附加行**

使用`append()`函数将新行添加到DataFrame。 此功能将附加行结束。

```python
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)
print(df[2:4])
```

**删除行**

使用索引标签从DataFrame中删除或删除行。 如果标签重复，则会删除多行。

如果有注意，在上述示例中，有标签是重复的。这里再多放一个标签，看看有多少行被删除。

```python
import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

print(df)
print(df2)

import pandas as pd

df = pd.DataFrame([[1, 2], [3, 4]], columns = ['a','b'])
df2 = pd.DataFrame([[5, 6], [7, 8]], columns = ['a','b'])

df = df.append(df2)

# Drop rows with label 0
df = df.drop(0)

print(df[2:4])
```

在上面的例子中，一共有两行被删除，因为这两行包含相同的标签`0`。