# Pandas 可视化(visualization)

**基本绘图：绘图**

Series和DataFrame上的这个功能只是使用`matplotlib`库的`plot()`方法的简单包装实现。参考以下示例代码 - 

```python
%matplotlib inline
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10,4),\
                  index=pd.date_range('2018/12/18',periods=10), \
                  columns=list('ABCD'))
df.plot(figsize=(16,6))
```

如果索引由日期组成，则调用`gct().autofmt_xdate()`来格式化`x`轴，如上图所示。

我们可以使用`x`和`y`关键字绘制一列与另一列。

绘图方法允许除默认线图之外的少数绘图样式。 这些方法可以作为`plot()`的`kind`关键字参数提供。这些包括 -

- `bar`或`barh`为条形
- `hist`为直方图
- `boxplot`为盒型图
- `area`为“面积”
- `scatter`为散点图

## 条形图

现在通过创建一个条形图来看看条形图是什么。条形图可以通过以下方式来创建 -

```python
%matplotlib inline
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(figsize=(16,6))
```

要生成一个堆积条形图，通过指定：*pass stacked=True* -

```python
%matplotlib inline
import pandas as pd
df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])
df.plot.bar(figsize=(16,6),stacked=True)
```

要获得水平条形图，使用`barh()`方法 -

```python
%matplotlib inline
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10,4),columns=['a','b','c','d'])

df.plot.barh(figsize=(16,6),stacked=True)
```

## 直方图

可以使用`plot.hist()`方法绘制直方图。我们可以指定`bins`的数量值。

```python
%matplotlib inline
import pandas as pd
import numpy as np

df = pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.plot.hist(figsize=(16,6),bins=20)
```

要为每列绘制不同的直方图，请使用以下代码 -

```python
%matplotlib inline
import pandas as pd
import numpy as np

df=pd.DataFrame({'a':np.random.randn(1000)+1,'b':np.random.randn(1000),'c':
np.random.randn(1000) - 1}, columns=['a', 'b', 'c'])

df.hist(figsize=(16,6),bins=20)
```

## 箱形图

Boxplot可以绘制调用`Series.box.plot()`和`DataFrame.box.plot()`或`DataFrame.boxplot()`来可视化每列中值的分布。

例如，这里是一个箱形图，表示对`[0,1)`上的统一随机变量的`10`次观察的五次试验。

```python
%matplotlib inline
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
df.plot.box(figsize=(16,6))
```

## 区域块图形

可以使用`Series.plot.area()`或`DataFrame.plot.area()`方法创建区域图形。

```python
%matplotlib inline
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df.plot.area(figsize=(16,6))
```

## 散点图形

可以使用`DataFrame.plot.scatter()`方法创建散点图。

```python
%matplotlib inline
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.rand(50, 4), columns=['a', 'b', 'c', 'd'])
df.plot.scatter(x='a', y='b',figsize=(16,6))
```

## 饼状图

饼状图可以使用`DataFrame.plot.pie()`方法创建。

```python
%matplotlib inline
import pandas as pd
import numpy as np

df = pd.DataFrame(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], columns=['x'])
df.plot.pie(subplots=True,figsize=(16,6))
```