# SymPy 化简simplify

#### 普通的化简

```python
from sympy import simplify

from sympy.abc import x

 
simplify((x**3 + x**2 - x - 1)/(x**2 + 2*x + 1))
```

## 指数化简

```python
from sympy import powsimp
from sympy.abc import x,a,b
y = x**a * x**b

y
```

```python
powsimp(y)
```
