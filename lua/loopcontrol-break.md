# Lua break语句

当在循环内遇到`break`语句时，循环立即终止，程序控制在循环后的下一个语句处重新开始。

如果使用嵌套循环(即，一个循环中使用另一个循环)，则`break`语句将停止执行最内层循环并开始执行该块之后的下一行代码。

#### 语法

Lua中`break`语句的语法如下

```lua
break
```

**流程图**

![img](https://www.yiibai.com/uploads/article/2018/12/06/145631_94387.jpg)

**示例代码**

文件名:loopcontrol-break.lua

```lua
--[ local variable definition --]
a = 10

--[ while loop execution --]
while( a < 20 )
do
   print("value of a:", a)
   a=a+1

   if( a > 15)
   then
      --[ terminate the loop using break statement --]
      break
   end

end
```

```bash
lua /share/lesson/lua/loopcontrol-break.lua
```

康康