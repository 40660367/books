# Pandas 字符串和文本数据 			

在本章中，我们将使用基本系列/索引来讨论字符串操作。在随后的章节中，将学习如何将这些字符串函数应用于数据帧(*DataFrame*)。

*Pandas*提供了一组字符串函数，可以方便地对字符串数据进行操作。 最重要的是，这些函数忽略(或排除)丢失/NaN值。

几乎这些方法都使用Python字符串函数(请参阅： http://docs.python.org/3/library/stdtypes.html#string-methods )。 因此，将Series对象转换为String对象，然后执行该操作。

下面来看看每个操作的执行和说明。

| 编号 | 函数                  | 描述                                                         |
| ---- | --------------------- | ------------------------------------------------------------ |
| 1    | `lower()`             | 将`Series/Index`中的字符串转换为小写。                       |
| 2    | `upper()`             | 将`Series/Index`中的字符串转换为大写。                       |
| 3    | `len()`               | 计算字符串长度。                                             |
| 4    | `strip()`             | 帮助从两侧的系列/索引中的每个字符串中删除空格(包括换行符)。  |
| 5    | `split(' ')`          | 用给定的模式拆分每个字符串。                                 |
| 6    | `cat(sep=' ')`        | 使用给定的分隔符连接系列/索引元素。                          |
| 7    | `get_dummies()`       | 返回具有单热编码值的数据帧(DataFrame)。                      |
| 8    | `contains(pattern)`   | 如果元素中包含子字符串，则返回每个元素的布尔值`True`，否则为`False`。 |
| 9    | `replace(a,b)`        | 将值`a`替换为值`b`。                                         |
| 10   | `repeat(value)`       | 重复每个元素指定的次数。                                     |
| 11   | `count(pattern)`      | 返回模式中每个元素的出现总数。                               |
| 12   | `startswith(pattern)` | 如果系列/索引中的元素以模式开始，则返回`true`。              |
| 13   | `endswith(pattern)`   | 如果系列/索引中的元素以模式结束，则返回`true`。              |
| 14   | `find(pattern)`       | 返回模式第一次出现的位置。                                   |
| 15   | `findall(pattern)`    | 返回模式的所有出现的列表。                                   |
| 16   | `swapcase`            | 变换字母大小写。                                             |
| 17   | `islower()`           | 检查系列/索引中每个字符串中的所有字符是否小写，返回布尔值    |
| 18   | `isupper()`           | 检查系列/索引中每个字符串中的所有字符是否大写，返回布尔值    |
| 19   | `isnumeric()`         | 检查系列/索引中每个字符串中的所有字符是否为数字，返回布尔值。 |

现在创建一个系列，看看上述所有函数是如何工作的。

```python
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print(s)
```

**1. lower()函数示例**

```python
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print(s.str.lower())
```

**2. upper()函数示例**

```python
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])

print(s.str.upper())
```

**3. len()函数示例**

```python
import pandas as pd
import numpy as np

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t', np.nan, '1234','SteveMinsu'])
print(s.str.len())
```

**4. strip()函数示例**

```python
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s)
print("=========== After Stripping ================")
print(s.str.strip())
```

**5. split(pattern)函数示例**

```python
import pandas as pd
import numpy as np
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s)
print("================= Split Pattern: ==================")
print(s.str.split(' '))
```

**6. cat(sep=pattern)函数示例**

```python
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print(s.str.cat(sep=' <=> '))
```

**7. get_dummies()函数示例**

```python
import pandas as pd
import numpy as np

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print(s.str.get_dummies())
```

**8. contains()函数示例**

```python
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s.str.contains(' '))
```

**9. replace(a,b)函数示例**

```python
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s)
print("After replacing @ with $: ============== ")
print(s.str.replace('@','$'))
```

**10. repeat(value)函数示例**

```python
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s.str.repeat(2))
```

**11. count(pattern)函数示例**

```python
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print("The number of 'm's in each string:")
print(s.str.count('m'))
```

**12. startswith(pattern)函数示例**

```python
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])

print("Strings that start with 'T':")
print(s.str. startswith ('T'))
```

**13. endswith(pattern)函数示例**

```python
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print("Strings that end with 't':")
print(s.str.endswith('t'))
```

**14. find(pattern)函数示例**

```python
import pandas as pd
s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s.str.find('e'))
```

> 注意：`-1`表示元素中没有这样的模式可用。

**15. findall(pattern)函数示例**

```python
import pandas as pd

s = pd.Series(['Tom ', ' William Rick', 'John', 'Alber@t'])
print(s.str.findall('e'))
```

> 空列表(`[]`)表示元素中没有这样的模式可用。

**16. swapcase()函数示例**

```python
import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print(s.str.swapcase())
```

**17. islower()函数示例**

```python
import pandas as pd

s = pd.Series(['Tom', 'William Rick', 'John', 'Alber@t'])
print(s.str.islower())
```

**18. isupper()函数示例**

```python
import pandas as pd

s = pd.Series(['TOM', 'William Rick', 'John', 'Alber@t'])

print(s.str.isupper())
```

执行上面示例代码，得到以下结果 - 

**19. isnumeric()函数示例**

```python
import pandas as pd
s = pd.Series(['Tom', '1199','William Rick', 'John', 'Alber@t'])
print(s.str.isnumeric())
```