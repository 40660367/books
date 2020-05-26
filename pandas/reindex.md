# Pandas 重建索引(reindex)

重新索引会更改DataFrame的行标签和列标签。重新索引意味着符合数据以匹配特定轴上的一组给定的标签。

可以通过索引来实现多个操作 -

- 重新排序现有数据以匹配一组新的标签。
- 在没有标签数据的标签位置插入缺失值(NA)标记。

**示例**

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

#reindex the DataFrame
df_reindexed = df.reindex(index=[0,2,5], columns=['A', 'C', 'B'])

print(df_reindexed)
```

## 重建索引与其他对象对齐

有时可能希望采取一个对象和重新索引，其轴被标记为与另一个对象相同。 考虑下面的例子来理解这一点。

**示例**

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(10,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(7,3),columns=['col1','col2','col3'])

df1 = df1.reindex_like(df2)
print(df1)
```

> 注意 - 在这里，`df1`数据帧(*DataFrame*)被更改并重新编号，如`df2`。 列名称应该匹配，否则将为整个列标签添加`NAN`。

## 填充时重新加注

`reindex()`采用可选参数方法，它是一个填充方法，其值如下：

- `pad/ffill` - 向前填充值
- `bfill/backfill` - 向后填充值
- `nearest`  - 从最近的索引值填充

**示例**

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print("Data Frame with Forward Fill:")
print(df2.reindex_like(df1,method='ffill'))
```

> 注 - 最后四行被填充了。

## 重建索引时的填充限制

限制参数在重建索引时提供对填充的额外控制。限制指定连续匹配的最大计数。考虑下面的例子来理解这个概念 -

**示例**

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
df2 = pd.DataFrame(np.random.randn(2,3),columns=['col1','col2','col3'])

# Padding NAN's
print(df2.reindex_like(df1))

# Now Fill the NAN's with preceding Values
print("Data Frame with Forward Fill limiting to 1:")
print(df2.reindex_like(df1,method='ffill',limit=1))
```

> 注意 - 只有第`7`行由前`6`行填充。 然后，其它行按原样保留。

## 重命名

`rename()`方法允许基于一些映射(字典或者系列)或任意函数来重新标记一个轴。
看看下面的例子来理解这一概念。

**示例**

```python
import pandas as pd
import numpy as np

df1 = pd.DataFrame(np.random.randn(6,3),columns=['col1','col2','col3'])
print(df1)

print("After renaming the rows and columns:")
print(df1.rename(columns={'col1' : 'c1', 'col2' : 'c2'},index = {0 : 'apple', 1 : 'banana', 2 : 'durian'}))
```

`rename()`方法提供了一个`inplace`命名参数，默认为`False`并复制底层数据。 指定传递`inplace = True`则表示将数据重命名。