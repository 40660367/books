# Lua 文件操作

I/O库用于读取和操作Lua中的文件。 Lua中有两种文件操作，即隐式文件描述符和显式文件描述符。

文件打开操作的语法为：

```lua
file = io.open (filename [, mode])
```

下表列出了各种文件模式 - 

| 编号 | 模式 | 描述                                                         |
| ---- | ---- | ------------------------------------------------------------ |
| 1    | `r`  | 只读模式，是打开现有文件的默认模式。                         |
| 2    | `w`  | 写入启用模式，覆盖现有文件或创建新文件。                     |
| 3    | `a`  | 附加模式，用于打开现有文件或创建新文件以进行追加。           |
| 4    | `r+` | 现有文件的读写模式。                                         |
| 5    | `w+` | 如果文件存在或创建具有读写权限的新文件，则删除所有现有数据。 |
| 6    | `a+` | 启用了读取模式的追加模式可打开现有文件或创建新文件。         |


为以下示例，准备示例文件test.lua

文件名: test.lua
```
cd ~
cat > test.lua << EOF
-- sample test.lua
-- sample2 test.lua
EOF
```

## 1. 隐式文件描述符

隐式文件描述符使用标准输入/输出模式或使用单个输入和单个输出文件。 使用隐式文件描述符的示例如下所示。

文件名:io-read.lua

```lua
-- Opens a file in read
file = io.open("test.lua", "r")

-- sets the default input file as test.lua
io.input(file)

-- prints the first line of the file
print(io.read())

-- closes the open file
io.close(file)
```
```bash
lua /share/lesson/lua/io-read.lua
```
运行程序时，将获得testfile.txt文件第一行的输出。`-- Sample test.lua`

文件名:io-write.lua

```lua
-- Opens a file in append mode
file = io.open("test.lua", "a")

-- sets the default output file as test.lua
io.output(file)

-- appends a word test to the last line of the file
io.write("-- End of the test.lua file")

-- closes the open file
io.close(file)
```
```bash
lua /share/lesson/lua/io-read.lua
cat test.txt
```
运行程序时将`"-- End of the test.lua file"`这一行附加到test.lua` 文件中的最后一行。



在上面的示例中，可以使用`io."x"`方法查看隐式描述符如何与文件系统一起使用。 上面的示例使用不带可选参数的`io.read()`方法。可选参数可以是以面中的任何一个。

| 编号 | 模式     | 描述                                                         |
| ---- | -------- | ------------------------------------------------------------ |
| 1    | `*n`     | 从当前文件位置读取并返回一个数字(如果存在于文件位置或返回`nil`)。 |
| 2    | `*a`     | 从当前文件位置返回文件的所有内容。                           |
| 3    | `*l`     | 从当前文件位置读取行，并将文件位置移动到下一行。             |
| 4    | `number` | 读取函数中指定的字节数。                                     |

其他常见的**I/O**方法包括，

- `io.tmpfile()` - 返回一个临时文件，用于读取和写入，当程序退出，将删除该文件。
- `io.type(file)` - 根据输入文件返回文件，关闭文件或`nil`。
- `io.flush()` - 清除默认输出缓冲区。
- `io.lines(可选文件名)` - 提供循环迭代器的通用循环迭代器，循环遍历文件并最终关闭文件，以防提供文件名或使用默认文件而不在循环结束时关闭。

## 2. 显式文件描述符

显式文件描述符经常使用，它允许一次操作多个文件。 这些函数与隐式文件描述符非常相似。 在这里，使用`file：function_name`，而不是`io.function_name`。 

下面显示了以下相同隐式文件描述符示例的显式文件描述符版本示例。

文件名:io.lua

```lua
-- Opens a file in read mode
file = io.open("test.lua", "r")

-- prints the first line of the file
print(file:read())

-- closes the opened file
file:close()

-- Opens a file in append mode
file = io.open("test.lua", "a")

-- appends a word test to the last line of the file
file:write("--test")

-- closes the open file
file:close()
```

```bash
lua /share/lesson/lua/io.lua
```

文件打开的所有模式和用于读取外部描述符的参数与隐式文件描述符相同。

其他常见的文件方法包括，

- `file:seek(optional whence, optional offset)` - 参数是`set`，`cur`或`end`。 使用文件开头的更新文件位置设置新文件指针。 在此函数中，偏移量为零。 如果第一个参数是`set`，则从文件的开头测量偏移量; 从文件中的当前位置开始，如果它是`cur`; 或者从文件的末尾开始，则它是`end`。 默认参数值为`cur`和`0`，因此可以通过不带参数调用此函数来获取当前文件位置。
- `file:flush()` − 清除默认输出缓冲区。
- `io.lines(optional file name)` - 提供循环迭代器的通用循环迭代器，循环遍历文件并最终关闭文件，以防提供文件名或使用默认文件而不在循环结束时关闭。

使用搜索方法的示例如下所示。它将光标从文件结束前的`25`个位置偏移。 `read`函数从搜索位置打印文件的剩余部分。

文件名:io-seek.lua

```lua
-- Opens a file in read
file = io.open("test.lua", "r")

file:seek("end",-25)
print(file:read("*a"))

-- closes the opened file
file:close()
```

```bash
lua /share/lesson/lua/io-seek.lua
```

您可自己使用所有的模式和参数来了解Lua文件操作的完整功能。