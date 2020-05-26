# Julia 元编程

## 元编程

类似 Lisp ，Julia 自身的代码也是语言本身的数据结构。由于代码是由这门语言本身所构造和处理的对象所表示的，因此程序也可以转换并生成自身语言的代码。元编程的另一个功能是反射，它可以在程序运行时动态展现程序本身的特性。

## 表达式和求值

Julia 代码表示为由 Julia 的 `Expr` 类型的数据结构而构成的语法树。下面是 `Expr` 类型的定义：

```
type Expr
  head::Symbol
  args::Array{Any,1}
  typ
end
```

`head` 是标明表达式种类的符号；`args` 是子表达式数组，它可能是求值时引用变量值的符号，也可能是嵌套的 `Expr` 对象，还可能是真实的对象值。 `typ` 域被类型推断用来做类型注释，通常可以被忽略。

有两种“引用”代码的方法，它们可以简单地构造表达式对象，而不需要显式构造 `Expr` 对象。第一种是内联表达式，使用 `:` ，后面跟单表达式；第二种是代码块儿，放在 `quote ... end` 内部。下例是第一种方法，引用一个算术表达式：

```julia
ex = :(a+b*c+1)
:(a + b * c + 1)

typeof(ex)

ex.head

typeof(ans)

ex.args

typeof(ex.args[1])

typeof(ex.args[2])

typeof(ex.args[3])

typeof(ex.args[4])
```

下例是第二种方法：

```julia
quote
         x = 1
         y = 2
         x + y
       end
quote  # none, line 2:
    x = 1 # line 3:
    y = 2 # line 4:
    x + y
end
```

### 符号

`:` 的参数为符号时，结果为 `Symbol` 对象，而不是 `Expr` ：

```julia
:foo
:foo

typeof(ans)
Symbol
```

在表达式的上下文中，符号用来指示对变量的读取。当表达式被求值时，符号的值受限于符号的作用域（详见[*变量的作用域*](http://julia-cn.readthedocs.org/zh_CN/latest/manual/variables-and-scoping/#man-variables-and-scoping)）。

有时, 为了防止解析时产生歧义，`:` 的参数需要添加额外的括号：

```julia
:(:)

:(::)
```

`Symbol` 也可以使用 `symbol` 函数来创建，参数为一个字符或者字符串：

```
symbol('\'')

symbol("'")
```

### 求值和内插

指定一个表达式，Julia 可以使用 `eval` 函数在 global 作用域对其求值。

```julia
:(1 + 2)

eval(ans)

ex = :(a + b)

eval(ex)

a = 1; b = 2;

eval(ex)
```

每一个[组件](https://www.w3cschool.cn/julia/module-learning.html) 有在它全局范围内评估计算表达式的 `eval` 表达式。传递给 `eval` 的表达式不限于返回一个值 - 他们也会具有改变封闭模块的环境状态的副作用：

```julia
ex = :(x = 1)
:(x = 1)

x

eval(ex)

x
```

表达式仅仅是一个 `Expr` 对象，它可以通过编程构造，然后对其求值：

```julia
a = 1;

ex = Expr(:call, :+,a,:b)

a = 0; b = 2;

eval(ex)
```

注意上例中 `a` 与 `b` 使用时的区别：

- 表达式构造时，直接使用*变量* `a` 的值。因此，对表达式求值时 `a` 的值没有任何影响：表达式中的值为 `1`，与现在 `a` 的值无关
- 表达式构造时，使用的是*符号* `:b` 。因此，构造时变量 `b` 的值是无关的—— `:b` 仅仅是个符号，此时变量 `b` 还未定义。对表达式求值时，通过查询变量 `b` 的值来解析符号 `:b` 的值

这样构造 `Expr` 对象太丑了。Julia 允许对表达式对象内插。因此上例可写为：

```julia
a = 1;

ex = :($a + b)
```

编译器自动将这个语法翻译成上面带 `Expr` 的语法。

### 代码生成

Julia 使用表达式内插和求值来生成重复的代码。下例定义了一组操作三个参数的运算符： ::

```julia
for op = (:+, :*, :&, :|, :$)
  eval(quote
    ($op)(a,b,c) = ($op)(($op)(a,b),c)
  end)
end
```

上例可用 `:` 前缀引用格式写的更精简： ::

```julia
for op = (:+, :*, :&, :|, :$)
  eval(:(($op)(a,b,c) = ($op)(($op)(a,b),c)))
end
```

使用 `eval(quote(...))` 模式进行语言内的代码生成，这种方式太常见了。Julia 用宏来简写这个模式： 

```julia
for op = (:+, :*, :&, :|, :$)
  @eval ($op)(a,b,c) = ($op)(($op)(a,b),c)
end
```

`@eval` 宏重写了这个调用，使得代码更精简。 `@eval` 的参数也可以是块代码：

```julia
@eval begin
  # multiple lines
end
```

对非引用表达式进行内插，会引发编译时错误：

```julia
$a + b
```

## 宏

宏有点儿像编译时的表达式生成函数。正如函数会通过一组参数得到一个返回值,宏可以进行表达式的变换，这些宏允许程序员在最后的程序语法树中对表达式进行任意的转化。调用宏的语法为：

`@name expr1 expr2 ...`,`@name(expr1, expr2, ...)`

注意，宏名前有 `@` 符号。第一种形式，参数表达式之间没有逗号；第二种形式，宏名后没有空格。这两种形式不要记混。例如，下面的写法的结果就与上例不同，它只向宏传递了一个参数，此参数为多元组 `(expr1, expr2, ...)`:`@name (expr1, expr2, ...)`

程序运行前， `@name` 展开函数会对表达式参数处理，用结果替代这个表达式。使用关键字 `macro` 来定义展开函数：

```julia
macro name(expr1, expr2, ...)
    ...
    return resulting_expr
end
```

下例是 Julia 中 `@assert` 宏的简单定义：

```julia
macro assert(ex)
    return :($ex ? nothing : error("Assertion failed: ", $(string(ex))))
end
```

这个宏可如下使用：

```julia
@assert 1==1.0

@assert 1==0
```

宏调用在解析时被展开为返回的结果。这等价于：

```julia
1==1.0 ? nothing : error("Assertion failed: ", "1==1.0")
1==0 ? nothing : error("Assertion failed: ", "1==0")
```

上面的代码的意思是，当第一次调用表达式 `:(1==1.0)` 的时候，会被拼接为条件语句，而 `string(:(1==1.0))` 会被替换成一个断言。因此所有这些表达式构成了程序的语法树。然后在运行期间，如果表达式为真，则返回 `nothing`，如果条件为假，一个提示语句将会表明这个表达式为假。注意，这里无法用函数来代替，因为在函数中只有值可以被传递，如果这么做的话我们无法在最后的错误结果中得到具体的表达式是什么样子的。

在标准库中真实的 `@assert` 定义要复杂一些，它可以允许用户去操作错误信息，而不只是打印出来。和函数一样宏也可以有可变参数，我们可以看下面的这个定义：

```julia
macro assert(ex, msgs...)
    msg_body = isempty(msgs) ? ex : msgs[1]
    msg = string("assertion failed: ", msg_body)
    return :($ex ? nothing : error($msg))
end
```

现在根据参数的接收数目我们可以把 `@assert` 分为两种操作模式。如果只有一个参数，表达式会被 `msgs` 捕获为空，并且如上面所示作为一个更简单的定义。如果用户填上第二个参数, 这个参数会被作为打印参数而不是错误的表达式。你可以在下面名为 `macroexpand` 的函数中检查宏扩展的结果:

```julia
macroexpand(:(@assert a==b))
:(if a == b
        nothing
    else
        Base.error("assertion failed: a == b")
    end)

macroexpand(:(@assert a==b "a should equal b!"))
:(if a == b
        nothing
    else
        Base.error("assertion failed: a should equal b!")
    end)
```

在实际的 `@assert` 宏定义中会有另一种情况：如果不仅仅是要打印 "a should equal b,"，我们还想要打印它们的值呢？有些人可能天真的想插入字符串变量如:`@assert a==b "a ($a) should equal b ($b)!"`，但是这个宏不会如我们所愿的执行。你能看出是为什么吗？回顾字符串的那一章，一个字符串的重写函数，请进行比较：

```julia
typeof(:("a should equal b"))

typeof(:("a ($a) should equal b ($b)!"))

dump(:("a ($a) should equal b ($b)!"))
```

所以现在不应该得到一个面上的字符串 `msg_body`，这个宏接收整个表达式且需要如我们所期望的计算。这可以直接拼接成返回的表达式来作为 `string` 调用的一个参数。通过看 [error.jl](https://github.com/JuliaLang/julia/blob/master/base/error.jl)源码得到完整的实现。

`@assert` 宏极大地通过宏替换实现了表达式的简化功能。

### 卫生宏

[卫生宏](http://en.wikipedia.org/wiki/Hygienic_macro)是个更复杂的宏。一般来说，宏必须确保变量的引入不会和现有的上下文变量发送冲突。相反的，宏中的表达式作为参数应该可以和上下文代码有机的结合在一起，进行交互。另一个令人关注的问题是，当宏用不同方式定义的时候是否被应该称为另一种模式。在这种情况下，我们需要确保所有的全局变量应该被纳入正确的模式中来。Julia 已经在宏方面有了很大的优势相比其它语言（比如 C）。所有的变量（比如 `@assert`中的 `msg`）遵循这一标准。

来看一下 `@time` 宏，它的参数是一个表达式。它先记录下时间，运行表达式，再记录下时间，打印出这两次之间的时间差，它的最终值是表达式的值：

```julia
macro time(ex)
  return quote
    local t0 = time()
    local val = $ex
    local t1 = time()
    println("elapsed time: ", t1-t0, " seconds")
    val
  end
end
```

`t0`, `t1`, 及 `val` 应为私有临时变量，而 `time` 是标准库中的 `time` 函数，而不是用户可能使用的某个叫 `time` 的变量（ `println` 函数也如此）。

Julia 宏展开机制是这样解决命名冲突的。首先，宏结果的变量被分类为本地变量或全局变量。如果变量被赋值（且未被声明为全局变量）、被声明为本地变量、或被用作函数参数名，则它被认为是本地变量；否则，它被认为是全局变量。本地变量被重命名为一个独一无二的名字（使用 `gensym` 函数产生新符号），全局变量被解析到宏定义环境中。

但还有个问题没解决。考虑下例：

```julia
module MyModule
import Base.@time

time() = ... # compute something

@time time()
end
```

此例中， `ex` 是对 `time` 的调用，但它并不是宏使用的 `time` 函数。它实际指向的是 `MyModule.time` 。因此我们应对要解析到宏调用环境中的 `ex` 代码做修改。这是通过 `esc` 函数的对表达式“转义”完成的：

```julia
macro time(ex)
    ...
    local val = $(esc(ex))
    ...
end
```

这样，封装的表达式就不会被宏展开机制处理，能够正确的在宏调用环境中解析。

必要时这个转义机制可以用来“破坏”卫生，从而引入或操作自定义变量。下例在调用环境中宏将 `x` 设置为 0 ：

```julia
macro zerox()
  return esc(:(x = 0))
end

function foo()
  x = 1
  @zerox
  x  # is zero
end
```

应审慎使用这种操作。

### 非标准字符串文本

[字符串](https://www.w3cschool.cn/julia/string-learning.html)中曾讨论过带标识符前缀的字符串文本被称为非标准字符串文本，它们有特殊的语义。例如：

- `r"^\s*(?:#|$)"` 生成正则表达式对象而不是字符串
- `b"DATA\xff\u2200"` 是字节数组文本 `[68,65,84,65,255,226,136,128]`

事实上，这些行为不是 Julia 解释器或编码器内置的，它们调用的是特殊名字的宏。例如，正则表达式宏的定义如下：

```julia
macro r_str(p)
  Regex(p)
end
```

因此，表达式 `r"^\s*(?:#|$)"` 等价于把下列对象直接放入语法树：

```julia
Regex("^\\s*(?:#|\$)")
```

这么写不仅字符串文本短，而且效率高：正则表达式需要被编译，而 `Regex` 仅在 *代码编译时* 才构造，因此仅编译一次，而不是每次执行都编译。下例中循环中有一个正则表达式：

```julia
for line = lines
  m = match(r"^\s*(?:#|$)", line)
  if m == nothing
    # non-comment
  else
    # comment
  end
end
```

如果不想使用宏，要使上例只编译一次，需要如下改写：

```julia
re = Regex("^\\s*(?:#|\$)")
for line = lines
  m = match(re, line)
  if m == nothing
    # non-comment
  else
    # comment
  end
end
```

由于编译器优化的原因，上例依然不如使用宏高效。但有时，不使用宏可能更方便：要对正则表达式内插时必须使用这种麻烦点儿的方式；正则表达式模式本身是动态的，每次循环迭代都会改变，生成新的正则表达式。

不止非标准字符串文本，命令文本语法（ `echo "Hello, $person"`）也是用宏实现的：

```julia
macro cmd(str)
  :(cmd_gen($shell_parse(str)))
end
```

当然，大量复杂的工作被这个宏定义中的函数隐藏了，但是这些函数也是用 Julia 写的。你可以阅读源代码，看看它如何工作。它所做的事儿就是构造一个表达式对象，用于插入到你的程序的语法树中。

## 反射

除了使用元编程语法层面的反思，朱丽亚还提供了一些其他的运行时反射能力。

**类型字段** 数据类型的域的名称（或模块成员）可以使用 `names` 命令来询问。例如，给定以下类型：

```julia
type Point
  x::FloatingPoint
  y
end
```

`names(Point)` 将会返回指针 `Any[:x, :y]`。在一个 `Point` 中每一个域的类型都会被存储在指针对象的 `types`域中：

```julia
typeof(Point)
DataType
Point.types
(FloatingPoint,Any)
```

**亚型**

任何数据类型的*直接*亚型可以使用 `subtypes(t::DataType)` 来列表查看。例如，抽象数据类型 `FloatingPoint` 包含四种（具体的）亚型：：

```julia
subtypes(FloatingPoint)
```

任何一个抽象的亚型也将被列入此列表中，但其进一步的亚型则不会；“亚型”的递归应用程序允许建立完整的类型树。

**类型内部**

当使用到 C 代码接口时类型的内部表示是非常重要的。`isbits(T::DataType)` 在 `T` 存储在 C 语言兼容定位时返回 true 。每一个域内的补偿量可以使用 `fieldoffsets(T::DataType)` 语句实现列表显示。

**函数方法**

函数内的所有方法可以通过 `methods(f::Function)` 语句列表显示出来。

**函数表示**

函数可以在几个表示层次上实现内部检查。一个函数的更低形式在使用 `code_lowered(f::Function, (Args...))`时是可用的，而类型推断的更低形式在使用 `code_typed(f::Function, (Args...))`时是可用的。

更接近机器的是，LLVM 的中间表示的函数是通过 `code_llvm(f::Function, (Args...))` 打印的，并且最终的由此产生的汇编指令在使用 `code_native(f::Function, (Args...)` 时是可用的。

