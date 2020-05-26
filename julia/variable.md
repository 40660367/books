# Julia 变量

## 变量

在 Julia 中的一个变量是一个与一个值关联（或绑定）的名称。它的作用表现在当你想存储一个值（例如，你在进行一些数学运算后得到了一些值，你需要在之后使用到这些值）时。例如：

```julia
# 给变量 x 赋值为 10
x = 10
println(x)

# 用 x 的值做一些数学运算
println(x + 1)

# 重新给 x 赋值
x = 1 + 1
println(x)

# 您可以为变量赋给种类型的值，例如文本字符串等
x = "Hello World!"
println(x)
```

Julia 提供了极其灵活的变量命名系统。变量名区分大小写。

```julia
x = 1.0

y = -3

Z = "My string"

customary_phrase = "Hello world!"

UniversalDeclarationOfHumanRightsStart = "人人生而自由，在尊严和权力上一律平等。"

println(x,y,Z,customary_phrase,UniversalDeclarationOfHumanRightsStart)
```

也可以使用 Unicode 字符（UTF-8 编码）来命名：

```julia
δ = 0.00001

안녕하세요 = "Hello"

println(δ)
println(안녕하세요)
```

在 Julia REPL 和其他几个 Julia 编辑环境中，您可以通过输入反斜杠符号名称后再输入标签来键入很多 Unicode 数学符号。例如，变量名 `δ` 可以通过键入 `\delta` 键入，甚至可以通过输入 `\alpha` - *tab* - `\hat` - *tab* - `\_2` - *tab* 输入 `α̂₂` 。

Julia 甚至允许重新定义内置的常数

```julia
println(pi)
pi = 3
println(sqrt(100))
println(pi)
```
很显然, 不鼓励这样的做法。

## 可用的变量名

变量名必须以字母（a-z 或 A-Z），下划线，或一个 Unicode 编码指针中指向比 00A0 更大的指针子集开始；特别是 [Unicode 字符 ](http://www.fileformat.info/info/unicode/category/index.htm)Lu/Ll/Lt/Lm/Lo/Nl（字母），Sc/So （货币和其他符号），和其他一些可以看做字符的一些输入（例如 Sm 数学符号的子集）是允许的。首位之后的字符也包括 ！和数字（0-9 和其他字符 Nd/No ），以及其他 Unicode 编码指针：变音符号和其他修改标记（字母 Mn/Mc/Me/Sk），一些标点连接器（字母 PC），素数，和其他的一些字符。

运算符类似 `+` 也是有效的标识符，但需要特别解析。在某些情况下，运算符可以像变量一样使用；例如 `(+)` 是指增加功能，和 `(+) = f` 将重新定义这个运算。大多数的 Unicode 中缀操作符（在 Sm 中），如 `⊕` ，会被解析为中缀操作符，同时可以自定义方法（例如，你可以使用 `⊗ = kron` 定义 `⊕` 成为一个中缀 Kronecker 积）。

内置的关键字不能当变量名：

```julia
else = false #syntax: unexpected "else"
try = "No" #syntax: unexpected "="
```
## 命名规范

尽管 Julia 对命名本身只有很少的限制, 但尽量遵循一定的命名规范吧：

- 变量名使用小写字母
- 单词间使用下划线 (`'_'`) 分隔，但不鼓励
- 类型名首字母大写, 单词间使用驼峰式分隔.
- 函数名和宏名使用小写字母, 不使用下划线分隔单词.
- 修改参数的函数结尾使用 `!` . 这样的函数被称为 mutating functions 或 in-place functions
