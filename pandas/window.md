# Pandas 窗口函数

为了处理数字数据，Pandas提供了几个变体，如滚动，展开和指数移动窗口统计的权重。 其中包括总和，均值，中位数，方差，协方差，相关性等。

下来学习如何在DataFrame对象上应用上提及的每种方法。

## .rolling()函数

这个函数可以应用于一系列数据。指定`window=n`参数并在其上应用适当的统计函数。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
index = pd.date_range('1/1/2020', periods=10),
columns = ['A', 'B', 'C', 'D'])

print(df.rolling(window=3).mean())
```

> 注 - 由于窗口大小为`3`(`window`)，前两个元素有空值，第三个元素的值将是`n`，`n-1`和`n-2`元素的平均值。这样也可以应用上面提到的各种函数了。

## .expanding()函数

这个函数可以应用于一系列数据。 指定`min_periods = n`参数并在其上应用适当的统计函数。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2018', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df.expanding(min_periods=3).mean())
```

## .ewm()函数

`ewm()`可应用于系列数据。指定`com`，`span`，`halflife`参数，并在其上应用适当的统计函数。它以指数形式分配权重。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
   index = pd.date_range('1/1/2019', periods=10),
   columns = ['A', 'B', 'C', 'D'])
print(df.ewm(com=0.5).mean())
```

窗口函数主要用于通过平滑曲线来以图形方式查找数据内的趋势。如果日常数据中有很多变化，并且有很多数据点可用，那么采样和绘图就是一种方法，应用窗口计算并在结果上绘制图形是另一种方法。 通过这些方法，可以平滑曲线或趋势。