# Pandas 聚合(aggreation)	

当有了滚动，扩展和`ewm`对象创建了以后，就有几种方法可以对数据执行聚合。

## DataFrame应用聚合

让我们创建一个DataFrame并在其上应用聚合。

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2019', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print(df)
print("=======================================")
r = df.rolling(window=3,min_periods=1)
print(r)
```

可以通过向整个DataFrame传递一个函数来进行聚合，或者通过标准的获取项目方法来选择一个列。

## 在整个数据框上应用聚合

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df)

r = df.rolling(window=3,min_periods=1)
print(r.aggregate(np.sum))
```

**在数据框的单个列上应用聚合**

示例代码

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2000', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df)
print("====================================")
r = df.rolling(window=3,min_periods=1)
print(r['A'].aggregate(np.sum))
```

**在DataFrame的多列上应用聚合**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('1/1/2018', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df)
print("==========================================")
r = df.rolling(window=3,min_periods=1)
print(r[['A','B']].aggregate(np.sum))
```

**在DataFrame的单个列上应用多个函数**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('2019/01/01', periods=10),
      columns = ['A', 'B', 'C', 'D'])
print(df)

print("==========================================")

r = df.rolling(window=3,min_periods=1)
print(r['A'].aggregate([np.sum,np.mean]))
```

**在DataFrame的多列上应用多个函数**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(10, 4),
      index = pd.date_range('2020/01/01', periods=10),
      columns = ['A', 'B', 'C', 'D'])

print(df)
print("==========================================")
r = df.rolling(window=3,min_periods=1)
print(r[['A','B']].aggregate([np.sum,np.mean]))
```

**将不同的函数应用于DataFrame的不同列**

```python
import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.randn(3, 4),
      index = pd.date_range('2020/01/01', periods=3),
      columns = ['A', 'B', 'C', 'D'])
print(df)
print("==========================================")
r = df.rolling(window=3,min_periods=1)
print(r.aggregate({'A' : np.sum,'B' : np.mean}))
```

