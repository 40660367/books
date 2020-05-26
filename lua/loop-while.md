# Lua while循环

只要给定条件为真，Lua编程语言中的`while`循环语句就会重复执行目标语句。

## 语法

Lua编程语言中`while`循环的语法：

```lua
while(condition)
do
   statement(s)
end
```

这里，`statement(s)`可以是一个语句或多个语句块。 `condition`可以是任何表达式，`true`是任何非零值。 当条件为真时，循环迭代。

当条件变为假时，程序控制传递到紧接循环之后的行。

**流程图**



在这里，需要注意的是`while`循环可能根本不会被执行。当测试条件并且结果为假时，将跳过循环体并且将执行`while`循环之后的第一个语句。

**示例**

文件名:loop-while.lua

```lua
a = 10

while( a < 50 )
do
   print("value of a:", a)
   a = a+1
end
```

```bash
lua /share/lesson/lua/loop-while.lua
```

康康