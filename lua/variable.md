# Lua 变量(variable)

变量是程序可以操作的存储区域的名称。 它可以包含不同类型的值，包括函数和表。

变量的名称可以由字母，数字和下划线字符组成。 它必须以字母或下划线开头。 大写和小写字母是不同的，因为Lua区分大小写。Lua中有八种基本类型的值。

在Lua中，虽然没有可变数据类型，但根据变量的范围有三种类型。

- **全局变量** - 所有变量都被视为全局变量，除非明确声明为局部变量。
- **局部变量** - 当为变量指定类型为`local`时，其范围受函数范围限制。
- **表字段** - 这是一种特殊类型的变量，可以保存除`nil`之外的任何内容，包括函数。

## Lua变量定义

变量定义告诉解释器为变量创建存储的位置和数量。 变量定义具有可选类型，并包含该类型的一个或多个变量的列表，如下所示 - 

```lua
type variable_list;
```

这里，`type`是可选的本地或全局类型，而`variable_list`可以包含一个或多个由逗号分隔的标识符名称。 这里显示了一些有效的声明 - 

```lua
local    i, j
local    i
local    a,c
```

行`local i，j`都声明并定义变量`i`和`j`; 它指示解释器创建名为`i`，`j`的变量，并将范围限制为局部。

变量可以在声明中初始化(分配初始值)。 初始化程序包含一个等号，后跟一个常量表达式，如下所示 - 

```lua
type variable_list = value_list;
```

同样的一些示例如下 - 

```lua
local d , f = 5 ,10     --declaration of d and f as local variables. 
d , f = 5, 10;          --declaration of d and f as global variables. 
d, f = 10               --[[declaration of d and f as global variables. 
                           Here value of f is nil --]]
```

对于没有初始化程序的定义：具有静态存储持续时间的变量使用`nil`隐式初始化。

## Lua变量声明

正如在上面的示例中所看到的，多个变量的赋值遵循`variable_list`和`value_list`格式。 在上面的例子中，`local d , f = 5 ,10`在`variable_list`中就是`d`和`f`，在`value_list`中就是`5`和`10`。

Lua中的值赋值类似于`variable_list`中的第一个变量，`value_list`中的第一个值，依此类推。 因此，`d`的值为`5`，`f`的值为`10`。

**示例**

看看以下示例，其中变量已在顶部声明，但它们已在主函数内定义和初始化

文件名:variable.lua

```lua
-- Variable definition:
local a, b

-- Initialization
a = 10
b = 30

print("value of a:", a)

print("value of b:", b)

-- Swapping of variables
b, a = a, b

print("value of a:", a)

print("value of b:", b)

f = 70.0/3.0
print("value of f", f)
```

```bash
lua /share/lesson/lua/variable.lua
```

康康

## Lua 左值和右值

Lua中有两种表达方式

- **左值** - 引用内存位置的表达式称为“左值”表达式。 左值可以显示为赋值的左侧或右侧。
- **右值** - 术语右值是指存储在内存中某个地址的数据值。 右值是一个不能赋值的表达式，所以右值可能出现在右侧，但不会出现在赋值的左侧。

变量是左值，因此可能出现在赋值的左侧。 数字文字是右值，因此可能无法分配，也不能出现在左侧。 以下是有效的声明 - 

```lua
g = 20
```

但是以下不是有效的语句，会产生构建时错误 - 

```lua
10 = 20
```

在Lua编程语言中，除了上述类型的赋值之外，在同一个语句中可以有多个左值和右值。 如下所示。

```lua
g,l = 20,30
```

在上面的语句中，`20`分配给变量`g`，`30`分配给变量`l`。