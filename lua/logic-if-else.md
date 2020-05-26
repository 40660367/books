# Lua if...else语句

`if`语句后面可以跟一个可选的`else`语句，该语句在布尔表达式为`false`时执行。

## 语法

Lua编程语言中`if...else`语句的语法是 - 

```lua
if(boolean_expression)
then
   --[ statement(s) will execute if the boolean expression is true --]
else
   --[ statement(s) will execute if the boolean expression is false --]
end
```

如果布尔表达式的计算结果为`true`，那么将执行`if`代码块，否则将执行`else`中的代码块。

Lua编程语言假定布尔`true`和`non-nil`值的任意组合为`true`，如果它是布尔`false`或`nil`，则假定为`false`值。 需要注意的是，在Lua中，零将被视为`true`。

**流程图**

![img](https://www.yiibai.com/uploads/article/2018/12/06/151756_55719.jpg)

**示例**

文件名:logic-if-else.lua

```lua
--[ local variable definition --]
a = 100;

--[ check the boolean condition --]

if( a < 20 )
then
   --[ if condition is true then print the following --]
   print("a is less than 20" )
else
   --[ if condition is false then print the following --]
   print("a is not less than 20" )
end

print("value of a is :", a)
```

```bash
lua /share/lesson/lua/logic-if-else.lua
```

康康

## if…else if…else语句

`if`语句后面可以跟一个`else if...else`语句，这对于使用单个`if...else if`语句测试各种条件非常有用。

使用`if`，`else if`，`else`语句时，需要记住几点 - 

- `if`语句有零个或一个`else`语句，它必须在`else if`语句之后。
- `if`语句有零或多个`else if`语句，并且它们必须在`else`语句之前。
- 当有一个`if else`匹配成功，其余的其他`if`或者`if else`都不会再测试。

**语法**

Lua编程语言中`if ... else if`语句的语法是

```lua
if(boolean_expression 1)
then
   --[ Executes when the boolean expression 1 is true --]

else if( boolean_expression 2)
   --[ Executes when the boolean expression 2 is true --]

else if( boolean_expression 3)
   --[ Executes when the boolean expression 3 is true --]
else 
   --[ executes when the none of the above condition is true --]
end
```

**示例代码**

文件名:logic-if-else-if-else.lua

```lua
--[ local variable definition --]
a = 100

--[ check the boolean condition --]

if( a == 10 )
then
   --[ if condition is true then print the following --]
   print("Value of a is 10" )
elseif( a == 20 )
then   
   --[ if else if condition is true --]
   print("Value of a is 20" )
elseif( a == 30 )
then
   --[ if else if condition is true  --]
   print("Value of a is 30" )
else
   --[ if none of the conditions is true --]
   print("None of the values is matching" )
end
print("Exact value of a is: ", a )
```

```bash
lua /share/lesson/lua/logic-ifelse.lua
```

康康