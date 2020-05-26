# Lua 基本语法

## 注释

### 单行注释

两个减号`--`是单行注释:

```lua
-- This is a single line comment
```

### 多行注释

```lua
--[[
 多行注释
 多行注释
 --]]
```

## Lua 令牌标记(token)

Lua程序由各种标记组成，标记可以是关键字，标识符，常量，字符串文字或符号。 例如，

以下Lua语句由三个标记组成:

```lua
io.write("Hello world, from ",_VERSION,"!\n")
```

独立标记是

```lua
io.write
(
   "Hello world, from ",_VERSION,"!\n"
)
```

## 标示符

Lua 标示符用于定义一个变量，函数获取其他用户定义的项。标示符以一个字母 A 到 Z 或 a 到 z 或下划线 _ 开头后加上0个或多个字母，下划线，数字（0到9）。

最好不要使用下划线加大写字母的标示符，因为Lua的保留字也是这样的。

Lua 不允许使用特殊字符如 @, $, 和 % 来定义标示符。 Lua 是一个区分大小写的编程语言。因此在 Lua 中 Lua与 lua是两个不同的标示符。以下列出了一些正确的标示符：

```lua
mohd         zara      abc     move_name    a_123
myname50     _temp     j       a23b9        retVal
```

## 关键词

以下列出了 Lua 的保留关键字。保留关键字不能作为常量或变量或其他用户自定义标示符：

| and      | break | do    | else   |
| -------- | ----- | ----- | ------ |
| elseif   | end   | false | for    |
| function | if    | in    | local  |
| nil      | not   | or    | repeat |
| return   | then  | true  | until  |
| while    | goto  |       |        |

一般约定，以下划线开头连接一串大写字母的名字（比如 _VERSION）被保留用于 Lua 内部全局变量。

## Lua空白符

只包含空格(可能带有注释)的行称为空行，Lua解释器完全忽略它。

空白符是Lua用来描述空格，制表符，换行符和注释的术语。 空格符将语句的一部分与另一部分分开，并使解释器能够识别语句中的一个元素(如`int`结束)和下一个元素的开始位置。 因此，在以下声明中

```lua
local age
```

在`local`和`age`之间必须至少有一个空格字符(通常是空格)，以便解释器能够区分它们。 另一方面，在以下声明中 

```lua
fruit = apples + oranges   --get the total fruit
```

在`fruit`和`=`之间，或`=`和`apples`之间不需要空白字符，但如果希望增加可读性，可以自由添加一些空白字符。

## 全局变量

在默认情况下，变量总是认为是全局的。

全局变量不需要声明，给一个变量赋值后即创建了这个全局变量，访问一个没有初始化的全局变量也不会出错，只不过得到的结果是：nil。

```lua
-- 访问未初始化的全局变量b
print(b)
```

```lua
-- 初始化全局变量b并进行访问
b=10
print(b)
```

```lua
-- 删除一个全局变量，只需要将变量赋值为nil
b = nil
print(b)
```

这样变量b就好像从没被使用过一样。换句话说, 当且仅当一个变量不等于nil时，这个变量即存在。

