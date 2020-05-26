# Lua 数据类型

Lua是一种动态类型语言，因此变量没有类型，只有值具有类型。 值可以存储在变量中，作为参数传递并作为结果返回。

在Lua中，虽然没有可变数据类型，但有值的类型。

 值的数据类型列表如下。

| 编号 | 值类型     | 描述                                                         |
| ---- | ---------- | ------------------------------------------------------------ |
| 1    | `nil`      | 用于区分值与某些数据或没有(`nil`)数据。                      |
| 2    | `boolean`  | 包括`true`和`false`作为值，通常用于条件检查。                |
| 3    | `number`   | 表示实数(双精度浮点)数字。                                   |
| 4    | `string`   | 表示字符数组。                                               |
| 5    | `function` | 表示用C语言或Lua编写的方法。                                 |
| 6    | `userdata` | 表示任意C语言数据。                                          |
| 7    | `thread`   | 表示独立的执行线程，它用于实现协同程序。                     |
| 8    | `table`    | 表示普通数组，符号表，集合，记录，图形，树等，并实现关联数组。 它可以保存任何值(除了`nil`)。 |

```lua
print(type("Hello world"))    --> string
print(type(10.4*3))           --> number
print(type(print))            --> function
print(type(type))             --> function
print(type(true))             --> boolean
print(type(nil))              --> nil
print(type(type(X)))          --> string
```

## 数字(number)

Lua 默认只有一种 number 类型 -- double（双精度）类型（默认类型可以修改 luaconf.h 里的定义），以下几种写法都被看作是 number 类型：

```lua
print(type(2))
print(type(2.2))
print(type(0.2))
print(type(2e+1))
print(type(0.2e-1))
print(type(7.8263692594256e-06))
```

## 字符串(string)

字符串由一对双引号或单引号来表示。

```lua
string1 = "this is string1"
string2 = 'this is string2'
print(string1,string2)
```

也可以用 2 个方括号 "[[]]" 来表示"一块"字符串。

```lua
link = [[

[Lua](http://www.lua.org/)

]]
print(link)
```

在对一个数字字符串上进行算术操作时，Lua 会尝试将这个数字字符串转成一个数字:

```lua
print("2" + 6)
print("2" + "6")
print("2 + 6")
print("-2e2" * "6")
```

```lua
-- 字符串连接使用的是 .. ，如：
print("a" .. 'b')
```

```lua
-- 使用 # 来计算字符串的长度，放在字符串前面
str1 = "www.lua.org"
print(#str1)
print(#"www.lua.org")
```

## 表(table)

在 Lua 里，table 的创建是通过"构造表达式"来完成，最简单构造表达式是{}，用来创建一个空表。也可以在表里添加一些数据，直接初始化表:

## 实例

```lua
-- 创建一个空的 table
local tbl1 = {}
 
-- 直接初始表
local tbl2 = {"apple", "pear", "orange", "grape"}
```

Lua 中的表（table）其实是一个"关联数组"（associative arrays），数组的索引可以是数字或者是字符串。

文件名:tableloop1.lua

```lua
a = {}
a["key"] = "value"
key = 1
a[key] = 99
a[key] = a[key] + 1
for k, v in pairs(a) do
    print(k .. " : " .. v)
end
```

```bash
lua /share/lesson/lua/tableloop1.lua
```

康康

不同于其他语言的数组把 0 作为数组的初始索引，在 Lua 里表的默认初始索引一般以 1 开始。

文件名:tableloop2.lua

```lua
local tbl = {"apple", "pear", "orange", "grape"}
for key, val in pairs(tbl) do
    print("Key", key)
end
```

```bash
lua /share/lesson/lua/tableloop2.lua
```

康康

table 不会固定长度大小，有新数据添加时 table 长度会自动增长，没初始的 table 都是 nil。

文件名:tableloop3.lua

```lua
a3 = {}
for i = 1, 10 do
    a3[i] = i
end
a3["key"] = "val"
print(a3["key"])
print(a3["none"])
```

```bash
lua /share/lesson/lua/tableloop3.lua
```

康康

## function（函数）

在 Lua 中，函数是被看作是"第一类值（First-Class Value）"，函数可以存在变量里:

文件名:function-firstclass.lua

```lua
function factorial1(n)
    if n == 0 then
        return 1
    else
        return n * factorial1(n - 1)
    end
end
print(factorial1(10))


f = factorial1
print(f(5))
```

```bash
lua /share/lesson/lua/function-firstclass.lua
```

康康

function 可以以匿名函数（anonymous function）的方式通过参数传递:

文件名:function-anonymous.lua

```lua
function testFun(tab,fun)
    for k ,v in pairs(tab) do
            print(fun(k,v));
    end
end


tab={key1="val1",key2="val2"};
testFun(tab,
function(key,val)--匿名函数
    return key.."="..val;
end
);
```

```bash
lua /share/lesson/lua/function-anonymous.lua
```

康康

## thread（线程）

在 Lua 里，最主要的线程是协同程序（coroutine）。它跟线程（thread）差不多，拥有自己独立的栈、局部变量和指令指针，可以跟其他协同程序共享全局变量和其他大部分东西。

线程跟协程的区别：线程可以同时多个运行，而协程任意时刻只能运行一个，并且处于运行状态的协程只有被挂起（suspend）时才会暂停。

## userdata（自定义类型）

userdata 是一种用户自定义数据，用于表示一种由应用程序或 C/C++ 语言库所创建的类型，可以将任意 C/C++ 的任意数据类型的数据（通常是 struct 和 指针）存储到 Lua 变量中调用。