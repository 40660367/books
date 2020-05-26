# Seaborn 绘制观测值的分布

在上一章中处理的分类散点图中，该方法在它可以提供的有关每个类别中值的分布的信息方面受到限制。现在，进一步，让我们看看什么可以帮助我们进行类别比较。

## 箱形图

**箱线图**是通过四分位数可视化数据分布的便捷方法。

箱形图通常具有从框延伸的垂直线，称为晶须。这些晶须表示上下四分位数之外的变异性，因此箱形图也称为**箱须**图和**箱须**图。数据中的所有异常值均作为单个点绘制。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.swarmplot(x = "species", y = "petal_length", data = df)
plt.show()
```

图上的点表示异常值。

## 小提琴图

小提琴图是箱形图与内核密度估计值的组合。因此，这些图更易于分析和理解数据的分布。

让我们使用称为的提示数据集来了解更多关于小提琴图的信息。该数据集包含与餐厅顾客提供的小费相关的信息。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/tips.csv')
sb.violinplot(x = "day", y = "total_bill", data=df)
plt.show()
```

小提琴内显示了箱形图的四分位和晶须值。由于小提琴图使用KDE，所以小提琴的较宽部分表示较高的密度，而狭窄的区域表示相对较低的密度。箱形图的四分位数间距和kde的较高密度部分位于小提琴图的每个类别的相同区域。

上图显示了一周中四天的total_bill分布。但是，除此之外，如果我们想了解性别分布的行为，请在下面的示例中进行探讨。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/tips.csv')
sb.violinplot(x = "day", y = "total_bill",hue = 'sex', data = df)
plt.show()
```

现在我们可以清楚地看到男性和女性之间的消费行为。

我们可以很容易地说，通过观察情节，男人比女人赚更多的钱。



而且，如果色相变量只有两个类别，我们可以通过在给定的一天将每个小提琴分为两个而不是两个小提琴来美化图表。小提琴的任何部分都引用hue变量中的每个类别。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/tips.csv')
sb.violinplot(x = "day", y="total_bill",hue = 'sex', data = df)
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
