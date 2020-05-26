# Seaborn 拟合并绘制线性关系图

大多数时候，我们使用包含多个定量变量的数据集，而分析的目的通常是将这些变量相互关联。这可以通过回归线来完成。

在建立回归模型时，我们经常检查**多重共线性，**在这里我们必须看到连续变量的所有组合之间的相关性，并会采取必要的措施消除多重共线性（如果存在）。在这种情况下，以下技术会有所帮助。

## 绘制线性回归模型的函数

Seaborn中有两个主要功能来可视化通过回归确定的线性关系。这些函数是**regplot()**和**lmplot()**。

### 例

在此示例中，先使用相同的数据绘制regplot，然后绘制lmplot

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/tips.csv')
sb.regplot(x = "total_bill", y = "tip", data = df)
sb.lmplot(x = "total_bill", y = "tip", data = df)
plt.show()
```
您可以看到两个图之间的大小差异。


当变量之一取离散值时，我们也可以拟合线性回归

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/tips.csv')
sb.lmplot(x = "size", y = "tip", data = df)
plt.show()
```


## 拟合不同类型的模型

上面使用的简单线性回归模型非常容易拟合，但是在大多数情况下，数据是非线性的，并且上述方法无法概括回归线。

让我们将Anscombe的数据集与回归图一起使用-

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/anscombe.csv')
sb.lmplot(x="x", y="y", data=df.query("dataset == 'I'"))
plt.show()
```


在这种情况下，数据非常适合线性回归模型，且方差较小。

让我们看另一个示例，其中数据存在高偏差，这表明最佳拟合线不好。

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/anscombe.csv')
sb.lmplot(x = "x", y = "y", data = df.query("dataset == 'II'"))
plt.show()
```


该图显示了数据点与回归线的高度偏差。可以使用**lmplot（）**和**regplot（）**可视化这种非线性的高阶函数，**它们**可以拟合多项式回归模型以探索数据集中简单的非线性趋势-

### 例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/anscombe.csv')
sb.lmplot(x = "x", y = "y", data = df.query("dataset == 'II'"),order = 2)
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
