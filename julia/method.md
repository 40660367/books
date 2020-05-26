# Julia 方法

<iframe src="//player.bilibili.com/player.html?aid=47775635&bvid=BV1Cb411W7Sr&cid=83682792&page=12" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## 方法

*函数*中说到，函数是从参数多元组映射到返回值的对象，若没有合适返回值则抛出异常。实际中常需要对不同类型的参数做同样的运算，例如对整数做加法、对浮点数做加法、对整数与浮点数做加法，它们都是加法。在 Julia 中，它们都属于同一对象： `+` 函数。

对同一概念做一系列实现时，可以逐个定义特定参数类型、个数所对应的特定函数行为。*方法*是对函数中某一特定的行为定义。函数中可以定义多个方法。对一个特定的参数多元组调用函数时，最匹配此参数多元组的方法被调用。

函数调用时，选取调用哪个方法，被称为[重载](http://en.wikipedia.org/wiki/Multiple_dispatch)。 Julia 依据参数个数、类型来进行重载。

## 定义方法

Julia 的所有标准函数和运算符，如前面提到的 `+` 函数，都有许多针对各种参数类型组合和不同参数个数而定义的方法。

定义函数时，可以像[*复合类型*]中介绍的那样，使用 `::` 类型断言运算符，选择性地对参数类型进行限制：

```julia
f(x::Float64, y::Float64) = 2x + y;
```

此函数中参数 `x` 和 `y` 只能是 `Float64` 类型：

```julia
f(2.0, 3.0)
```

如果参数是其它类型，会引发 “no method” 错误：

```julia
f(2.0, 3)

f(float32(2.0), 3.0)

f(2.0, "3.0")

f("2.0", "3.0")
```

有时需要写一些通用方法，这时应声明参数为抽象类型：

```julia
f(x::Number, y::Number) = 2x - y;

f(2.0, 3)
```

要想给一个函数定义多个方法，只需要多次定义这个函数，每次定义的参数个数和类型需不同。函数调用时，最匹配的方法被重载：

```julia
f(2.0, 3.0)

f(2, 3.0)

f(2.0, 3)

f(2, 3)
```

对非数值的值，或参数个数少于 2，`f` 是未定义的，调用它会返回 “no method” 错误：

```julia
f("foo", 3)

f()
```

在交互式会话中输入函数对象本身，可以看到函数所存在的方法：

```julia
f
```

这个输出告诉我们，`f` 是一个含有两个方法的函数对象。要找出这些方法的签名，可以通过使用 `methods` 函数来实现：

```julia
methods(f)
```

这表明，`f` 有两个方法，一个以两个 `Float64` 类型作为参数和另一个则以一个 `Number` 类型作为参数。它也指示了定义方法的文件和行数：因为这些方法在 REPL 中定义，我们得到明显行数值：`none:1`。

定义类型时如果没使用 `::`，则方法参数的类型默认为 `Any`。对 `f` 定义一个总括匹配的方法：

```julia
f(x,y) = println("Whoa there, Nelly.");

f("foo", 1)
```

总括匹配的方法，是重载时的最后选择。

重载是 Julia 最强大最核心的特性。核心运算一般都有好几十种方法：

```julia
methods(+)
```

重载和灵活的参数化类型系统一起，使得 Julia 可以抽象表达高级算法，不需关注实现的具体细节，生成有效率、运行时专用的代码。

## 方法歧义

函数方法的适用范围可能会重叠：

```julia
g(x::Float64, y) = 2x + y;

g(x, y::Float64) = x + 2y;

g(2.0, 3)

g(2, 3.0)

g(2.0, 3.0)
```

此处 `g(2.0, 3.0)` 既可以调用 `g(Float64, Any)`，也可以调用 `g(Any, Float64)`，两种方法没有优先级。遇到这种情况，Julia 会警告定义含糊，但仍会任选一个方法来继续执行。应避免含糊的方法：

```julia
g(x::Float64, y::Float64) = 2x + 2y;

g(x::Float64, y) = 2x + y;

g(x, y::Float64) = x + 2y;

g(2.0, 3)

g(2, 3.0)

g(2.0, 3.0)
```

要消除 Julia 的警告，应先定义清晰的方法。

## 参数化方法

构造参数化方法，应在方法名与参数多元组之间，添加类型参数：

```julia
same_type{T}(x::T, y::T) = true;

same_type(x,y) = false;
```

这两个方法定义了一个布尔函数，它检查两个参数是否为同一类型：

```julia
same_type(1, 2)

same_type(1, 2.0)

same_type(1.0, 2.0)

same_type("foo", 2.0)

same_type("foo", "bar")

same_type(int32(1), int64(2))
```

类型参数可用于函数定义或函数体的任何地方：

```julia
myappend{T}(v::Vector{T}, x::T) = [v..., x]

myappend([1,2,3],4)

myappend([1,2,3],2.5)

myappend([1.0,2.0,3.0],4.0)

myappend([1.0,2.0,3.0],4)
```

下例中，方法类型参数 `T` 被用作返回值：

```julia
mytypeof{T}(x::T) = T

mytypeof(1)

mytypeof(1.0)
```

方法的类型参数也可以被限制范围：

```julia
same_type_numeric{T<:Number}(x::T, y::T) = true
same_type_numeric(x::Number, y::Number) = false

same_type_numeric(1, 2)

same_type_numeric(1, 2.0)

same_type_numeric(1.0, 2.0)

same_type_numeric("foo", 2.0)

same_type_numeric("foo", "bar")

same_type_numeric(int32(1), int64(2))
```

`same_type_numeric` 函数与 `same_type` 大致相同，但只应用于数对儿。

## 关于可选参数和关键字参数

*函数*中曾简略提到，可选参数是可由多方法定义语法的实现。例如：

```julia
f(a=1,b=2) = a+2b
```

可以翻译为下面三个方法：

```julia
f(a,b) = a+2b
f(a) = f(a,2)
f() = f(1,2)
```

关键字参数则与普通的与位置有关的参数不同。它们不用于方法重载。方法重载仅基于位置参数，选取了匹配的方法后，才处理关键字参数。


