# Seaborn 统计估计

在大多数情况下，我们处理数据整体分布的估计。但是，当涉及集中趋势估计时，我们需要一种特定的方法来汇总分布。平均值和中位数是估计分布的集中趋势的常用技术。

在上一节中学习的所有图中，我们对整个分布进行了可视化。现在，让我们讨论关于可以用来估计分布的集中趋势的图。

## 条形图

所述**barplot（）**示出了一个分类变量和连续变量之间的关系。数据用矩形条表示，其中条的长度表示该类别中数据的比例。

条形图表示集中趋势的估计。让我们使用“ titanic”数据集学习条形图。

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/titanic.csv')
sb.barplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()
```

在上面的示例中，我们可以看到每个类别中男性和女性的平均存活数。从情节中我们可以了解到，存活下来的女性人数多于男性。在男性和女性中，更多的存活率来自头等舱。

条形图中的一种特殊情况是显示每个类别中没有观测值，而不是计算第二个变量的统计量。为此，我们使用**countplot（）。**

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/titanic.csv')
sb.countplot(x = "class", data = df, palette = "Blues");
plt.show()
```

情节说，三等舱的乘客人数高于一等舱和二等舱。

## 点图

点状图与条形图相同，但样式不同。估计值由另一轴上某个高度的点表示，而不是完整的条形。

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/titanic.csv')
sb.pointplot(x = "sex", y = "survived", hue = "class", data = df)
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
