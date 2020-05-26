# Pandas 分类数据(categorical)

通常实时的数据包括重复的文本列。例如：性别，国家和代码等特征总是重复的。这些是分类数据的例子。

分类变量只能采用有限的数量，而且通常是固定的数量。除了固定长度，分类数据可能有顺序，但不能执行数字操作。 分类是*Pandas*数据类型。

分类数据类型在以下情况下非常有用 -

- 一个字符串变量，只包含几个不同的值。将这样的字符串变量转换为分类变量将会节省一些内存。
- 变量的词汇顺序与逻辑顺序(`"one"`，`"two"`，`"three"`)不同。 通过转换为分类并指定类别上的顺序，排序和最小/最大将使用逻辑顺序，而不是词法顺序。
- 作为其他python库的一个信号，这个列应该被当作一个分类变量(例如，使用合适的统计方法或`plot`类型)。

## 对象创建

分类对象可以通过多种方式创建。下面介绍了不同的方法 -

**类别/分类**

通过在`pandas`对象创建中将`dtype`指定为`“category”`。

```python
import pandas as pd
s = pd.Series(["a","b","c","a"], dtype="category")
print(s)
```

传递给系列对象的元素数量是四个，但类别只有三个。观察相同的输出类别。

**pd.Categorical**

使用标准*Pandas*分类构造函数，我们可以创建一个类别对象。语法如下 - 

```
pandas.Categorical(values, categories, ordered)
```

举个例子 -

```python
import pandas as pd
cat = pd.Categorical(['a', 'b', 'c', 'a', 'b', 'c'])
print(cat)
```

再举一个例子 -

```python
import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'])
print(cat)
```

这里，第二个参数表示类别。因此，在类别中不存在的任何值将被视为`NaN`。

现在，看看下面的例子 -

```python
import pandas as pd
cat = cat=pd.Categorical(['a','b','c','a','b','c','d'], ['c', 'b', 'a'],ordered=True)
print(cat)
```

从逻辑上讲，排序(*ordered*)意味着，`a`大于`b`，`b`大于`c`。

**描述**

使用分类数据上的`.describe()`命令，可以得到与类型字符串的Series或DataFrame类似的输出。

```python
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
df = pd.DataFrame({"cat":cat, "s":["a", "c", "c", np.nan]})
print(df.describe())
print("=============================")
print(df["cat"].describe())
```

**获取类别的属性**

`obj.cat.categories`命令用于获取对象的类别。

```python
import pandas as pd
import numpy as np

s = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print(s.categories)
```

**obj.ordered**命令用于获取对象的顺序。

```python
import pandas as pd
import numpy as np

cat = pd.Categorical(["a", "c", "c", np.nan], categories=["b", "a", "c"])
print(cat.ordered)
```

该函数返回结果为：*False*，因为这里没有指定任何顺序。

**重命名类别**

重命名类别是通过将新值分配给`series.cat.categories`属性来完成的。参考以下示例代码 -

```python
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s.cat.categories = ["Group %s" % g for g in s.cat.categories]

print(s.cat.categories)
```

初始类别`[a，b，c]`由对象的`s.cat.categories`属性更新。

**附加新类别**
使用`Categorical.add.categories()`方法，可以追加新的类别。

```python
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
s = s.cat.add_categories([4])
print(s.cat.categories)
```

**删除类别**
使用`Categorical.remove_categories()`方法，可以删除不需要的类别。

```python
import pandas as pd

s = pd.Series(["a","b","c","a"], dtype="category")
print("Original object:")
print(s)
print("=====================================")
print("After removal:")
print(s.cat.remove_categories("a"))
```
