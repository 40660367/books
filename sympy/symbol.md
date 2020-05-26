# sympy symbols

### 定义符号：symbol与var ，类似于Python里的faction

创建一个符号使用symbols()，会返回一个Symbol对象，用于表示符号变量，其有name属性，这是符号名

```python
x0=symbols('x0')
```





其中左边的x是一个符号对象，而右边括 号中用引号包着的x是符号对象的name属性， 两个x不要求一样，但是为了易于理解，通常将 符号对象和name属性显示成一样，另外name 属性是引号包起来的。如要同时配置多个符号 对象，symbols()中多个name属性可以以空格或者逗号分隔，然后用引号包住，如下：

```python
from sympy import symbols

x,y = symbols('x y')
expr = x + 2*y
expr
```



