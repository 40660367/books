# Lua 字符串(string)

字符串是由一系列字符以及控制字符组成，如换页符。 字符串可以用三种形式初始化，包括

- 单引号之间的字符
- 双引号之间的字符
- `[[`和`]]`之间的字符

以下示出了上述三种形式的示例。

```lua
string1 = "Lua"
print(""String 1 is"",string1)

string2 = 'Lua Tutorial'
print("String 2 is",string2)

string3 = [["Lua Tutorial"]]
print("String 3 is",string3)
```

字符串中使用转义序列字符来更改字符的正常解释。例如，要打印双引号(`""`)，在上面的示例中使用了`"`。转义序列及其用法列在下表中。

| 转义序列 | 用法       |
| -------- | ---------- |
| `\a`     | 铃         |
| `\b`     | 退格       |
| `\f`     | 换页       |
| `\n`     | 新行       |
| `\r`     | 回车       |
| `\t`     | 制表符     |
| `\v`     | 垂直制表符 |
| `\\`     | 反斜杠     |
| `"`      | 双引号     |
| `'`      | 单引号     |
| `\[`     | 左方括号   |
| `\]`     | 右方括号   |

## 字符串操作

Lua支持字符串来操作字符串 - 

| 编号 | 方法                                                         | 作用                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | `string.upper(argument)`                                     | 返回参数的大写表示。                                         |
| 2    | `string.lower(argument)`                                     | 返回参数的小写表示。                                         |
| 3    | `string.gsub(mainString,findString,replaceString)`           | 返回用`replaceString`替换`findString`后字符串。              |
| 4    | `string.find(mainString,findString, optionalStartIndex,optionalEndIndex)` | 返回`mainString`中`findString`的起始索引和结束索引找到字符串，如果未找到则返回`nil`。 |
| 5    | `string.reverse(arg)`                                        | 将传递的字符串`arg`反转后的字符串。                          |
| 6    | `string.format(...)`                                         | 返回格式化字符串。                                           |
| 7    | `string.char(arg)` 和 `string.byte(arg)`                     | 返回输入参数的内部数字和字符表示。                           |
| 8    | `string.len(arg)`                                            | 返回传递字符串`arg`的长度。                                  |
| 9    | `string.rep(string, n))`                                     | 通过重复相同的字符串`n`次返回一个字符串。                    |
| 10   | `..`                                                         | 此运算符连接两个字符串。                                     |

现在，来深入了解一些示例，以准确了解这些字符串操作函数的行为方式。

#### 大小写操作

下面给出了用于将字符串转换为大写和小写的示例代码。

文件名:string1.lua

```lua
string = "Lua Tutorial"

-- replacing strings
newstring = string.gsub(string,"Tutorial","Language")
print("The new string is "..newstring)
```

```bash
lua /share/lesson/lua/string1.lua
```

康康

#### 寻找和反转

下面给出了用于查找子串索引和反转字符串的示例代码。

文件名:string2.lua

```lua
string = "Lua Tutorial"

-- replacing strings
print(string.find(string,"Tutorial"))
reversedString = string.reverse(string)
print("The new string is",reversedString)
```

```bash
lua /share/lesson/lua/string2.lua
```

康康

#### 格式化字符串

在Lua编程中，有时需要以格式化的方式打印字符串。 那么可使用`string.format`函数格式化输出，如下所示。

文件名:string3.lua

```lua
string1 = "Lua"
string2 = "Tutorial"

number1 = 10
number2 = 20

-- Basic string formatting
print(string.format("Basic formatting %s %s",string1,string2))

-- Date formatting
date = 2; month = 1; year = 2014
print(string.format("Date formatting %02d/%02d/%03d", date, month, year))

-- Decimal formatting
print(string.format("%.4f",1/3))
```

```bash
lua /share/lesson/lua/string3.lua
```

康康

#### 字符和字节表示

字符和字节表示的示例代码，用于将字符串从字符串转换为内部表示，反之亦然。

文件名:string4.lua

```lua
-- Byte conversion

-- First character
print(string.byte("Lua"))

-- Third character
print(string.byte("Lua",3))

-- first character from last
print(string.byte("Lua",-1))

-- Second character
print(string.byte("Lua",2))

-- Second character from last
print(string.byte("Lua",-2))

-- Internal Numeric ASCII Conversion
print(string.char(97))
```

```bash
lua /share/lesson/lua/string4.lua
```

康康

#### 其他常用函数

常见的字符串操作包括字符串连接，查找字符串的长度以及有时多次重复相同的字符串。 下面给出了这些操作的示例。

文件名:string5.lua

```lua
string1 = "Lua"
string2 = "Tutorial"

-- String Concatenations using ..
print("Concatenated string",string1..string2)

-- Length of string
print("Length of string1 is ",string.len(string1))

-- Repeating strings
repeatedString = string.rep(string1,3)
print(repeatedString)
```

```bash
lua /share/lesson/lua/string5.lua
```

康康