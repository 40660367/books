# Lua 嵌套循环

Lua编程语言允许在一个循环中嵌套使用另一个循环。 下面显示了几个例子来说明这个概念。

## 语法

Lua中嵌套`for`循环语句的语法：

```lua
for init,max/min value, increment
do
   for init,max/min value, increment
   do
      statement(s)
   end
   statement(s)
end
```

Lua编程语言中嵌套`while`循环语句的语法：

```lua
while(condition)
do
   while(condition)
   do
      statement(s)
   end
   statement(s)
end
```

Lua编程语言中嵌套`repeat...until`循环语句的语法：

```lua
repeat
   statement(s)
   repeat
      statement(s)
   until( condition )
until( condition )
```

可以将任何类型的循环放在任何其他类型的循环中。 例如，`for`循环可以在`while`循环内，反之亦然。

#### 示例

文件名:loop-nested1.lua

```lua
j = 2
for i = 2,10 do
   for j = 2,(i/j) , 2 do

      if(not(i%j)) 
      then
         break 
      end

      if(j > (i/j))then
         print("Value of i is",i)
      end

   end
end
```

```bash
lua /share/lesson/lua/loop-nested1.lua
```

康康