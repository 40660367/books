# Seaborn 配对网格

PairGrid允许我们使用相同的绘图类型绘制子图网格以可视化数据。

与FacetGrid不同，它为每个子图使用不同的变量对。它形成子图矩阵。有时也称为“散点图矩阵”。

pairgrid的用法类似于facetgrid。首先初始化网格，然后传递绘图功能。

## 实例：PairGrid首先初始化网格，然后传递绘图功能。

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
g = sb.PairGrid(df)
g.map(plt.scatter);
plt.show()
```

## 实例：对角线上绘制不同的函数，以显示每列中变量的单变量分布。

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
g = sb.PairGrid(df)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter);
plt.show()
```



## 实例：自定义这些图的颜色
我们可以使用另一个分类变量来自定义这些图的颜色。
例如，鸢尾花数据集针对三种不同种类的鸢尾花中的每一种都有四个测量值，因此您可以看到它们之间的差异。

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
g = sb.PairGrid(df)
g.map_diag(plt.hist)
g.map_offdiag(plt.scatter);
plt.show()
```

## 实例：上下三角形中使用不同的函数来查看关系的不同方面。

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
g = sb.PairGrid(df)
g.map_upper(plt.scatter)
g.map_lower(sb.kdeplot, cmap = "Blues_d")
g.map_diag(sb.kdeplot, lw = 3, legend = False);
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
