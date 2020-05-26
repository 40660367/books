# Pandas 基本功能	

到目前为止，我们了解了两种种*Pandas*数据结构以及如何创建它们。接下来将主要关注数据帧(DataFrame)对象，因为它在实时数据处理中非常重要，并且还讨论其他数据结构。

## 系列基本功能

| 编号 | 属性或方法 | 描述                                |
| ---- | ---------- | ----------------------------------- |
| 1    | `axes`     | 返回行轴标签列表。                  |
| 2    | `dtype`    | 返回对象的数据类型(`dtype`)。       |
| 3    | `empty`    | 如果系列为空，则返回`True`。        |
| 4    | `ndim`     | 返回底层数据的维数，默认定义：`1`。 |
| 5    | `size`     | 返回基础数据中的元素数。            |
| 6    | `values`   | 将系列作为`ndarray`返回。           |
| 7    | `head()`   | 返回前`n`行。                       |
| 8    | `tail()`   | 返回最后`n`行。                     |

现在创建一个系列并演示如何使用上面所有列出的属性操作。

**示例**

```python
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
s
```

**axes示例**

返回系列的标签列表。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print("The axes are:")
s.axes
```

上述结果是从`0`到`5`的值列表的紧凑格式，即：`[0,1,2,3,4]`。

**empty示例**

返回布尔值，表示对象是否为空。返回`True`则表示对象为空。

```python
import pandas as pd
import numpy as np

#Create a series with 100 random numbers
s = pd.Series(np.random.randn(4))
print("Is the Object empty?")
s.empty
```

**ndim示例**

返回对象的维数。根据定义，一个系列是一个`1D`数据结构，参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print(s)

print("The dimensions of the object:")
print(s.ndim)
```

**size示例**

返回系列的大小(长度)。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(2))
print(s)
print("The size of the object:")
print(s.size)
```

**values示例**

以数组形式返回系列中的实际数据值。

```python
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print(s)

print("The actual data series is:")
print(s.values)
```

**head()和tail()方法示例**

要查看Series或DataFrame对象的小样本，请使用`head()`和`tail()`方法。

`head()`返回前`n`行(观察索引值)。要显示的元素的默认数量为`5`，但可以传递自定义这个数字值。

```python
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print("The original series is:")
print(s)

print("The first two rows of the data series:")
print(s.head(2))
```

`tail()`返回最后`n`行(观察索引值)。 要显示的元素的默认数量为`5`，但可以传递自定义数字值。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a series with 4 random numbers
s = pd.Series(np.random.randn(4))
print("The original series is:")
print(s)

print("The last two rows of the data series:")
print(s.tail(2))
```

## DataFrame基本功能

下面来看看数据帧(DataFrame)的基本功能有哪些？下表列出了DataFrame基本功能的重要属性或方法。

| 编号 | 属性或方法 | 描述                                                         |
| ---- | ---------- | ------------------------------------------------------------ |
| 1    | `T`        | 转置行和列。                                                 |
| 2    | `axes`     | 返回一个列，行轴标签和列轴标签作为唯一的成员。               |
| 3    | `dtypes`   | 返回此对象中的数据类型(`dtypes`)。                           |
| 4    | `empty`    | 如果`NDFrame`完全为空[无项目]，则返回为`True`; 如果任何轴的长度为`0`。 |
| 5    | `ndim`     | 轴/数组维度大小。                                            |
| 6    | `shape`    | 返回表示`DataFrame`的维度的元组。                            |
| 7    | `size`     | `NDFrame`中的元素数。                                        |
| 8    | `values`   | NDFrame的Numpy表示。                                         |
| 9    | `head()`   | 返回开头前`n`行。                                            |
| 10   | `tail()`   | 返回最后`n`行。                                              |

下面来看看如何创建一个DataFrame并使用上述属性和方法。

**示例**

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our data series is:")
df
```

**T(转置)示例**

返回`DataFrame`的转置。行和列将交换。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

# Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

# Create a DataFrame
df = pd.DataFrame(d)
print("The transpose of the data series is:")
df.T
```

**axes示例**

返回行轴标签和列轴标签列表。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Row axis labels and column axis labels are:")
df.axes
```

**dtypes示例**

返回每列的数据类型。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("The data types of each column are:")
df.dtypes
```

**empty示例**

返回布尔值，表示对象是否为空; 返回`True`表示对象为空。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Is the object empty?")
print(df.empty)
```

**ndim示例**

返回对象的维数。根据定义，DataFrame是一个`2D`对象。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our object is:")
print(df)
print("The dimension of the object is:")
print(df.ndim)
```

**shape示例**

返回表示`DataFrame`的维度的元组。 元组`(a，b)`，其中`a`表示行数，`b`表示列数。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our object is:")
print(df)
print("The shape of the object is:")
print(df.shape)
```

**size示例**

返回DataFrame中的元素数。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our object is:")
print(df)
print("The total number of elements in our object is:")
print(df.size)
```

**values示例**

将`DataFrame`中的实际数据作为`NDarray`返回。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our object is:")
print(df)
print("The actual data in our data frame is:")
print(df.values)
```

**head()和tail()示例**

要查看DataFrame对象的小样本，可使用`head()`和`tail()`方法。`head()`返回前`n`行(观察索引值)。显示元素的默认数量为`5`，但可以传递自定义数字值。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our data frame is:")
print(df)
print("The first two rows of the data frame is:")
print(df.head(2))
```

`tail()`返回最后`n`行(观察索引值)。显示元素的默认数量为`5`，但可以传递自定义数字值。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack']),
   'Age':pd.Series([25,26,25,23,30,29,23]), 
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8])}

#Create a DataFrame
df = pd.DataFrame(d)
print("Our data frame is:")
print( df)
print("The last two rows of the data frame is:")
print(df.tail(2))
```

