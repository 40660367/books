# Jupyter 绘图

## 环境配置

[环境安装](./setup.html)

### 利用networkx与pydot绘制有向图

```bash
#安装pydot库
!pip install pydot
```
```python
#绘制有向图
%matplotlib inline
import networkx as nx
import pydot
import pathlib
from matplotlib import pyplot as plt
plt.figure(figsize=(14, 7))
#有向图定义
dg=nx.DiGraph(name='directed graph')
dg.add_edge(1,2)
dg.add_edge(1,3)
dg.add_edge(3,2)
nx.draw_networkx(dg)
```
### 使用matplotlib进行绘图

```python
%matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.figure(figsize=(14, 7))
ys = 200 + np.random.randn(100)
x = [x for x in range(len(ys))]

plt.plot(x, ys, '-')
plt.fill_between(x, ys, 195, where=(ys > 195), facecolor='y', alpha=0.8)

plt.title("Fills and Alpha Example")
plt.show()
```

### 使用seaborn进行绘图

```python
%matplotlib inline
import seaborn as sns
import matplotlib.pyplot as plt
#导数数据集'titanic'
titanic=sns.load_dataset('/share/datasets/seaborn-data/titanic')
plt.figure(figsize=(14, 7))
sns.barplot(x='class',y='survived',data=titanic)

print(titanic['age'].sample(10))
#去除'age'中的缺失值，distplot不能处理缺失数据
age1=titanic['age'].dropna()
plt.figure(figsize=(14, 7))
sns.distplot(age1)
```