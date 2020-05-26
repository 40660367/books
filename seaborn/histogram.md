# Seaborn 直方图(histogram)

## 绘制单变量分布

数据分发是我们在分析数据时需要了解的最重要的事情。在这里，我们将看到seaborn如何帮助我们理解数据的单变量分布。

函数**distplot（）**提供了最方便的方法来快速查看单变量分布。此函数将绘制适合数据核密度估计的直方图。

直方图表示数据分布，方法是沿数据范围形成bin，然后绘制条形图以显示落入每个bin中的观测值数量。

Seaborn附带了一些数据集，在前几章中我们只使用了很少的数据集。我们已经学习了如何加载数据集以及如何查找可用数据集列表。

Seaborn附带了一些数据集，在前几章中我们只使用了很少的数据集。我们已经学习了如何加载数据集以及如何查找可用数据集列表。

## 例

```python
%matplotlib inline
import numpy as np
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.distplot(df['petal_length'],kde = False)
plt.show()
```

此处，**kde**标志设置为False。结果，将去除核估计图的表示，仅绘制直方图。

### 用法

```
seaborn.distplot(a, bins=None, hist=True, 
                 kde=True, rug=False, fit=None, 
                 hist_kws=None, kde_kws=None, rug_kws=None,
                 fit_kws=None, color=None, vertical=False,
                 norm_hist=False, axlabel=None,
                 label=None, ax=None)
```

### 参量

```
a: Series, 一维数组或列表

要输入的数据，如果设置name属性，则该名称将用于标记数据轴；

以下是可选参数:
bins: matplotlib hist()的参数 或者 None
作用：指定直方图规格，若为None，则使用Freedman-Diaconis规则,
该规则对数据中的离群值不太敏感，可能更适用于重尾分布的数据。
它使用 bin 大小  
[2∗IQR(X(:))∗numel(X)(−1/4),2∗IQR(Y(:))∗numel(Y)(−1/4)][2∗IQR(X(:))∗numel(X)(−1/4),2∗IQR(Y(:))∗numel(Y)(−1/4)] ，
其中 IQR 为四分位差。

hist:bool
是否绘制(标准化)直方图

kde:bool
是否绘制高斯核密度估计图

rug:bool
是否在支撑轴上绘制rugplot()图

{hist，kde，rug，fit} _kws：字典
底层绘图函数的关键字参数

color:matplotlib color
该颜色可以绘制除了拟合曲线之外的所有内容

vertical:bool
如果为True,则观察值在y轴上，即水平横向的显示
```

#### 实例：显示默认绘图，其中包含内核密度估计值和直方图
```python
%matplotlib inline
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)

sns.distplot(x,kde=True,hist=False)
plt.show()
```
#### 实例：绘制直方图和核函数密度估计图
```python
%matplotlib inline
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)
# 使用pandas来设置x 轴标签 和y 轴标签
x = pd.Series(x, name="x variable")

sns.distplot(x)
plt.show()
```

#### 实例：绘制核密度估计和地图

```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)
sns.distplot(x, rug=True, hist=False)
plt.show()
```
#### 实例：绘制直方图和最大似然高斯分布拟合图
```python
%matplotlib inline
from scipy.stats import norm
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)

sns.distplot(x, fit=norm, kde=False)
plt.show()
```

#### 实例：绘制水平直方图 (即在垂直轴上绘制分布)
```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)
sns.distplot(x, vertical=True)
plt.show()
```
#### 实例：改变绘图元素的颜色
```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)

sns.set_color_codes()
sns.distplot(x, color="y")
plt.show()
```

#### 实例： 制定一些绘图参数
```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)
sns.distplot(x, rug=True, rug_kws={"color": "g"},
             kde_kws={"color": "k", "lw": 3, "label": "KDE"},
             hist_kws={"histtype": "step", "linewidth": 3,
                       "alpha": 1, "color": "g"})
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
