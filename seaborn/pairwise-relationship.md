# Seaborn 可视化成对关系

实时研究中的数据集包含许多变量。在这种情况下，应分析每个变量之间的关系。为（n，2）组合绘制双变量分布将是一个非常复杂且耗时的过程。

要在数据集中绘制成对的双变量分布，可以使用**pairplot（）**函数。这显示了数据帧中变量的（n，2）组合的关系作为图的矩阵，对角线图是单变量图。

## 轴数

在本节中，我们将学习什么是轴，它们的用法，参数等。

### 用法

```
seaborn.pairplot(data,…)
```

### 参量

下表列出了轴的参数-

| 序号 |                   参数及说明                   |
| ---- | :--------------------------------------------: |
| 1个  |                 **数据**数据框                 |
| 2    | **色调**数据可变以将绘图方面映射为不同的颜色。 |
| 3    |       **调色板**用于映射色调变量的颜色集       |
| 4    | **类**非身份关系的情节类型。{'scatter'，'reg'} |
| 5    |  **diag_kind**对角子图的图样。{'hist'，'kde'}  |

除数据外，所有其他参数均为可选。**pairplot**可以接受的其他参数很少。上面提到的是经常使用的参数。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.set_style("ticks")
sb.pairplot(df,hue = 'species',diag_kind = "kde",kind = "scatter",palette = "husl")
plt.show()
```

我们可以观察每个图的变化。这些图采用矩阵格式，其中行名称表示x轴，列名称表示y轴。

对角线图是内核密度图，其中其他图是如上所述的散点图。
<code class=gatsby-kernelname data-language=python></code>