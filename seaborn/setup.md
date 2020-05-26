# Seaborn 环境安装及配置

## 本课程在线环境的安装

本课程无需您做任何安装操作，在浏览器中即可开始本课程的学习。

### 导入库

让我们从导入Pandas开始，这是一个用于管理关系（表格式）数据集的好库。Seaborn在处理DataFrames时非常方便，DataFrames是用于数据分析的最广泛使用的数据结构。

以下命令将帮助您导入Pandas

```python
# Pandas for managing datasets
import pandas as pd
```

现在，让我们导入Matplotlib库，它可以帮助我们自定义绘图。

```python
# Matplotlib for additional customization
from matplotlib import pyplot as plt
```

我们将使用以下命令导入Seaborn库

```python
# Seaborn for plotting and styling
import seaborn as sb
```

### 导入数据集

我们已经导入了所需的库。在本节中，我们将了解如何导入所需的数据集。

Seaborn随附了库中的一些重要数据集。安装Seaborn后，数据集将自动下载。

您可以使用任何这些数据集进行学习。

借助以下功能，您可以加载所需的数据集

```
load_dataset()
```

### 将数据作为Pandas DataFrame导入

在本节中，我们将导入数据集。默认情况下，此数据集作为Pandas DataFrame加载。如果Pandas DataFrame中有任何功能，则可以在此DataFrame上使用。

要查看Seaborn库中的所有可用数据集，可以将以下命令与**get_dataset_names（）**函数一起使用，如下所示-

```python
import seaborn as sb
print(sb.get_dataset_names())
```

以下代码行将帮助您导入数据集（注意，该数据集并非内置于seaborn，而是通过https://github.com/mwaskom/seaborn-data下载，有时会因网络问题出现加载时间过长而失败的情况），本课程中均使用本地文件保证加载速度。

```python
# Seaborn for plotting and styling
import seaborn as sb
df = sb.load_dataset('/share/datasets/seaborn-data/tips')
print(df.head())
```

DataFrames以矩形网格的形式存储数据，通过该网格可以轻松查看数据。矩形网格的每一行都包含一个实例的值，网格的每一列都是一个向量，用于保存特定变量的数据。这意味着DataFrame的行不需要包含相同数据类型的值，它们可以是数字，字符，逻辑等。

Python的DataFrames随Pandas库一起提供，它们被定义为带有二维标签的数据结构具有可能不同类型的列。

## 在您本地安装

### 使用Pip安装程序

要安装最新版本的Seaborn，可以使用pip-

```
pip install seaborn
```

### 对于Windows，Linux和Mac使用Anaconda

Anaconda（来自https://www.anaconda.com/是针对SciPy堆栈的免费Python发行版，也适用于Linux和Mac。

也可以使用conda安装发行的版本-

```
conda install seaborn
```

### 直接从github安装Seaborn的开发版本

[https://github.com/mwaskom/seaborn“](https://github.com/mwaskom/seaborn)


<code class=gatsby-kernelname data-language=python></code>
