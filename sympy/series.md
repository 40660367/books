# 级数展开(Series Expansion)

```python
exp=exp(sin(x))
expr.series(x,0,4)
```

```python
x + x**3 + x**5 +O(x**6)
```

```python
x + x**3 + x**7 +O(x**6)
```

#### 展开式

高数中有泰勒展开式，拉格朗日展开式。

e^x=1+x+x^2/2!+x^3/3!+x^4/4!+...+x^n/n!+o(x^n) 

比如当n=3时，

e^x=1+x+x^2/2+o(x^3)

这里实现的方法是：sympy表达式.series(变量, 0, n)

```python
from sympy import exp,symbols

x = symbols('x')
expr = exp(x)


expr.series(x, 0, 3)
```





## 

SymPy can compute asymptotic series expansions of functions around a point. To compute the expansion of f(x)f(x) around the point x=x0x=x0 terms of order xnxn, use `f(x).series(x, x0, n)`. `x0` and `n` can be omitted, in which case the defaults `x0=0` and `n=6` will be used.