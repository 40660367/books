# Lua repeat...until循环

与在循环顶部测试循环条件的`for`和`while`循环不同，Lua编程语言中的`repeat...until`循环在底部检查循环的条件。

`repeat...until`循环类似于`while`循环，但是`do...while`循环保证至少执行一次。

## 语法

Lua编程语言中`repeat ... until`循环的语法如下 - 

```lua
repeat
   statement(s)
until( condition )
```

请注意，`condition`表达式在循环的末尾，因此循环中的语句在测试条件之前执行一次。
如果条件为假，则控制流跳回来执行，循环中的语句再次执行。 重复此过程直到给定条件变为真。

**流程图**

![img](https://www.yiibai.com/uploads/article/2018/12/06/144212_10443.jpg)

**示例代码**

文件名:loop-repeat-until.lua

```lua
--[ local variable definition --]
a = 10

--[ repeat loop execution --]
repeat
   print("value of a:", a)
   a = a + 1
until( a > 15 )
```

```bash
lua /share/lesson/lua/loop-repeat-until.lua
```

康康