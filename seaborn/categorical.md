# Seaborn 绘制分类数据

在前面的章节中，我们了解了散点图，六边形图和kde图，这些图用于分析研究中的连续变量。当所研究的变量是分类变量时，这些图不适用。

当研究中的一个或两个变量是分类变量时，我们使用诸如slotlot（），swarmplot（）等图。Seaborn提供了这样做的界面。

## 分类散点图

在本节中，我们将学习分类散点图。

### stripplot（）

当所研究的变量之一是分类变量时，将使用stripplot（）。它代表沿任一轴排序的数据。

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.stripplot(x = "species", y = "petal_length", data = df)
plt.show()
```

在上面的图中，我们可以清楚地看到每种物种的**petal_length**的差异。但是，上述散点图的主要问题是散点图上的点是重叠的。我们使用“抖动”参数来处理这种情况。

抖动会给数据增加一些随机噪声。此参数将调整沿分类轴的位置。

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.stripplot(x = "species", y = "petal_length", data = df, jitter=0.05)
plt.show()
```

现在，可以轻松看到点的分布。

### Swarmplot（）

可以替代“抖动”的另一个选项是**swarmplot（）**函数。此函数将散点图的每个点定位在分类轴上，从而避免了点重叠-

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.swarmplot(x = "species", y = "petal_length", data = df)
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
