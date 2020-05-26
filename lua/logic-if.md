# Lua if语句 			

`if`语句由一个布尔表达式后跟一个或多个语句组成。

## 语法

Lua编程语言中`if`语句的语法:

```lua
if(boolean_expression)
then
   --[ statement(s) will execute if the boolean expression is true --]
end
```

如果布尔表达式的计算结果为`true`，那么将执行`if`语句中的代码块。 如果布尔表达式的计算结果为`false`，则将执行`if`语句结束后(在结束大括号之后)的第一组代码。

Lua编程语言假定布尔`true`和`non-nil`值的任意组合为`true`，如果它是布尔`false`或`nil`，则假定为`false`值。 需要注意的是，在Lua中，零将被视为`true`。

**流程图**

![image-20200418195922560](./images/logic-if.png)

**示例代码**

文件名:logic-if.lua

```lua
--[ local variable definition --]
a = 10;

--[ check the boolean condition using if statement --]

if( a < 20 )
then
   --[ if condition is true then print the following --]
   print("a is less than 20" );
end

print("value of a is :", a);
```

```bash
lua /share/lesson/lua/logic-if.lua
```

康康