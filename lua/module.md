# Lua 模块(module)

模块是一个可以使用`require`加载的库，并且只有一个包含表的全局名称。 模块可以包含许多功能和变量。 所有这些函数和变量都包含在表中，表充当命名空间。 此外，一个良好的模块有必要的子句，以在使用`require`语句时返回此表。

## Lua模块的特色

模块中表的使用以多种方式，能够使用与操作任何其他Lua表相同的方式操作模块。 由于能够操作模块，它提供了其他语言需要特殊机制的额外功能。 由于Lua中模块的这种自由机制，用户可以通过多种方式调用Lua中的函数。 其中一些操作示例如下所示。

```lua
-- Assuming we have a module printFormatter
-- Also printFormatter has a funtion simpleFormat(arg)
-- Method 1
require "printFormatter"
printFormatter.simpleFormat("test")

-- Method 2
local formatter = require "printFormatter"
formatter.simpleFormat("test")

-- Method 3
require "printFormatter"
local formatterFunction = printFormatter.simpleFormat
formatterFunction("test")
```

在上面的示例代码中，可以看到Lua中的编程灵活性，没有任何特殊的附加代码。

## require函数

Lua提供了一个名为`require`的高级函数来加载所有必需的模块。 它保持尽可能简单，以避免有太多关于模块的信息来加载。 `require`函数只是将模块假定为一块代码，它定义了一些值，实际上是包含函数或表。

**示例**

考虑一个简单的例子，其中一个函数是数学函数。 将此模块称为`modulemath`，文件名为`modulemath.lua`。 

文件名:modulemath.lua

```bash
cd ~
cat > modulemath.lua << EOF

local modulemath =  {}

function modulemath.add(a,b)
   print(a+b)
end

function modulemath.sub(a,b)
   print(a-b)
end

function modulemath.mul(a,b)
   print(a*b)
end

function modulemath.div(a,b)
   print(a/b)
end

return modulemath
EOF
```

现在在另一个文件`module-test.lua`中访问此Lua模块，

文件名:moduletest.lua

```lua
mymathmodule = require("modulemath")
mymathmodule.add(20,20)
mymathmodule.sub(30,30)
mymathmodule.mul(20,20)
mymathmodule.div(30,30)
```

要运行此代码，需要将两个Lua文件放在同一目录中，或者，可以将模块文件放在包路径中，它需要额外的设置。 

```bash
cd ~
lua /share/lesson/lua/moduletest.lua
```

康康

**注意事项**

- 将运行的模块和文件放在同一目录中。
- 模块名称及其文件名应相同。
- 使用`require`函数返回模块，因此模块最好如上所示实现，尽管可以在其他地方找到其他类型的实现。
