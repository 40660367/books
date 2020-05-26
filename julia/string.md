# Julia 字符串

## 字符串

Julia 中处理 [ASCII](http://zh.wikipedia.org/zh-cn/ASCII) 文本简洁高效，也可以处理 Unicode 。使用 C 风格的字符串代码来处理 ASCII 字符串，性能和语义都没问题。如果这种代码遇到非 ASCII 文本，会提示错误，而不是显示乱码。这时，修改代码以兼容非 ASCII 数据也很简单。

关于 Julia 字符串，有一些值得注意的高级特性：

- `String` 是个抽象类型，不是具体类型
- Julia 的 `Char` 类型代表单字符，是由 32 位整数表示的 Unicode 码位
- 与 Java 中一样，字符串不可更改：`String` 对象的值不能改变。要得到不同的字符串，需要构造新的字符串
- 概念上，字符串是从索引值映射到字符的*部分函数*，对某些索引值，如果不是字符，会抛出异常
- Julia 支持全部 Unicode 字符: 文本字符通常都是 ASCII 或 [UTF-8](http://zh.wikipedia.org/zh-cn/UTF-8) 的，但也支持其它编码

## 字符

`Char` 表示单个字符：它是 32 位整数，值参见 [Unicode 码位](http://zh.wikipedia.org/zh-cn/码位) 。 `Char` 必须使用单引号：

```julia
typeof('x')
```

可以把 `Char` 转换为对应整数值：

```julia
typeof(Int('x'))
```

在 32 位架构上， `typeof(ans)` 的类型为 `Int32` 。也可以把整数值转换为 `Char` ：

```julia
Char(120)
```

并非所有的整数值都是有效的 Unicode 码位，但为了性能， `char` 一般不检查其是否有效。如果你想要确保其有效，使用 `is_valid_char` 函数：

```julia
Char(0x110000)

#is_valid_char(0x110000)
```

目前，有效的 Unicode 码位为，从 `U+00` 至 `U+d7ff`，以及从 `U+e000` 至 `U+10ffff`。

可以用单引号包住 `\u` 及跟着的最多四位十六进制数，或者 `\U` 及跟着的最多八位（有效的字符，最多需要六位）十六进制数，来输入 Unicode 字符：

```julia
'\u0'

'\u78'

'\u2200'

'\U10ffff'
```

Julia 使用系统默认的区域和语言设置来确定，哪些字符可以被正确显示，哪些需要用 `\u` 或 `\U` 的转义来显示。除 Unicode 转义格式之外，所有 [C 语言转义的输入格式](http://en.wikipedia.org/wiki/C_syntax#Backslash_escapes)都能使：

```julia
println(Int('\0'))

println(Int('\t'))

println(Int('\n'))

println(Int('\e'))

println(Int('\x7f'))

println(Int('\177'))

println(Int('\xff'))
```

可以对 `Char` 值比较大小，也可以做少量算术运算：

```julia
println('A' < 'a')

println('A' <= 'a' <= 'Z')

println('A' <= 'X' <= 'Z')

println('x' - 'a')

println('A' + 1)
```

## 字符串基础

字符串文本应放在双引号 `"..."` 或三个双引号 `"""..."""` 中间：

```julia
str = "Hello, world.\n"

"""Contains "quote" characters"""
```

使用索引从字符串提取字符：

```julia
str = "Hello,.\n world"

println(str[1])

println(str[end])
```

Julia 中的索引都是从 1 开始的，最后一个元素的索引与字符串长度相同，都是 `n` 。

在任何索引表达式中，关键词 `end` 都是最后一个索引值（由 `endof(str)` 计算得到）的缩写。可以对字符串做 `end` 算术或其它运算：

```julia
str = "Hello, world.\n"

println(str[end-1])

println(str[end/2])

println(str[end/3])

println(str[end/4])
```

索引小于 1 或者大于 `end` ，会提示错误：

```julia
str = "Hello, world.\n"

println(str[0])

println(str[end+1])
```

使用范围索引来提取子字符串：

```julia
str = "Hello, world.\n"

println(str[4:9])

#str[k] 和 str[k:k] 的结果不同：
println(str[6])

println(str[6:6])
```

前者是类型为 `Char` 的单个字符，后者为仅有一个字符的字符串。在 Julia 中这两者完全不同。

## Unicode 和 UTF-8

Julia 完整支持 Unicode 字符和字符串。正如上文所讨论的在字符文本中， Unicode 码位可以由 `\u` 和 `\U` 来转义，也可以使用标准 C 的转义序列。它们都可以用来写字符串文本：

```julia
s = "\u2200 x \u2203 y"
```

非 ASCII 字符串文本使用 UTF-8 编码。 UTF-8 是一种变长编码，意味着并非所有的字符的编码长度都是相同的。在 UTF-8 中，码位低于 `0x80 (128)` 的字符即 ASCII 字符，编码如在 ASCII 中一样，使用单字节；其余码位的字符使用多字节，每字符最多四字节。这意味着 UTF-8 字符串中，并非所有的字节索引值都是有效的字符索引值。如果索引到无效的字节索引值，会抛出错误：

```julia
s = "\u2200 x \u2203 y"

println(s[1])

println(s[2])

println(s[3])

println(s[4])
```

上例中，字符 `∀` 为 3 字节字符，所以索引值 2 和 3 是无效的，而下一个字符的索引值为 4。

由于变长编码，字符串的字符数（由 `length(s)` 确定）不一定等于字符串的最后索引值。对字符串 `s` 进行索引，并从 1 遍历至 `endof(s)` ，如果没有抛出异常，返回的字符序列将包括 `s` 的序列。因而 `length(s) <= endof(s)`。下面是个低效率的遍历 `s` 字符的例子：

```julia
s = "\u2200 x \u2203 y"

for i = 1:12
     try
       println(s[i])
     catch
       # ignore the index error
       println("out of range")
     end
end
```

所幸我们可以把字符串作为遍历对象，而不需处理异常：

```julia
s = "\u2200 x \u2203 y"

for c in s
    println(c)
end
```

Julia 不只支持 UTF-8 ，增加其它编码的支持也很简单。特别是，Julia 还提供了 `utf16string` 和 `utf32string` 类型，由 `utf16(s)`和 `utf32(s)`函数分别支持 UTF-16 和 UTF-32 编码。它还为 UTF-16 或 UTF-32 字符串提供了别名 `WString` 和 `wstring(s)`，两者的选择取决于 `Cwchar_t` 大小。有关 UTF-8 的讨论，详见字节数组文本。

## 内插

字符串连接是最常用的操作：

```julia
greet = "Hello"

whom = "world"

string(greet, ", ", whom, ".\n")
```

像 Perl 一样， Julia 允许使用 `$` 来内插字符串文本：

```julia
"$greet, $whom.\n"
```

系统会将其重写为字符串文本连接。

`$` 将其后的最短的完整表达式内插进字符串。可以使用小括号将任意表达式内插：

```julia
"1 + 2 = $(1 + 2)"
```

字符串连接和内插都调用 `string` 函数来把对象转换为 `String` 。与在交互式会话中一样，大多数非 `String` 对象被转换为字符串：

```julia
v = [1,2,3]

"v: $v"
```

`Char` 值也可以被内插到字符串中：

```julia
c = 'x'

"hi, $c"
```

要在字符串文本中包含 `$` 文本，应使用反斜杠将其转义：

```julia
print("I have \$100 in my account.\n")
```

## 一般操作

使用标准比较运算符，按照字典顺序比较字符串：

```julia
"abracadabra" < "xylophone"

"abracadabra" == "xylophone"

"Hello, world." != "Goodbye, world."

"1 + 2 = 3" == "1 + 2 = $(1 + 2)"
```

使用 `search` 函数查找某个字符的索引值：

```julia
search("xylophone", 'x')

search("xylophone", 'p')

search("xylophone", 'z')
```

可以通过提供第三个参数，从此偏移值开始查找：

```julia
search("xylophone", 'o')

search("xylophone", 'o', 5)

search("xylophone", 'o', 8)
```

另一个好用的处理字符串的函数 `repeat` ：

```julia
repeat(".:Z:.", 10)
```

其它一些有用的函数：

- `endof(str)` 给出 `str` 的最大（字节）索引值
- `length(str)` 给出 `str` 的字符数
- `i = start(str)` 给出第一个可在 `str` 中被找到的字符的有效索引值（一般为 1 ）
- `c, j = next(str,i)` 返回索引值 `i` 处或之后的下一个字符，以及之后的下一个有效字符的索引值。通过 `start` 和 `endof` ，可以用来遍历 `str` 中的字符
- `ind2chr(str,i)` 给出字符串中第 i 个索引值所在的字符，对应的是第几个字符
- `chr2ind(str,j)` 给出字符串中索引为 i 的字符，对应的（第一个）字节的索引值

## 非标准字符串文本

Julia 提供了[*非标准字符串文本*](http://julia-cn.readthedocs.org/zh_CN/latest/manual/metaprogramming/#man-non-standard-string-literals2) 。它在正常的双引号括起来的字符串文本上，添加了前缀标识符。下面将要介绍的正则表达式、字节数组文本和版本号文本，就是非标准字符串文本的例子。[*元编程*](https://www.w3cschool.cn/julia/cell-code.md)章节有另外的一些例子。

### 正则表达式

Julia 的正则表达式 (regexp) 与 Perl 兼容，由 [PCRE](http://www.pcre.org/) 库提供。它是一种非标准字符串文本，前缀为 `r` ，最后面可再跟一些标识符。最基础的正则表达式仅为 `r"..."` 的形式：

```julia
r"^\s*(?:#|$)"

typeof(ans)
Regex (constructor with 3 methods)
```

检查正则表达式是否匹配字符串，使用 `ismatch` 函数：

```julia
ismatch(r"^\s*(?:#|$)", "not a comment")

ismatch(r"^\s*(?:#|$)", "# a comment")
```

`ismatch` 根据正则表达式是否匹配字符串，返回真或假。 `match`函数可以返回匹配的具体情况：

```julia
match(r"^\s*(?:#|$)", "not a comment")

match(r"^\s*(?:#|$)", "# a comment")
```

如果没有匹配， `match` 返回 `nothing`，这个值不会在交互式会话中打印。除了不被打印，这个值完全可以在编程中正常使用：

```julia
m = match(r"^\s*(?:#|$)", line)
if m == nothing
  println("not a comment")
else
  println("blank or comment")
end
```

如果匹配成功， `match` 的返回值是一个 `RegexMatch` 对象。这个对象记录正则表达式是如何匹配的，包括类型匹配的子字符串，和其他捕获的子字符串。本例中仅捕获了匹配字符串的一部分，假如我们想要注释字符后的非空白开头的文本，可以这么写：

```julia
m = match(r"^\s*(?:#\s*(.*?)\s*$|$)", "# a comment ")
```

当调用 `match` 时，你可以选择指定一个索引，它指示在哪里开始搜索。比如:

```julia
m = match(r"[0-9]","aaaa1aaaa2aaaa3",1)

m = match(r"[0-9]","aaaa1aaaa2aaaa3",6)

m = match(r"[0-9]","aaaa1aaaa2aaaa3",11)
```

可以在 `RegexMatch` 对象中提取下列信息：

- 完整匹配的子字符串： `m.match`
- 捕获的子字符串组成的字符串多元组： `m.captures`
- 完整匹配的起始偏移值： `m.offset`
- 捕获的子字符串的偏移值向量： `m.offsets`

对于没匹配的捕获，`m.captures` 的内容不是子字符串，而是 `nothing` ，`m.offsets` 为 0 偏移（Julia 中的索引值都是从 1 开始的，因此 0 偏移值表示无效）：

```julia
m = match(r"(a|b)(c)?(d)", "acd")

m.match

m.captures

m.offset

m.offsets

m = match(r"(a|b)(c)?(d)", "ad")

m.match

m.captures

m.offset

m.offsets
```

可以把结果多元组绑定给本地变量：

```julia
first, second, third = m.captures; first
```

可以在右引号之后，使用标识符 `i`,`m`, `s`及 `x` 的组合，来修改正则表达式的行为。这几个标识符的用法与 Perl 中的一样，详见 [perlre manpage](http://perldoc.perl.org/perlre.html#Modifiers) ：


i   不区分大小写

m   多行匹配。 "^" 和 "$" 匹配多行的起始和结尾

s   单行匹配。 "." 匹配所有字符，包括换行符, 一起使用时，例如 r""ms 中， "." 匹配任意字符，而 "^" 与 "$" 匹配字符串中新行之前和之后的字符

x   忽略大多数空白，除非是反斜杠。可以使用这个标识符，把正则表达式分为可读的小段。 '#' 字符被认为是引入注释的元字符

例如，下面的正则表达式使用了所有选项：

```julia
r"a+.*b+.*?d$"ism

match(r"a+.*b+.*?d$"ism, "Goodbye,\nOh, angry,\nBad world\n")
```

Julia 支持三个双引号所引起来的正则表达式字符串，即 `r"""..."""` 。这种形式在正则表达式包含引号或换行符时比较有用。

... 三重引号的正则字符串，形式为 `r"""..."""`，也是 ... 支持的（可能对于含有 ... 等式标记或换行的正则表达式是方便的）。

## 字节数组文本

另一类非标准字符串文本为 `b"..."` ，可以表示文本化的字节数组，如 `Uint8` 数组。习惯上，非标准文本的前缀为大写，会生成实际的字符串对象；而前缀为小写的，会生成非字符串对象，如字节数组或编译后的正则表达式。字节表达式的规则如下：

- ASCII 字符与 ASCII 转义符生成一个单字节
- \x 和八进制转义序列生成对应转义值的字节
- Unicode 转义序列生成 UTF-8 码位的字节序列

三种情况都有的例子：

```julia
b"DATA\xff\u2200"
```

ASCII 字符串 “DATA” 对应于字节 68, 65, 84, 65 。 `\xff` 生成的单字节为 255 。Unicode 转义 `\u2200` 按 UTF-8 编码为三字节 226, 136, 128 。注意，字节数组的结果并不对应于一个有效的 UTF-8 字符串，如果把它当作普通的字符串文本，会得到语法错误：

```julia
"DATA\xff\u2200"
```

`\xff` 和 `\uff` 也不同：前者是*字节 255* 的转义序列；后者是*码位 255* 的转义序列，将被 UTF-8 编码为两个字节：

```julia
b"\xff"

b"\uff"
```

在字符文本中，这两个是相同的。 `\xff` 也可以代表码位 255，因为字符*永远*代表码位。然而在字符串中，`\x` 转义永远表示字节而不是码位，而 `\u` 和 `\U` 转义永远表示码位，编码后为 1 或多个字节。

## 版本号文字

版本号可以很容易地用非标准字符串的形式 `v"..."` 表示。版本号会遵循[语义版本](http://semver.org/)的规范创建 `VersionNumber` 对象，因此版本号主要是由主版本号，次版本号和补丁的值决定的，其后是预发布和创建的数字注释。例如，`v"0.2.1-rc1+win64"` 可以被分块解释为主版本 `0`，次要版本 `2`，补丁版本 `1`，预发布 RC1 和创建为 Win64。当输入一个版本号时，除了主版本号的其余字段都是可选的，因此，会出现例如 `v"0.2"` 与 `v"0.2.0"` 等效（空预发布/创建注释），`v"2"` 与 `v"2.0.0"` 等效，等等。

`VersionNumber` 对象大多是能做到容易且准确地比较两个（或更多）的版本。例如，恒定的 `VERSION` 把 Julia 版本号作为一个 `VersionNumber` 对象管理，因此可以使用简单的语句定义一些特定版本的行为，例如：

```julia
if v"0.2" <= VERSION < v"0.3-"
    # do something specific to 0.2 release series
end
```

既然在上面的示例中使用了非标准的版本号 `v"0.3-"`,它使用了一个后连接号：此符号是一个 Julia 扩展的标准符号，它是用来表示一个低于任何 0.3 发行版的版本，其中包括其所有的预发行版本。所以在上面的例子中的代码只会运行稳定在 `0.2` 版本，并不能运行在这样的版本 `v"0.3.0-rc1"`。为了允许它也在不稳定的（即预发行版）0.2 版上运行，较低的检查应修改为 `v"0.2-" <= VERSION`。

另一个非标准版规范扩展允许对使用尾部 `+` 来表达一个上限构建版本，例如 `VERSION > "v"0.2-rc1+"` 可以被用来表示任何版本在 `0.2-rc1` 之上且任何创建形式的版本：对于版本 `v"0.2-rc1+win64"` 将返回 false ,而对于 `v"0.2-rc2"` 会返回 true 。

使用这种特殊的版本比较是好的尝试（特别是，尾随 `-` 应该总是被使用在上限规范，除非有一个很好的理由不去这样），但这样的形式不得被当作任何的实际版本号使用，因为在语义版本控制方案上它们是非法的。

除了用于 `VERSION` 常数，`VersionNumber` 对象还广泛应用于 `Pkg` 模块，来指定包的版本和它们的依赖关系。
