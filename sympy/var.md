#### Var创建同名的symbol或function对象

由于符号对象名和 name属性名经常一致，所以可以使用var（）函数替代symbols

![image-20200422173938385](C:\Users\David\AppData\Roaming\Typora\typora-user-images\image-20200422173938385.png)

```python
form sympy import var
var('x y z x1 y1 z1')
%whos
```

```python
type(x)
```

![image-20200422174026600](C:\Users\David\AppData\Roaming\Typora\typora-user-images\image-20200422174026600.png)



```python
from sympy import symbols,Function,var
var('x',interger=True)
var('x y',real=True)
var('g h',cls=Function)
%whos
```



