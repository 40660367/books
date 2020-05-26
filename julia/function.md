# Julia 函数

<iframe src="//player.bilibili.com/player.html?aid=47775635&bvid=BV1Cb411W7Sr&cid=83682724&page=11" scrolling="no" border="0" frameborder="no" framespacing="0" allowfullscreen="true"> </iframe>

## 函数

Julia 中的函数是将一系列参数组成的元组映设到一个返回值的对象，Julia 的函数不是纯的数学式函数，有些函数可以改变或者影响程序的全局状态。Julia 中定义函数的基本语法为：

```julia
function f(x,y)
  x + y
end
f
```

Julia 中可以精炼地定义函数。上述传统的声明语法，等价于下列紧凑的“赋值形式”：

```julia
f(x,y) = x + y
```

对于赋值形式，函数体通常是单表达式，但也可以为复合表达式（详见[复合表达式](http://julia-cn.readthedocs.org/zh_CN/latest/manual/control-flow/#man-compound-expressions)）。Julia 中常见这种短小简单的函数定义。短函数语法相对而言更方便输入和阅读。

使用圆括号来调用函数：

```julia
f(2,3)
```

没有圆括号时， `f` 表达式指向的是函数对象，这个函数对象可以像值一样被传递：

```julia
g = f;

g(2,3)
```

调用函数有两种方法：使用特定函数名的特殊运算符语法（详见后面[函数运算符](http://julia-cn.readthedocs.org/zh_CN/latest/manual/functions/#operators-are-functions)），或者使用 `apply` 函数：

```julia
apply(f,2,3)
```

`apply` 函数把第一个参数当做函数对象，应用在后面的参数上。

和变量名称一样, 函数名称也可以使用 Unicode 字符:

```julia
∑(x,y) = x + y
```

## 参数传递行为

Julia 函数的参数遵循 “pass-by-sharing” 的惯例，即不传递值，而是传递引用。函数参数本身，有点儿像新变量*绑定*（引用值的新位置），但它们引用的值与传递的值完全相同。对可变值（如数组）的修改，会影响其它函数。

### `return` 关键字

函数返回值通常是函数体中最后一个表达式的值。上一节中 `f` 是表达式 `x + y` 的值。在 C 和大部分命令式语言或函数式语言中， `return` 关键字使得函数在计算完该表达式的值后立即返回：

```julia
function g(x,y)
  return x * y
  x + y
end
```

对比下列两个函数：

```julia
f(x,y) = x + y

function g(x,y)
  return x * y
  x + y
end

println(f(2,3))

println(g(2,3))
```

在纯线性函数体，比如 g 中，不需要使用 `return` ，它不会计算表达式 `x + y` 。可以把 `x * y` 作为函数的最后一个表达式，并省略 `return` 。只有涉及其它控制流时， `return` 才有用。下例计算直角三角形的斜边长度，其中直角边为 x 和 y，为避免溢出：

```julia
function hypot(x,y)
  x = abs(x)
  y = abs(y)
  if x > y
    r = y/x
    return x*sqrt(1+r*r)
  end
  if y == 0
    return zero(x)
  end
  r = x/y
  return y*sqrt(1+r*r)
end
```

最后一行的 `return` 可以省略。

## 函数运算符

Julia 中，大多数运算符都是支持特定语法的函数。 `&&` 、 `||` 等短路运算是例外，它们不是函数，因为[*短路求值*](http://julia-cn.readthedocs.org/zh_CN/latest/manual/control-flow/#man-short-circuit-evaluation)先算前面的值，再算后面的值。对于函数运算符，可以像其它函数一样，把参数列表用圆括号括起来，作为函数运算符的参数：

```julia
1 + 2 + 3
```
```julia
+(1,2,3)
```
中缀形式与函数形式完全等价，事实上，前者被内部解析为函数调用的形式。可以像对其它函数一样，对 `+` 、 `*` 等运算符进行赋值、传递：

```julia
fadd = +;

fadd(1,2,3)
```

但是，这时 `fadd` 函数不支持中缀表达式。

## 特殊名字的运算符

有一些表达式调用特殊名字的运算符：

| 表达式            | 调用         |
| :---------------- | :----------- |
| `[A B C ...]`     | `hcat`       |
| `[A, B, C, ...]`  | `vcat`       |
| `[A B; C D; ...]` | `hvcat`      |
| `A'`              | `ctranspose` |
| `A.'`             | `transpose`  |
| `1:n`             | `colon`      |
| `A[i]`            | `getindex`   |
| `A[i]=x`          | `setindex!`  |

这些函数都存在于 `Base.Operators` 模块中。

## 匿名函数

Julia 中函数是[第一类对象](http://zh.wikipedia.org/zh-cn/第一類物件)，可以被赋值给变量，可以通过赋值后的变量来调用函数, 还可以当做参数和返回值，甚至可以被匿名构造：

```julia
x -> x^2 + 2x - 1
```

上例构造了一个匿名函数，输入一个参数 x ，返回多项式 x^2 + 2x - 1 的值。匿名函数的主要作用是把它传递给接受其它函数作为参数的函数。最经典的例子是 `map` 函数，它将函数应用在数组的每个值上，返回结果数组：

```julia
map(round, [1.2,3.5,1.7])
```

`map` 的第一个参数可以是非匿名函数。但是大多数情况，不存在这样的函数时，匿名函数就可以简单地构造单用途的函数对象，而不需要名字：

```julia
map(x -> x^2 + 2x - 1, [1,3,-1])
```
匿名函数可以通过类似 `(x,y,z)->2x+y-z` 的语法接收多个参数。

无参匿名函数则类似于 `()->3` 。无参匿名函数可以“延迟”计算，做这个用处时，代码被封装进无参函数，以后可以通过把它命名为 `f()` 来引入。

## 多返回值

Julia 中可以通过返回多元组来模拟返回多值。但是，多元组并不需要圆括号来构造和析构，因此造成了可以返回多值的假象。下例返回一对儿值：

```julia
function foo(a,b)
         a+b, a*b
       end;
```
调用这个函数，但不将返回值赋值出去，会看到返回的是多元组：
```julia
foo(2,3)#(5, 6)
```

Julia 支持简单的多元组“析构”来给变量赋值：

```julia
x, y = foo(2,3);

println(x)

println(y)
```

也可以通过 `return` 来返回：

```julia
function foo(a,b)
  return a+b, a*b
end

foo(2,3)
```

这与之前定义的 `foo` 结果相同。

## 变参函数
函数的参数列表如果可以为任意个数，有时会非常方便。这种函数被称为“变参”函数，是“参数个数可变”的简称。可以在最后一个参数后紧跟省略号 `...` 来定义变参函数：

```julia
function fo1(a,b,x...)
  println(a)
  println(b)
  println(x)
end
```
变量 `a` 和 `b` 是前两个普通的参数，变量 `x` 是尾随的可迭代的参数集合，其参数个数为 `0` 或多个：

```julia
fo1(1,2)

fo1(1,2,3)

fo1(1,2,3,4)

fo1(1,2,3,4,5,6)
```

上述例子中， `x` 是传递给 `fo1` 的尾随的值多元组。

函数调用时，也可以使用 ... ：

```julia
x = (3,4)

fo1(1,2,x...)
```

上例中，多元组的值完全按照变参函数的定义进行内插，也可以不完全遵守其函数定义来调用：

```julia
x = (2,3,4)

fo1(1,x...)

x = (1,2,3,4)

fo1(x...)
```

被内插的对象也可以不是多元组：

```julia
x = [3,4

fo1(1,2,x...)

x = [1,2,3,4]

fo1(x...)
```

原函数也可以不是变参函数（大多数情况下，应该写成变参函数）：

```julia
fo2(a,b) = a + b
```
```julia
args = [1,2]
fo2(args...)
```
但如果输入的参数个数不对，函数调用会失败。
```julia
args = [1,2,3]
fo2(args...)
```


## 可选参数

很多时候，函数参数都有默认值。例如，库函数 `parseint(num,base)` 把字符串解析为某个进制的数。`base` 参数默认为 `10`。这种情形可以写为：
```julia
function parseint(num, base=10)
    println(base)
end
```
这时，调用函数时，参数可以是一个或两个。当第二个参数未指明时，自动传递 `10`：

```julia
parseint("12")
parseint("12",16)
```

可选参数很方便参数个数不同的多方法定义（详见[方法](http://julia-cn.readthedocs.org/zh_CN/latest/manual/methods/#man-methods)）。

## 关键字参数

有些函数的参数个数很多，或者有很多行为。很难记住如何调用这种函数。关键字参数，允许通过参数名来区分参数，便于使用、扩展这些复杂接口。

例如，函数 `plot` 用于画出一条线。此函数有许多可选项，控制线的类型、宽度、颜色等。如果它接收关键字参数，当我们要指明线的宽度时，可以调用 `plot(x, y, width=2)`之类的形式。这样的调用方法给参数添加了标签，便于阅读；也可以按任何顺序传递部分参数。

使用关键字参数的函数，在函数签名中使用分号来定义：
```
function plot(x, y; style="solid", width=1, color="black")
    ###
end
```

额外的关键字参数，可以像变参函数中一样，使用 `...` 来匹配：

```
function f(x; y=0, args...)
    ###
end
```
在函数 `f` 内部，`args` 可以是 `(key,value)` 多元组的集合，其中 `key` 是符号。可以在函数调用时使用分号来传递这个集合, 如 `f(x, z=1; args...).` 这种情况下也可以使用字典。

关键字参数的默认值仅在必要的时候从左至右地被求值(当对应的关键字参数没有被传递)，所以默认的(关键字参数的)表达式可以调用在它之前的关键字参数。

## 默认值的求值作用域

可选参数和关键字参数的区别在于它们的默认值是怎样被求值的。当可选的参数被求值时，只有在它*之前的*的参数在作用域之内; 与之相对的, 当关键字参数的默认值被计算时, *所有的*参数都是在作用域之内。比如，定义函数:

```julia
function f(x, a=b, b=1)
    ###
end
```
在 `a=b` 中的 `b` 指的是该函数的作用域之外的 `b` ，而不是接下来 的参数 `b`。然而，如果 `a` 和 `b` 都是关键字参数，那么它们都将在 生成在同一个作用域上，`a=b` 中的 `b` 指向的是接下来的参数 `b` (遮蔽了任何外层空间的 `b`), 并且 `a=b` 会得到未定义变量的错误 (因为默认 参数的表达式是自左而右的求值的，`b` 并没有被赋值)。

## 函数参数的块语法

将函数作为参数传递给其它函数，当行数较多时，有时不太方便。下例在多行函数中调用 `map` ：
```julia
map(x->begin
           if x < 0 && iseven(x)
               return 0
           elseif x == 0
               return 1
           else
               return x
           end
       end,
    [A, B, C])
```

Julia 提供了保留字 `do` 来重写这种代码，使之更清晰：
```julia
map([A, B, C]) do x
    if x < 0 && iseven(x)
        return 0
    elseif x == 0
        return 1
    else
        return x
    end
end
```

`do x` 的语法创建一个含有参数 `x` 的匿名函数，并将其传给 `map` 作为第一个参数。类似地，`do a,b` 将创建一个含有两个参数的匿名函数，和一个朴素的 `do` 的声明以 `() -> ....` 方式说明如下是一个匿名函数。

如何将这些参数初始化取决于“外部”函数；在这里，`map` 将依次设置 `x` 到 `A`, `B`, `C`，每个都将调用匿名函数，就像在语法 `map(func, [A, B, C])` 中做的一样。

因为语法的调用看起来像正常的代码块，所以这种语法使它更容易使用函数来有效地扩展语言。这里有许多可能完全不同于 `map` 的用途，如管理系统状态。例如，有一个版本的 `open`，运行代码来确保打开的文件最终关闭：

```julia
open("outfile", "w") do io
    write(io, data)
end
```

它可以通过以下定义来实现：

```julia
function open(f::Function, args...)
    io = open(args...)
    try
        f(io)
    finally
        close(io)
    end
end
```

对比的 `map` 的例子，这里的 IO 是通过 `open("outfile", "w")`来实现初始化的。字符流之后会传递给您的执行写入的匿名函数；最后，`open` 的功能确保流在您的函数结束后是关闭状态的。 `try/finally` 的构造将在 [*控制流*](https://www.w3cschool.cn/julia/control-learning.html) 中被描述。

do 块语法的使用有助于检查文档或实现了解用户函数的参数是如何被初始化的。