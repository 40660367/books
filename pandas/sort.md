# Pandas 排序(sort)

*Pandas*有两种排序方式，它们分别是 - 

- 按标签
- 按实际值

下面来看看一个输出的例子。

```python
import pandas as pd
import numpy as np

unsorted_df=pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],\
                         columns=['col2','col1'])
print(unsorted_df)
```

在`unsorted_df`数据值中，标签和值未排序。下面来看看如何按标签来排序。

## 按标签排序

使用`sort_index()`方法，通过传递`axis`参数和排序顺序，可以对`DataFrame`进行排序。 默认情况下，按照升序对行标签进行排序。

```python
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df=unsorted_df.sort_index()
print(sorted_df)
```

## 排序顺序

通过将布尔值传递给升序参数，可以控制排序顺序。 来看看下面的例子来理解一下。

```python
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df = unsorted_df.sort_index(ascending=False)
print(sorted_df)
```

## 按列排列

通过传递`axis`参数值为`0`或`1`，可以对列标签进行排序。 默认情况下，`axis = 0`，逐行排列。来看看下面的例子来理解这个概念。

```python
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame(np.random.randn(10,2),index=[1,4,6,2,3,5,9,8,0,7],columns = ['col2','col1'])

sorted_df=unsorted_df.sort_index(axis=1)

print(sorted_df)
```

## 按值排序

像索引排序一样，`sort_values()`是按值排序的方法。它接受一个`by`参数，它将使用要与其排序值的`DataFrame`的列名称。

```python
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1')

print(sorted_df)
```

> 注意： 观察上面的输出结果，`col1`值被排序，相应的`col2`值和行索引将随`col1`一起改变。因此，它们看起来没有排序。

通过`by`参数指定需要列值，参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by=['col1','col2'])

print(sorted_df)
```

## 排序算法

`sort_values()`提供了从`mergeesort`，`heapsort`和`quicksort`中选择算法的一个配置。`Mergesort`是唯一稳定的算法。参考以下示例代码 - 

```python
import pandas as pd
import numpy as np

unsorted_df = pd.DataFrame({'col1':[2,1,1,1],'col2':[1,3,2,4]})
sorted_df = unsorted_df.sort_values(by='col1' ,kind='mergesort')

print(sorted_df)
```

