# Pandas 统计函数(statistics function)

 统计方法有助于理解和分析数据的行为。现在我们将学习一些统计函数，可以将这些函数应用到*Pandas*的对象上。

## pct_change()函数

系列，DatFrames和Panel都有`pct_change()`函数。此函数将每个元素与其前一个元素进行比较，并计算变化百分比。

```python
import pandas as pd
import numpy as np
s = pd.Series([1,2,3,4,5,4])
print(s.pct_change())

df = pd.DataFrame(np.random.randn(5, 2))
print(df.pct_change())
```

默认情况下，`pct_change()`对列进行操作; 如果想应用到行上，那么可使用`axis = 1`参数。

## 协方差

协方差适用于系列数据。Series对象有一个方法`cov`用来计算序列对象之间的协方差。`NA`将被自动排除。

**Cov系列示例**

```python
import pandas as pd
import numpy as np
s1 = pd.Series(np.random.randn(10))
s2 = pd.Series(np.random.randn(10))
print(s1.cov(s2))
```

当应用于`DataFrame`时，协方差方法计算所有列之间的协方差(`cov`)值。

```python
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])
print(frame['a'].cov(frame['b']))
print(frame.cov())
```

> 注 - 观察第一个语句中`a`和`b`列之间的`cov`结果值，与由DataFrame上的`cov`返回的值相同。

## 相关性

相关性显示了任何两个数值(系列)之间的线性关系。有多种方法来计算`pearson`(默认)，`spearman`和`kendall`之间的相关性。

```python
import pandas as pd
import numpy as np
frame = pd.DataFrame(np.random.randn(10, 5), columns=['a', 'b', 'c', 'd', 'e'])

print(frame['a'].corr(frame['b']))
print(frame.corr())
```

如果DataFrame中存在任何非数字列，则会自动排除。

## 数据排名

数据排名为元素数组中的每个元素生成排名。在关系的情况下，分配平均等级。

```python
import pandas as pd
import numpy as np
s = pd.Series(np.random.randn(5), index=list('abcde'))

s['d'] = s['b'] # so there's a tie

print(s.rank())
```

`Rank`可选地使用一个默认为`true`的升序参数; 当错误时，数据被反向排序，也就是较大的值被分配较小的排序。

`Rank`支持不同的`tie-breaking`方法，用方法参数指定 -

- `average` - 并列组平均排序等级
- `min` - 组中最低的排序等级
- `max` - 组中最高的排序等级
- `first` - 按照它们出现在数组中的顺序分配队列