# SymPy 简介

Sympy是Python的一个数学符号计算库。它目的在于成为一个富有特色的计算机代数系统。它保证自身的代码尽可能的简单，且易于理解，容易扩展。Sympy完全由Python写成，不需要额外的库。

SymPy一个用于符号型数学计算（symbolic mathematics）的Python库。它旨在成为一个功能齐全的计算机代数系统（Computer Algebra System，CAS），同时保持代码简洁、易于理解和扩展。



## 符号计算的优点

```python
import math
math.sqrt(8)**2
```

本以为会得到8.0,但没想到得到8.00000000000000**2**。

 一、为什么会这样？

如果我们平常计算的任务常常有类似于上面的例子这样的表达式，那么直接用python计算其结果只是真实值的逼近。如果这样的计算很大很多，误差会逐渐积累，这是我们不能忍受的，所以这时候就需要Python能处理这种数学符号计算。

二、什么是数学符号计算？

数学符号计算能处理表征数字的符号计算。这意味着数学对象被精确地表示，而不是近似地表示，而具有未被计算的变量的数学表达式被留在符号形式中。

用符号计算：验证欧拉公式

```python
from sympy import *
E**(I*pi)+1
```


## `Rational`值

SymPy 具有用于处理有理数的`Rational`。 有理数是可以表示为两个整数（分子 p 和非零分母 q）的商或分数 p / q 的任何数字。

```python
from sympy import Rational

r1 = Rational(1/10)
r2 = Rational(1/10)
r3 = Rational(1/10)

val = (r1 + r2 + r3) * 3
print(val.evalf())

val2 = (1/10 + 1/10 + 1/10) * 3
print(val2)
```

该示例使用有理数。

```python
val = (r1 + r2 + r3) * 3
print(val.evalf())
```







#### 表达式美观打印

init_printing(use_unicode=True)



```python
from sympy import var,init_printing
var('x,y')
eq1=x**3+x**2+y**-1
eq1
```



```python
init_printing(use_unicode=True)
eq1
```



