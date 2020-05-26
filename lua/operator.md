# Lua 运算符(operator)

运算符是告诉解释器执行特定数学或逻辑操作的符号。 Lua语言内置运算符丰富，并提供以下类型的运算符 -

- 算术运算符
- 关系运算符
- 逻辑运算符
- 其它运算符

本教程将逐一解释算术，关系，逻辑和其他杂项运算符。

## 1. 算术运算符

下表显示了Lua语言支持的所有算术运算符。 假设变量`A=10`，变量`B=20`，然后 - 

| 运算符 | 描述                         | 示例          |
| ------ | ---------------------------- | ------------- |
| `+`    | 相加两个操作数               | `A + B = 30`  |
| `-`    | 从第一个减去第二个操作数     | `A - B = -10` |
| `*`    | 将两个操作数相乘             | `A * B = 200` |
| `/`    | 用除分子除以分子             | `B / A = 2`   |
| `%`    | 模数运算符，整数除法后的余数 | `B % A = 0`   |
| `^`    | 指数运算符取指数幂值         | `A^2 = 100`   |
| `-`    | 一元，充当否定               | `-A = -10`    |
**示例：**

文件名:operator-arithmetic.lua

```lua
a = 21
b = 10
c = a + b

print("Line 1 - Value of c is ", c )
c = a - b

print("Line 2 - Value of c is ", c )
c = a * b

print("Line 3 - Value of c is ", c )
c = a / b

print("Line 4 - Value of c is ", c )
c = a % b

print("Line 5 - Value of c is ", c )
c = a^2

print("Line 6 - Value of c is ", c )
c = -a

print("Line 7 - Value of c is ", c )
```

```bash
lua /share/lesson/lua/operator-arithmetic.lua
```

康康

## 2. 关系运算符

下表显示了Lua语言支持的所有关系运算符。 假设变量`A=10`，变量`B=20`，然后 - 

| 运算符 | 描述                                                         | 示例                    |
| ------ | ------------------------------------------------------------ | ----------------------- |
| `==`   | 检查两个操作数的值是否相等，如果相等，则条件变为真。         | `(A == B)`结果为`false` |
| `~=`   | 检查两个操作数的值是否相等，如果值不相等则条件变为`true`。   | `(A ~= B)`结果为`true`  |
| `>`    | 检查左操作数的值是否大于右操作数的值，如果是，则条件变为`true`。 | `(A > B)`结果为`false`  |
| `<`    | 检查左操作数的值是否小于右操作数的值，如果是，则条件变为`true`。 | `(A < B)`结果为`true`   |
| `>=`   | 检查左操作数的值是否大于或等于右操作数的值，如果是，则条件变为`true`。 | `(A >= B)`结果为`false` |
| `<=`   | 检查左操作数的值是否小于或等于右操作数的值，如果是，则条件变为`true`。 | `(A <= B)`结果为`true`  |
**示例：**

文件名:operator-relation.lua

```lua
a = 21
b = 10

if( a == b )
then
   print("Line 1 - a is equal to b" )
else
   print("Line 1 - a is not equal to b" )
end

if( a ~= b )
then
   print("Line 2 - a is not equal to b" )
else
   print("Line 2 - a is equal to b" )
end

if ( a < b )
then
   print("Line 3 - a is less than b" )
else
   print("Line 3 - a is not less than b" )
end

if ( a > b ) 
then
   print("Line 4 - a is greater than b" )
else
   print("Line 5 - a is not greater than b" )
end

-- Lets change value of a and b
a = 5
b = 20

if ( a <= b ) 
then
   print("Line 5 - a is either less than or equal to  b" )
end

if ( b >= a ) 
then
   print("Line 6 - b is either greater than  or equal to b" )
end
```

```bash
lua /share/lesson/lua/operator-relation.lua
```

康康

## 3. 逻辑运算符

下表显示了Lua语言支持的所有逻辑运算符。 假设变量`A=true`，变量`B=false`，则 - 

| 运算符 | 描述                                                         | 示例                      |
| ------ | ------------------------------------------------------------ | ------------------------- |
| `and`  | 逻辑与运算符。如果两个操作数都不为零，则条件成立。           | `(A and B)` 结果为`false` |
| `or`   | 逻辑或运算符。 如果两个操作数中的任何一个不为零，则条件变为真。 | `(A or B)` 结果为`true`   |
| `not`  | 逻辑非运算符。用于反转其操作数的逻辑状态。 如果条件为真，则逻辑非运算符将为`false`。 | `!(A and B)`结果为`true`  |

**示例**

文件名:operator-logic.lua

```lua
a = 21
b = 10

if( a == b )
then
   print("Line 1 - a is equal to b" )
else
   print("Line 1 - a is not equal to b" )
end

if( a ~= b )
then
   print("Line 2 - a is not equal to b" )
else
   print("Line 2 - a is equal to b" )
end

if ( a < b )
then
   print("Line 3 - a is less than b" )
else
   print("Line 3 - a is not less than b" )
end

if ( a > b ) 
then
   print("Line 4 - a is greater than b" )
else
   print("Line 5 - a is not greater than b" )
end

-- Lets change value of a and b
a = 5
b = 20

if ( a <= b ) 
then
   print("Line 5 - a is either less than or equal to  b" )
end

if ( b >= a ) 
then
   print("Line 6 - b is either greater than  or equal to b" )
end
```

```bash
lua /share/lesson/lua/operator-logic.lua
```

康康

## 4. 杂项运算符

Lua语言支持的其他运算符包括连接和长度。

| 编号  | 描述                             | 示例                                                        |
| ----- | -------------------------------- | ----------------------------------------------------------- |
| `...` | 连接两个字符串                   | 如果`a`为`Hello`，`b`为`World`，`a..b`将返回`Hello World`。 |
| `#`   | 返回字符串或表长度的一元运算符。 | `#"Hello"` 将返回 `5`                                       |

**示例：**

文件名:operator-other.lua

```lua
a = "Hello "
b = "World"

print("Concatenation of string a with b is ", a..b )

print("Length of b is ",#b )

print("Length of b is ",#"Test" )
```

```bash
lua /share/lesson/lua/operator-logic.lua
```

康康

## 5. Lua运算符优先级

运算符优先级确定表达式中的术语分组。 这会影响表达式的计算方式。 某些运算符的优先级高于其他运算符; 例如，乘法运算符的优先级高于加法运算符 - 

例如，`x = 7 + 3 * 2`; 这里`x`赋值为`13`，而不是`20`，因为运算符 `*` 的优先级高于`+`，所以它首先乘以`3 * 2`然后再加上`7`。

此处，具有最高优先级的运算符显示在表的顶部，具有最低优先级的运算符显示在底部。 在表达式中，将首先评估更高优先级的运算符。

| 类别   | 操作符                      | 关联性 |
| ------ | --------------------------- | ------ |
| 一元   | `not` `#` `-`               | 右到左 |
| 连接   | `..`                        | 右到左 |
| 乘法   | `*` `/` `%`                 | 左到右 |
| 加法   | `+` `-`                     | 左到右 |
| 关系   | `<` `>` `<=` `>=` `==` `~=` | 左到右 |
| 相等   | `==` `~=`                   | 左到右 |
| 逻辑与 | `and`                       | 左到右 |
| 逻辑或 | `or`                        | 左到右 |

**示例：**

文件名:operator-prior.lua

```lua
a = 20
b = 10
c = 15
d = 5

e = (a + b) * c / d;-- ( 30 * 15 ) / 5
print("(a + b) * c / d 运算值为  :",e )

e = ((a + b) * c) / d; -- (30 * 15 ) / 5
print("((a + b) * c) / d 运算值为 :",e )

e = (a + b) * (c / d);-- (30) * (15/5)
print("(a + b) * (c / d) 运算值为 :",e )

e = a + (b * c) / d;  -- 20 + (150/5)
print("a + (b * c) / d 运算值为   :",e )
```

```bash
lua /share/lesson/lua/operator-prior.lua
```

康康