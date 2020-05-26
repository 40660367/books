# Seaborn 调色板

在可视化中，颜色比任何其他方面都起着重要作用。有效地使用颜色，可以为绘图增加更多价值。调色板是指画家在其上布置和混合涂料的平坦表面。

## 调色板

Seaborn提供了一个称为**color_palette（）**的函数，该函数可用于为绘图赋予颜色并为其添加更多的美学价值。

### 用法

```
seaborn.color_palette（palette = None，n_colors = None，desat = None）
```

### 返回

返回是指RGB元组的列表。以下是现成的Seaborn调色板-

- 深
- 静音
- 亮
- 粉彩
- 暗
- 色盲

除了这些，还可以生成新的调色板

在不了解数据特征的情况下，很难决定应将哪个调色板用于给定的数据集。意识到这一点，我们将对使用**color_palette（）**类型的不同方式进行分类-

- 定性的
- 顺序的
- 发散

我们还有另一个函数**seaborn.palplot（）**处理调色板。此功能将调色板绘制为水平阵列。在接下来的示例中，我们将了解有关**seaborn.palplot（）的**更多信息。

## 定性调色板

定性或分类调色板最适合于绘制分类数据。

### 例

```python
%matplotlib inline
from matplotlib import pyplot as plt
import seaborn as sb
current_palette = sb.color_palette()
sb.palplot(current_palette)
plt.show()
```

我们没有在**color_palette（）中**传递任何参数**；**默认情况下，我们看到6种颜色。您可以通过将值传递给**n_colors**参数来查看所需的颜色数量。在这里，**palplot（）**用于水平绘制颜色阵列。

## 顺序调色板

顺序图适用于表示范围内相对较低值到较高值的数据分布。

在传递给color参数的颜色上附加一个字符's'将绘制顺序图。

### 例
```python
%matplotlib inline
from matplotlib import pyplot as plt
import seaborn as sb
current_palette = sb.color_palette()
sb.palplot(sb.color_palette("Greens"))
plt.show()
```


**注意-**我们需要在上面的示例中将's'附加到像'Greens'这样的参数上。

## 分散调色板

不同的调色板使用两种不同的颜色。每种颜色代表值从任一方向上的公共点开始的变化。

假定绘制范围为-1到1的数据。值-1到0代表一种颜色，0到+1代表另一种颜色。

默认情况下，值从零开始居中。您可以通过传递值来使用参数中心来控制它。

### 例

```python
%matplotlib inline
from matplotlib import pyplot as plt
import seaborn as sb
current_palette = sb.color_palette()
sb.palplot(sb.color_palette("BrBG", 7))
plt.show()
```


## 设置默认调色板

函数**color_palette（）**有一个名为**set_palette（）**的伴侣，它们之间的关系类似于“美学”一章中介绍的对。**set_palette（）**和**color_palette（）**的参数相同**，**但是默认的Matplotlib参数已更改，因此调色板可用于所有绘图。

### 例

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
def sinplot(flip = 1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)

import seaborn as sb
sb.set_style("white")
sb.set_palette("husl")
sinplot()
plt.show()
```


```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
plt.figure(figsize=(20,10))

sns.set()
#构建数据
np.random.seed(0)
x = np.random.randn(100)
# 制定一些绘图参数
sns.distplot(x, rug=True, rug_kws={"color": "g"},
             kde_kws={"color": "k", "lw": 3, "label": "KDE"},
             hist_kws={"histtype": "step", "linewidth": 3,
                       "alpha": 1, "color": "g"})
plt.show()
```
<code class=gatsby-kernelname data-language=python></code>
