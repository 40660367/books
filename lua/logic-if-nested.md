# Lua 嵌套if语句

在Lua编程中嵌套`if-else`语句是合法的，这意味着在一个`if`或`else if`语句中可以使用另一个`if`或`else if`语句。

**语法**

嵌套`if`语句的语法如下

```lua
if( boolean_expression 1)
then
   --[ Executes when the boolean expression 1 is true --]
   if(boolean_expression 2)
   then
      --[ Executes when the boolean expression 2 is true --]
   end
end
```

使用与嵌套`if`语句类似的方式嵌套`if else`语句。

**示例**

文件名:loop-if-nested.lua

```lua
--[ local variable definition --]
a = 100;
b = 200;

--[ check the boolean condition --]

if( a == 100 )
then
   --[ if condition is true then check the following --]
   if( b == 200 )
   then
      --[ if condition is true then print the following --]
      print("Value of a is 100 and b is 200" );
   end
end

print("Exact value of a is :", a );
print("Exact value of b is :", b );
```

```bash
lua /share/lesson/lua/loop-if-nested.lua
```

康康