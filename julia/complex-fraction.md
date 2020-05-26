# Julia 复数和分数

## 复数和分数

Julia 提供复数和分数类型，并对其支持所有的[标准数学运算](http://julia-cn.readthedocs.org/zh_CN/latest/manual/mathematical-operations/#man-mathematical-operations) 。对不同的数据类型进行混合运算时，无论是基础的还是复合的，都会自动使用[类型转换和类型提升](https://www.w3cschool.cn/julia/type-transformation.md)。

## 复数

全局变量 `im` 即复数 i ，表示 -1 的正平方根。因为 `i` 经常作为索引变量，所以不使用它来代表复数了。Julia 允许数值文本作为[代数系数](http://julia-cn.readthedocs.org/zh_CN/latest/manual/integers-and-floating-point-numbers/#man-numeric-literal-coefficients) ，也适用于复数：

```julia
1 + 2im
```

可以对复数做标准算术运算：

```julia
(1 + 2im)*(2 - 3im)

(1 + 2im)/(1 - 2im)

(1 + 2im) + (1 - 2im)

(-3 + 2im) - (5 - 1im)

(-1 + 2im)^2

(-1 + 2im)^2.5

(-1 + 2im)^(1 + 1im)

3(2 - 5im)

3(2 - 5im)^2

3(2 - 5im)^-1.0
```

类型提升机制保证了不同类型的运算对象能够在一起运算：

```julia
2(1 - 1im)
2 - 2im

(2 + 3im) - 1
1 + 3im

(1 + 2im) + 0.5
1.5 + 2.0im

(2 + 3im) - 0.5im
2.0 + 2.5im

0.75(1 + 2im)
0.75 + 1.5im

(2 + 3im) / 2
1.0 + 1.5im

(1 - 3im) / (2 + 2im)
-0.5 - 1.0im

2im^2
-2 + 0im

1 + 3/4im
1.0 - 0.75im
```

注意： `3/4im == 3/(4*im) == -(3/4*im)` ，因为文本系数比除法优先。

处理复数的标准函数：

```julia
real(1 + 2im)

imag(1 + 2im)

conj(1 + 2im)

abs(1 + 2im)

abs2(1 + 2im)

angle(1 + 2im)
```

通常， 复数的绝对值( `abs` )是它到零的距离。 函数 `abs2` 返回绝对值的平方， 特别地用在复数上来避免开根。`angle` 函数返回弧度制的相位(即 argument 或 arg )。 所有的[基本函数](http://julia-cn.readthedocs.org/zh_CN/latest/manual/mathematical-operations/#man-elementary-functions)也可以应用在复数上：

```julia
sqrt(1im)

sqrt(1 + 2im)

cos(1 + 2im)

exp(1 + 2im)

sinh(1 + 2im)
```

作用在实数上的数学函数，返回值一般为实数；作用在复数上的，返回值为复数。例如， `sqrt` 对 `-1` 和 `-1 + 0im` 的结果不同，即使 `-1 == -1 + 0im` ：

```julia
sqrt(-1)

sqrt(-1 + 0im)
```

[代数系数](http://julia-cn.readthedocs.org/zh_CN/latest/manual/integers-and-floating-point-numbers/#man-numeric-literal-coefficients)不能用于使用变量构造复数。乘法必须显式的写出来：

```julia
a = 1; b = 2; a + b*im
```

但是， 不 推荐使用上面的方法。推荐使用 `complex` 函数构造复数：

```julia
complex(a,b)
```

这种构造方式避免了乘法和加法操作。

`Inf` 和 `NaN` 也可以参与构造复数 (参考[特殊的浮点数](http://julia-cn.readthedocs.org/zh_CN/latest/manual/integers-and-floating-point-numbers/#man-special-floats)部分)：

```julia
1 + Inf*im

1 + NaN*im
```

分数 Julia 有分数类型。使用 `//` 运算符构造分数：

```julia
2//3
```

如果分子、分母有公约数，将自动约简至最简分数，且分母为非负数：

```julia
6//9

-4//8

5//-15

-4//-12
```

约简后的分数都是唯一的，可以通过分别比较分子、分母来确定两个分数是否相等。使用 `num` 和 `den` 函数来取得约简后的分子和分母：

```julia
num(2//3)

den(2//3)
```

其实并不需要比较分数和分母，我们已经为分数定义了标准算术和比较运算：

```julia
2//3 == 6//9

2//3 == 9//27

3//7 < 1//2

3//4 > 2//3

2//4 + 1//6

5//12 - 1//4

5//8 * 3//12

6//5 / 10//7
```

分数可以简单地转换为浮点数：

```julia
float(3//4)
```

分数到浮点数的转换遵循，对任意整数 `a` 和 `b` ，除 `a == 0` 及 `b == 0` 之外，有：

```julia
isequal(float(a//b), a/b)
```

可以构造结果为 `Inf` 的分数：

```julia
5//0

-3//0

typeof(ans)
```

但不能构造结果为 `NaN` 的分数：

```julia
0//0
```

类型提升系统使得分数类型与其它数值类型交互非常简单：

```julia
3//5 + 1

3//5 - 0.5
2//7 * (1 + 2im)

2//7 * (1.5 + 2im)

3//2 / (1 + 2im)

1//2 + 2im

1 + 2//3im

0.5 == 1//2

0.33 == 1//3

0.33 < 1//3

1//3 - 0.33
```