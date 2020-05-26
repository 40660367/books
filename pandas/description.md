# Pandas 描述性统计

有很多方法用来集体计算`DataFrame`的描述性统计信息和其他相关操作。 其中大多数是`sum()`，`mean()`等聚合函数，但其中一些，如`sumsum()`，产生一个相同大小的对象。 一般来说，这些方法采用轴参数，就像`ndarray.{sum，std，...}`，但轴可以通过名称或整数来指定：

- *数据帧(DataFrame)* - “index”(axis=0，默认)，columns(axis=1)

下面创建一个数据帧(DataFrame)，并使用此对象进行演示本章中所有操作。

**示例**

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
print(df)
```

**sum()方法**

返回所请求轴的值的总和。 默认情况下，轴为索引(`axis=0`)。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.sum()
```

每个单独的列单独添加(附加字符串)。

**axis=1示例**

此语法将给出如下所示的输出，参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.sum(1)
```

**mean()示例**
返回平均值，参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.mean()
```

**std()示例**

返回数字列的Bressel标准偏差。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.std()
```

## 函数和说明

下面来了解Python Pandas中描述性统计信息的函数，下表列出了重要函数 -

| 编号 | 函数        | 描述             |
| ---- | ----------- | ---------------- |
| 1    | `count()`   | 非空观测数量     |
| 2    | `sum()`     | 所有值之和       |
| 3    | `mean()`    | 所有值的平均值   |
| 4    | `median()`  | 所有值的中位数   |
| 5    | `mode()`    | 值的模值         |
| 6    | `std()`     | 值的标准偏差     |
| 7    | `min()`     | 所有值中的最小值 |
| 8    | `max()`     | 所有值中的最大值 |
| 9    | `abs()`     | 绝对值           |
| 10   | `prod()`    | 数组元素的乘积   |
| 11   | `cumsum()`  | 累计总和         |
| 12   | `cumprod()` | 累计乘积         |

> 注 - 由于DataFrame是异构数据结构。通用操作不适用于所有函数。

- 类似于：`sum()`，`cumsum()`函数能与数字和字符(或)字符串数据元素一起工作，不会产生任何错误。字符聚合从来都比较少被使用，虽然这些函数不会引发任何异常。
- 由于这样的操作无法执行，因此，当DataFrame包含字符或字符串数据时，像`abs()`，`cumprod()`这样的函数会抛出异常。

## 汇总数据

`describe()`函数是用来计算有关DataFrame列的统计信息的摘要。

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.describe()
```

该函数给出了平均值，标准差和IQR值。 而且，函数排除字符列，并给出关于数字列的摘要。 `include`是用于传递关于什么列需要考虑用于总结的必要信息的参数。获取值列表; 默认情况下是”数字值”。

- `object` - 汇总字符串列
- `number` - 汇总数字列
- `all` - 将所有列汇总在一起(不应将其作为列表值传递)

现在，在程序中使用以下语句并检查输出 -

```python
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.describe(include=['object'])
```

现在，使用以下语句并查看输出 -

```shell
import pandas as pd
import numpy as np

#Create a Dictionary of series
d = {'Name':pd.Series(['Tom','James','Ricky','Vin','Steve','Minsu','Jack',
   'Lee','David','Gasper','Betina','Andres']),
   'Age':pd.Series([25,26,25,23,30,29,23,34,40,30,51,46]),
   'Rating':pd.Series([4.23,3.24,3.98,2.56,3.20,4.6,3.8,3.78,2.98,4.80,4.10,3.65])}

#Create a DataFrame
df = pd.DataFrame(d)
df.describe(include='all')
```



