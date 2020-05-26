# Julia 交互

## 交互

Julia 有一个全功能的交互式命令行 REPL （read-eval-print 循环）内置在可执行的 `julia` 内。除了允许快速并且简易的评定 Julia 语句，他还有一个可搜索历史的功能，tab 补齐功能，以及更多有用的快捷键，和专门的帮助，并且还有 shell 模式。REPL 能够通过简单的无参数调用或双击执行来进行启动:

```
julia
               _
   _       _ _(_)_     |  A fresh approach to technical computing
  (_)     | (_) (_)    |  Documentation: http://docs.julialang.org
   _ _   _| |_  __ _   |  Type "help()" to list help topics
  | | | | | | |/ _` |  |
  | | |_| | | | (_| |  |  Version 0.3.0-prerelease+2834 (2014-04-30 03:13 UTC)
 _/ |\__'_|_|_|\__'_|  |  Commit 64f437b (0 days old master)
|__/                   |  x86_64-apple-darwin13.1.0

julia>
```

如果要退出互动会话，敲击 `^D` 即 control 键加上 d 键 - 或者是编辑 `quit()`，然后在敲击回车键。REPL 会给你 `julia>` 提示。

## 不同的提示模式

### Julia 模式

REPL 有四种主要的操作模式。第一种并且最常见的一种是 Julian 提示。它是默认的操作模式；每一行的开始都会是 `julia>` 。在这里，你可以输入 Julia 表达式。在一个完整的表达式已经输入好之后敲打回车将会评估该条目并且显示最后一个表达式的结果。

```julia
string(1 + 2)
```

这里有许多独特的特点可以来进行交互工作。除了显示结果外，REPL 同样将结果绑定到变量 `ans`。 在该行尾部的分号可以用作一个标志来抑制显示结果。

```julia
string(3 * 4);
```

```julia
ans
```

### 帮助模式

当指针在一行的开始位置时，敲击 `?` 提示将会变为帮助模式。Julia 将会尝试打印在帮助模式中的帮助或是文档：

```
    ? # upon typing ?, the prompt changes (in place) to: help>

    help> string
    Base.string(xs...)

       Create a string from any values using the "print" function.
```

除了方法名，完成方法调用可以看到哪一个方法被指定的参数调用了。宏,类型和变量也可以查询。

```
help> string(1)

help> @printf

help> String

想要退出帮助模式可以在一行的开始按下退格键。
```

### Shell 模式

帮助模式适用于快速访问文档，另一个常见任务是使用系统 Shell 来执行系统命令。就像当光标在一行的开始位置时 `?` 来进入帮助模式，使用分号 `(;)` 可以进入 shell 模式。并且想要退出模式时可以在一行的开始按下退格键。

```
; # upon typing ;, the prompt changes (in place) to: shell>

shell> echo hello
hello
```

### 查找模式

在所有以上的方法中，所有执行行会被保存到历史文件当中，并且能够被查找。为了初始化一个对先前历史的增量搜索，敲击 `^R` - control 键加上键盘上的 `r` 键。提示会被更改为 `(reverse-i-search)':`，并且随着你敲击，查询请求将会出现在引用中。达到匹配要求的最近一次的结果将会被动态更新在右面的控制台中。想要找到更老的结果就使用相同查询，然后再敲击一次 `^R`。

`^R` 是反向查询，而 `^S` 是正向查询，提示为 `(i-search)':`。这两个可以相互结合使用来相对的移动到前一个或是后一个匹配结果。

## 键绑定

Julia REPL 很好的使用了键绑定功能。上面已经介绍了很多种控制键绑定（`^D` 用来退出, `^R` 和 `^S` 用来查询），但是这里还有更多的键绑定。除了控制键，这里还有很多 meta - 键绑定。这些键绑定因平台的不同而不同，但是大部分终端默认使用 alt - 或 option - 选一个键来发送 meta - 键（或是通过配置）。

| Program control     |                                             |
| :------------------ | :------------------------------------------ |
| ^D                  | 退出（当缓冲区为空）                        |
| ^C                  | 中断或是取消                                |
| Return/Enter, ^J    | 新的一行并且如果上一行已经完成则执行上一行  |
| meta-Return/Enter   | 新的一行并且不执行                          |
| ? or ;              | 进入帮助或是 Shell 模式（在一行的起始位置） |
| ^R, ^S              | 增量历史搜索                                |
| **Cursor movement** |                                             |
| Right arrow, ^F     | 向右移动一个字符                            |
| Left arrow, ^B      | 向左移动一个字符                            |
| Home, ^A            | 移动到该行的起始                            |
| End, ^E             | 移动到该行的末尾                            |
| ^P                  | 改变先前或下一个历史条目                    |
| ^N                  | 改变到下一个历史条目                        |
| Up arrow            | 移动到上面一行（或是先前的历史条目）        |
| Down arrow          | 移动到下面一行（或是之后的历史条目）        |
| Page-up             | 切换到上一条光标前的文本匹配的历史条目      |
| Page-down           | 切换到下一条光标前的文本匹配的历史条目      |
| meta-F              | 向右移动一个词                              |
| meta-B              | 向左移动一个词                              |
| **Editing**         |                                             |
| Backspace, ^H       | 删除前一个字符                              |
| Delete, ^D          | 向后删除一个字符（当缓冲区有文本时）        |
| meta-Backspace      | 删除前一个词                                |
| meta-D              | 向后删除一个词                              |
| ^W                  | 删除先前的直到最近的空白的所有文本          |
| ^K                  | "杀死"到行的末尾，将文本放至缓冲区          |
| ^Y                  | 从 kill 缓冲区插入文本                      |
| ^T                  | 根据光标调换字符                            |
| Delete, ^D          | 向后删除一个字符（当缓冲区内有文本）        |

### 自定义快捷键

Julia REPL 的快捷键可以通过向 `REPL.setup_interface()` 传入字典类型的数据来实现自定义. 字典的关键字可以是字符, 也可以是字符串. 字符 `*` 代表默认默认操作. `^x` 代表快捷键 Control 键加 `x` 键. Meta 键加 `x` 键可以写作 `"\\Mx"`. 字典的数据必须是 `nothing` (代表忽略该操作), 或者参数为 `(PromptState, AbstractREPL, Char` 的函数. 例如, 为了实现绑定上下键到搜索历史记录, 可以把下面的代码加入到 `.juliarc.jl` :

```
import Base: LineEdit, REPL

const mykeys = {
# Up Arrow
"\e[A" => (s,o...)->(LineEdit.edit_move_up(s) || LineEdit.history_prev(s, LineEdit.mode(s).hist)),
# Down Arrow
"\e[B" => (s,o...)->(LineEdit.edit_move_up(s) || LineEdit.history_next(s, LineEdit.mode(s).hist))
}

Base.active_repl.interface = REPL.setup_interface(Base.active_repl; extra_repl_keymap = mykeys)
```

可供使用的按键和操作请参阅 `base/LineEdit.jl`.

## Tab 补全

在 Julia REPL (或者帮助模式下的 REPL), 可以输入函数或者类型名的前几个字符, 然后按 Tab 键来显示可能的选项::

```
stri
```

Tab 键也可以使 LaTeX 数学字符替换成 Unicode 并且显示可能的选项::

```
 \pi[TAB]
  π
  π = 3.1415926535897...

  e\_1[TAB] = [1,0]
  e₁ = [1,0]
  2-element Array{Int64,1}:
   1
   0

  e\^1[TAB] = [1 0]
  e¹ = [1 0]
  1x2 Array{Int64,2}:
   1  0

  \sqrt[TAB]2     # √ is equivalent to the sqrt() function
  √2
  1.4142135623730951

  \hbar[TAB](h) = h / 2\pi[TAB]
  ħ(h) = h / 2π
  ħ (generic function with 1 method)

  \h[TAB]
  \hat              \heartsuit         \hksearow          \hookleftarrow     \hslash
  \hbar             \hermitconjmatrix  \hkswarow          \hookrightarrow    \hspace
```
