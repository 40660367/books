# Seaborn 多面板分类图

我们可以使用两个图来可视化分类数据，您可以使用**pointplot（）**函数或更高级别的**factorplot（）**函数。

## 因子图

Factorplot在FacetGrid上绘制分类图。使用“种类”参数，我们可以选择箱形图，小提琴图，条形图和带状图等图。FacetGrid默认使用点图。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_csv('/share/datasets/seaborn-data/exercise.csv')
sb.factorplot(x = "time", y = "pulse", hue = "kind",data = df);
plt.show()
```

我们可以使用**kind**参数使用不同的图来可视化相同的数据。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt

df = pd.read_csv('/share/datasets/seaborn-data/exercise.csv')
sb.factorplot(x = "time", y = "pulse", hue = "kind", kind = 'violin',data = df);
plt.show()
```

在factorplot中，数据绘制在构面网格上。

## 什么是Facet Grid？

**构面网格**通过划分变量形成由行和列定义的面板矩阵。由于面板的原因，单个图看起来像多个图。分析两个离散变量中的所有组合非常有帮助。

让我们用一个例子形象化上面的定义

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/exercise.csv')
sb.factorplot(x = "time", y = "pulse", hue = "kind", kind = 'violin', col = "diet", data = df);
plt.show()
```

使用Facet的好处是，我们可以在绘图中输入另一个变量。上面的图根据使用“ col”参数的第三个变量“ diet”分为两个图。

我们可以创建许多列面并将它们与网格的行对齐-

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/titanic.csv')
sb.factorplot("alive", col = "deck", col_wrap = 3,data = df[df.deck.notnull()],kind = "count")
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
