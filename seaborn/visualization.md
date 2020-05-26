# Seaborn 数据可视化

可视化数据是一个步骤，进一步使可视化数据更令人愉悦是另一步骤。可视化在向观众传达定量见解以吸引他们的注意力方面起着至关重要的作用。

美学是指一系列与自然的本质和对美的欣赏有关的原则，尤其是在艺术中。可视化是一种以有效且最简单的方式表示数据的艺术。

Matplotlib库高度支持自定义，但是要知道要调整哪些设置才能获得引人入胜的预期图，这是使用它应该知道的。与Matplotlib不同，Seaborn带有自定义主题和高级界面，用于自定义和控制Matplotlib图形的外观。

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(20,6)) 

def sinplot(flip = 1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5): 
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()

plt.show()
```


要将相同的图更改为Seaborn默认值，请使用**set（）**函数-

### 实例

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt

plt.figure(figsize=(20,6)) 

def sinplot(flip = 1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set()
sinplot()
plt.show()
```

上面两个图显示了默认Matplotlib图和Seaborn图的差异。数据的表示形式相同，但是两者的表示方式不同。

基本上，Seaborn将Matplotlib参数分为两组-

- 绘图样式
- 地磅

## Seaborn人物风格

操纵样式的接口是**set_style（）**。使用此功能可以设置绘图的主题。根据最新的更新版本，以下是五个可用的主题。

- 暗网
- 白格
- 暗
- 白色

让我们尝试应用上述列表中的主题。该图的默认主题将是**Darkgrid**，这在上一个示例中已经看到。

### 例

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(20,6)) 

def sinplot(flip=1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("whitegrid")
sinplot()
plt.show()
```



上面两个图的区别是背景色

## 去除轴刺

在白色和刻度主题中，我们可以使用**despine（）**函数删除上轴和右轴的棘刺。

### 例

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(20,6)) 

def sinplot(flip=1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("white")
sinplot()
sb.despine()
plt.show()
```


在正则图中，我们仅使用左轴和底轴。使用**despine（）**函数，我们可以避免不必要的右，上轴刺，这在Matplotlib中不支持。

## 覆盖元素

如果要自定义Seaborn样式，可以将参数字典传递给**set_style（）**函数。可用的参数使用**axes_style（）**函数查看。

### 例

```python
%matplotlib inline
import seaborn as sb
print(sb.axes_style)
```
更改任何参数的值都会更改打印样式。

### 例

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(20,6))

def sinplot(flip=1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("darkgrid", {'axes.axisbelow': False})
sinplot()
sb.despine()
plt.show()
```

## 比例尺图元素

我们还可以控制图元素，并可以使用**set_context（）**函数控制图的比例。我们有四个用于上下文的预设模板，基于相对大小，上下文命名如下

- 纸
- 笔记本
- 谈论
- 海报

默认情况下，上下文设置为笔记本；并在上面的图中使用。

## 例

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(20,6))

def sinplot(flip = 1):
   x = np.linspace(0, 14, 100)
   for i in range(1, 5):
      plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
import seaborn as sb
sb.set_style("darkgrid", {'axes.axisbelow': False})
sinplot()
sb.despine()
plt.show()
```


与上述图相比，实际图的输出尺寸更大。

**注意** -由于我们网页上图像的缩放比例，您可能会错过示例图中的实际差异。
<code class=gatsby-kernelname data-language=python></code>
