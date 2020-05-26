# Lua for循环

`for`循环是一种重复控制结构，用于有效地编写需要执行特定次数的循环。

## 语法

Lua编程语言中`for`循环的语法如下 - 

```lua
for init,max/min value, increment
do
   statement(s)
end
```

这是`for`循环中的控制流 - 

- `init` 首先执行，只执行一次。 此步骤允许声明和初始化任何循环控制变量。
- 接下来执行`max/min`。 这是循环继续执行的最大值或最小值。 它在内部创建条件检查，以比较初始值和最大/最小值。
- 在执行`for`循环体之后，控制流会跳回到`increment/decrement`语句。此语句用于更新循环控制变量。
- 再次评估条件。 如果为真，则循环执行并且过程自身重复(循环体，然后递增步骤，然后再次调节)。 条件变为`false`后，`for`循环终止。

**流程图**

```flow
st=>start: 程序流
cond=>condition: 判断框(是或否?)
condcode=>operation: 条件代码
e=>end: 程序流
st->cond
cond(no)->e
cond(yes)->condcode
condcode->e
```



**示例代码**

文件名:loop-for1.lua

```lua
for i = 100,1,-1 
do 
   print(i) 
end
```

```bash
lua /share/lesson/lua/loop-for1.lua
```

康康



泛型 for 循环通过一个迭代器函数来遍历所有值，类似 java 中的 foreach 语句。

文件名:loop-for2.lua

```lua
-- 打印数组
-- i是数组索引值，v是对应索引的数组元素值。ipairs是Lua提供的一个迭代器函数，用来迭代数组。
a = {"one", "two", "three"}
for i, v in ipairs(a) do
    print(i, v)
end 


days = {"Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"}  
for i,v in ipairs(days) do
    print(v) 
end  
```

```bash
lua /share/lesson/lua/loop-for2.lua
```

康康