# Pandas 选项和自定义

Pandas提供API来自定义其行为的某些方面，大多使用来显示。

API由五个相关函数组成。它们分别是 -

- *get_option()*
- *set_option()*
- *reset_option()*
- *describe_option()*
- *option_context()*

现在来了解函数是如何工作的。

## get_option(param)

`get_option(param)`需要一个参数，并返回下面输出中给出的值 -

`get_option`需要一个参数，并返回下面输出中给出的值 -

**display.max_rows**

显示默认值。解释器读取此值并显示此值作为显示上限的行。

```python
import pandas as pd
print("display.max_rows = ", pd.get_option("display.max_rows"))
```

**display.max_columns**

显示默认值，解释器读取此值并显示此值作为显示上限的行。

```python
import pandas as pd
print("display.max_columns = ", pd.get_option("display.max_columns"))
```

这里，`60`和`20`是默认配置参数值。

## set_option(param,value)

`set_option`需要两个参数，并将该值设置为指定的参数值，如下所示：

**display.max_rows**

使用`set_option()`，可以更改要显示的默认行数。

```python
import pandas as pd

print("before set display.max_rows = ", pd.get_option("display.max_rows")) 

pd.set_option("display.max_rows",80)
print("after set display.max_rows = ", pd.get_option("display.max_rows"))
```

**display.max_columns**

使用`set_option()`，可以更改要显示的默认行数。

```python
import pandas as pd

print("before set display.max_columns = ", pd.get_option("display.max_columns")) 

pd.set_option("display.max_columns",32)
print("after set display.max_columns = ", pd.get_option("display.max_columns"))
```

## reset_option(param)

`reset_option`接受一个参数，并将该值设置为默认值。

**display.max_rows**

使用`reset_option()`，可以将该值更改回显示的默认行数。

```python
import pandas as pd

pd.set_option("display.max_rows",32)
print("after set display.max_rows = ", pd.get_option("display.max_rows")) 

pd.reset_option("display.max_rows")
print("reset display.max_rows = ", pd.get_option("display.max_rows"))
```

## describe_option(param)

`describe_option`打印参数的描述。

**display.max_rows**

使用`reset_option()`，可以将该值更改回显示的默认行数。

```python
import pandas as pd

pd.describe_option("display.max_rows")
```

## option_context()

`option_context`上下文管理器用于临时设置语句中的选项。当退出使用块时，选项值将自动恢复 -

**display.max_rows**
使用`option_context()`，可以临时设置该值。

```python
import pandas as pd
with pd.option_context("display.max_rows",10):
   print(pd.get_option("display.max_rows"))
   print(pd.get_option("display.max_rows"))
```

请参阅第一和第二个打印语句之间的区别。第一个语句打印由`option_context()`设置的值，该值在上下文中是临时的。在使用上下文之后，第二个打印语句打印配置的值。

常用参数，请参考下表 - 

| 编号 | 参数                        | 描述                 |
| ---- | --------------------------- | -------------------- |
| 1    | `display.max_rows`          | 要显示的最大行数     |
| 2    | `display.max_columns`       | 要显示的最大列数     |
| 3    | `display.expand_frame_repr` | 显示数据帧以拉伸页面 |
| 4    | `display.max_colwidth`      | 显示最大列宽         |
| 5    | `display.precision`         | 显示十进制数的精度   |