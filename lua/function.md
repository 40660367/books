# Lua 函数(function)

函数是一组一起执行任务的语句。可以将代码划分组合为单独的函数。如何在不同的函数之间划分代码取决于开发者，但逻辑上这个划分通常是唯一的，所以每个函数都执行一个特定的任务。

Lua语言提供了许多程序可以调用的内置方法。 例如，`print()`方法打印在控制台中作为输入传递的参数。

函数也有类似的其它叫法，例如：方法或子例程或过程等。

## 定义函数

Lua编程语言中方法定义的一般形式如下 - 

```lua
optional_function_scope function function_name( argument1, argument2, argument3........, 
argumentn)

function_body

return result_params_comma_separated
end
```

Lua编程语言中的方法定义由方法头和方法体组成。以下是方法的所有部分 - 

- **可选函数范围** - 使用关键字`local`来限制函数的范围，或者忽略`scope`部分，这会变成一个全局函数。
- **函数名称** - 这是函数的实际名称。 函数名称和参数列表一起构成函数签名。
- **参数** - 参数就像一个占位符。 调用函数时，将值传递给参数。 该值称为实际参数或参数。 参数列表指的是方法的参数的类型，顺序和数量。 参数是可选的; 也就是说，方法的参数可有可无。
- **函数主体** - 方法体包含一组语句，用于定义方法的作用。
- **返回** - 在Lua中，可通过使用`return`关键字，后加逗号分隔返回值列表来返回多个值。

## 示例

以下是`max()`函数的定义。 此函数接受两个参数`num1`和`num2`，并返回两者的最大值 

```lua
--[[ function returning the max between two numbers --]]
function max(num1, num2)

   if (num1 > num2) then
      result = num1;
   else
      result = num2;
   end

   return result; 
end
```

## 函数参数

如果函数使用参数，它必须声明接受参数值的变量。 这些变量称为函数的形式参数。
形式参数的行为与函数内部的其他局部变量相似，并在进入函数时创建，并在退出时销毁。

## 调用函数

在创建Lua函数时，可以定义函数必须执行的操作。 要使用方法，可通过调用函数来执行定义的任务。

当程序调用一个函数时，程序控制会转移到调用的函数。调用的函数执行定义的任务，当执行其返回语句或达到其函数结束时，它将程序控制返回给主程序。

要调用函数，只需传递必需的参数和函数名称，如果函数有返回值，则可以存储返回的值。 例如

文件名:function-max.lua

```lua
function max(num1, num2)

   if (num1 > num2) then
      result = num1;
   else
      result = num2;
   end

   return result; 
end

-- calling a function
print("The maximum of the two numbers is ",max(122,313))
print("The maximum of the two numbers is ",max(12,31))
```

```bash
lua /share/lesson/lua/function-max.lua
```

康康

## 分配和传递函数

在Lua中，将函数赋值给变量，也可以将它们作为另一个函数的参数传递。 下面是一个简单的例子，实现在Lua中分配和传递函数作为参数。

文件名:function-pass.lua

```lua
myprint = function(param)
   print("This is my print function -   ##",param,"##")
end

function add(num1,num2,functionPrint)
   result = num1 + num2
   functionPrint(result)
end

myprint(10)
add(2,5,myprint)
```

```bash
lua /share/lesson/lua/function-pass.lua
```

康康

## 可变参数的函数

使用`...`作为参数在Lua中创建具有可变参数的函数。下面是通过函数计算返回平均值，并采用变量参数的示例。

文件名:function-varparm.lua

```lua
function average(...)
   result = 0
   local arg = {...}
   for i,v in ipairs(arg) do
      result = result + v
   end
   return result/#arg
end

print("The average is",average(10,5,3,4,5,6))
print("The average is",average(1,3,5,77))
print("The average is",average(1,3,5,123,4,3,22,11,421))
```

```bash
lua /share/lesson/lua/function-varparm.lua
```

康康