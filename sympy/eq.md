# sympy eqution

```python
type(Eq(2*x-1,3))
```

```python
#默认表达式=0
slove(x**2-2,x)
```



```python
from sympy.abc import x,y
from sympy import solve,linsolve,Eq
solve(Eq(2*x-1,3), x)#[2]

linsolve([x+2*y-5,2*x+y-1], (x,y))#{(-1, 3)}
```

#### 对表达式赋值计算sub

```python
from sympy.abc import x,y
from sympy import sin,cos
y = sin(x)+cos(x)
y.subs(x,0)#赋值0，结果为1
y.subs(x,x**3)#赋值x为x**3，结果为sin(x**3) + cos(x**3)
```



```python
from sympy import var,init_printing
var('x,y')
eq1=x**2+y**-1
eq1
```

```python
eq1.subs(y,3)
```