# Sympy 积分

积分有两类，定积分definite与不定积分indefinite

## 定积分definite

使用函数`Integral`来计算定积分，语法如下

 `Integral(integration_variable, lower_limit, upper_limit)`.

求$$\int_{-\infin}^{\infin} sin(x^2)$$的定积分


```python
#返回unevaluated integral.
Integral(sin(x**2),(x,-oo,oo))#指定变量范围，求定积分计算式
```
```python
Integral(sin(x**2),(x,-oo,oo)).doit()#执行计算
```
**示例**

```python
Integral(sin(x**2),(x,-2,oo))
```
```python
Integral(sin(x**2),(x,-2,oo)).doit()
```

**示例**

```python
Integral(exp(-x)*exp(-y),(x,-oo,oo),(y,-oo,oo))
```
```python
Integral(exp(-x)*exp(-y),(x,-oo,oo),(y,-oo,oo)).doit()
```

**示例**

```python
Integral((x**4+x**2*exp(x)-x**2-2*x*exp(x)-2*x-exp(x)))
```

```python
Integral((x**4+x**2*exp(x)-x**2-2*x*exp(x)-2*x-exp(x))).doit()
```

**示例**

```python
Integral(exp(x)*sin(x)+exp(x)*cos(x),(x,-oo,0))
```

```python
Integral(exp(x)*sin(x)+exp(x)*cos(x),(x,-oo,0)).doit()
```

**示例**

```python
Integral(sin(x**2),(x,-oo,oo))
```

```python
Integral(sin(x**2),(x,-oo,oo)).doit()
```



## 不定积分indefinite

求不定积分，即函数的原函数，只需要把变量做为参数传入`integrate`即可

```python
integrate(sin(x), x)#指定函数变量，求不定积分，即原函数
```

```python
integrate(exp(x)*sin(x)+exp(x)*cos(x),x)
```

多重积分示例
$$
\int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{- x^{2} - y^{2}}\, dx\, dy,
$$

```python
integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
```



```python
integrate(log(x)**2, x)
```

```python
Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x -
    exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
```

```python
expr.doit()
```

```python
expr = Integral(sin(x**2), x)
expr
```

```python
expr.doit()
```

```python
integ = Integral(x**y*exp(-x), (x, 0, oo))
integ
```

如果无法求得积分，则直接返回一个积分对象

```python
expr = integrate(x**x, x)
expr
```

```python
expr.doit()
```