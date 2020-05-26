# sympy Function

#### symbols
```python
from sympy import Function, symbols

f = Function('f')

\# type(f)#sympy.core.function.UndefinedFunction

x,y=symbols('x y')

type(f('x','y'))
```



```python
import sympy
x = sympy.Symbol("x", real=True)
y = sympy.Symbol("y")

f = sympy.Function("f")#使用 Function()创建自定义的数学函数：
t = f(x,y)#当我使用f创建一个表达式时，就相当于创建它的一个实例：
isinstance(t, sympy.Function)#True
t+t*t#function的实例t可以参与表达式运算：
#f(x, y)**2 + f(x, y)

DSolve[y''[x] == 2 x*y[x], y[x], x]
```

