# Seaborn 内核密度估计(kde)

核密度估计（KDE）是一种估计连续随机变量的概率密度函数的方法。用于非参数分析。

在**distplot**中将**hist**标志设置为False 将产生内核密度估计图。

## 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.distplot(df['petal_length'],hist=False)
plt.show()
```


## 拟合参数分布

**distplot（）**用于可视化数据集的参数分布。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.distplot(df['petal_length'])
plt.show()
```


## 绘制双变量分布

双变量分布用于确定两个变量之间的关系。这主要涉及两个变量之间的关系以及一个变量相对于另一个变量的行为方式。

分析seaborn中的双变量分布的最佳方法是使用**jointplot（）**函数。

Jointplot创建一个多面板图形，该图形可以投影两个变量之间的双变量关系，以及每个变量在独立轴上的单变量分布。

## 散点图

散点图是可视化分布的最便捷方法，其中每个观测值均通过x和y轴以二维图表示。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df)
plt.show()
```


上图显示了IRIS数据中的**花瓣长度**和**花瓣宽度**之间的关系。图中的趋势表明，所研究的变量之间存在正相关。

### 六边形图

当数据稀疏时，即当数据非常分散且难以通过散点图进行分析时，六边形合并用于双变量数据分析。

称为“种类”和值“十六进制”的附加参数绘制了十六进制图。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df,kind = 'hex')
plt.show()
```

内核密度估计是估计变量分布的非参数方法。在seaborn中，我们可以使用**jointplot()**绘制kde **。**

将值“ kde”传递给参数种类以绘制内核图。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.jointplot(x = 'petal_length',y = 'petal_width',data = df,kind = 'hex')
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
