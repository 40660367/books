# Seaborn 绘制宽格式数据

始终最好使用“长期”或“整洁”的数据集。但是有时我们别无选择，只能使用“宽格式”数据集，同样的功能也可以应用于多种格式的“宽格式”数据，包括熊猫数据框或二维NumPy数组。这些对象应直接传递给data参数，x和y变量必须指定为字符串

## 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.boxplot(data = df, orient = "h")
plt.show()
```

此外，这些函数接受Pandas或NumPy对象的向量，而不是DataFrame中的变量。

### 实例

```python
%matplotlib inline
import pandas as pd
import seaborn as sb
from matplotlib import pyplot as plt
df = pd.read_csv('/share/datasets/seaborn-data/iris.csv')
sb.boxplot(data = df, orient = "h")
plt.show()
```

对于Python世界中的许多开发人员而言，使用Seaborn的主要优点是因为它可以将pandas DataFrame对象作为参数。
