# SymPy 导数derivatives

```python
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
```

#### 表达式：DerivativeCarries out differentiation of the given expression with respect to symbols.

```
Derivative(sin(x))
```

```python
#To take an unevaluated derivative, use the Derivative class.
Derivative(expr, x, y, y, z, 4)
```

```python
type(Derivative(exp,x,y,2))
```

```python
import sympy
x,y,z=sympy.symbols('x y z')
exp= 3*x**2*y*z
Derivative(f,x,y,z)
```

```python
diff(cos(x), x)
```

```
diff(exp(x**2), x)
```

`diff`一次可以取多个导数 要采用多个导数，请根据需要多次传递变量，或在变量后传递数字。

例如，以下两个都找到的三阶导数$$x^4$$

```python
diff(x**4, x, x, x)
```

```python
diff(x**4, x, 3)
```

##### 对表达式进行计算doit,相当于对表达式使用diff函数

```
Derivative(sin(x))#表示

Derivative(sin(x)).doit()#计算导函数
diff(sin(x))
```

```python
import sympy
x,y,z=sympy.symbols('x y z')
exp = 3*x**4*y*z**2
Derivative(exp,x,y,2,z)
```

```python
Derivative(exp,x,y,2,z).doit()
```

#### 计算：diff，返回给定函数关于某个变量的导函数

```python
#To take derivatives, use the diff function.

from sympy import *
x, y, z = symbols('x y z')
expr = exp(x*y*z)
init_printing(use_unicode=True)
diff(expr, x, y,2, z, 3)
```

```python
from sympy import *
x,y,z=sympy.symbols('x')
diff(sin(x)*exp(x),x)
```

```python
from sympy import diff,sin,cos
from sympy.abc import x,y,z,f
#对sin(x)求导
diff(sin(x))
diff(sin(x),x)#结果同上


#对cos(x)求导
diff(cos(x))
diff(cos(x),x)#结果同上
```

#### 求偏导diff

```python
f = 3*x**2*y*z
f
diff(f, x,y)
```

#### 高阶导数

```python
expr = exp(x*y*z)
diff(expr, x, y, y, z, z, z, z)
diff(expr, x, y, 2, z, 4)
diff(expr, x, y, y, z, 4)
```

