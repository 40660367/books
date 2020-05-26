# Lua 表(table)

表是Lua中唯一可用的数据结构，使用表可以创建不同的类型，如数组和字典。 Lua使用关联数组，不仅可使用数字编制索引，还可以使用除`nil`之外的字符串编制索引。 表没有固定的大小，可以根据需要增长大小。

Lua在所有表示中使用表，包括包的表示。 当访问方法`string.format`时，这意味着，访问字符串包中可用的格式函数。

## 表示和用法

表称为对象，它既不是值也不是变量。 Lua使用构造函数表达式`{}`来创建一个空表。 应该知道，保持表的引用的变量和表本身之间没有固定的关系。

```lua
--sample table initialization
mytable = {}

--simple table value assignment
mytable[1]= "Lua"

--removing reference
mytable = nil

-- lua garbage collection will take care of releasing memory
```

假设有一个包含元素集的表`a`，如果将它分配给表`b`，则`a`和`b`都指向相同的内存。 Lua不会单独为`b`分配单独的内存。 当`a`设置为`nil`时，`b`仍然可以访问表。 当没有对表的引用时，Lua中的垃圾收集器负责清理进程以使这些未引用的内存再次被重用。

下面示出了一个例子，用于解释表的上述特征。

文件名:table-sample.lua

```lua
-- Simple empty table
mytable = {}
print("Type of mytable is ",type(mytable))

mytable[1]= "Lua"
mytable["wow"] = "Tutorial"

print("mytable Element at index 1 is ", mytable[1])
print("mytable Element at index wow is ", mytable["wow"])

-- alternatetable and mytable refers to same table
alternatetable = mytable

print("alternatetable Element at index 1 is ", alternatetable[1])
print("mytable Element at index wow is ", alternatetable["wow"])

alternatetable["wow"] = "I changed it"

print("mytable Element at index wow is ", mytable["wow"])

-- only variable released and and not table
alternatetable = nil
print("alternatetable is ", alternatetable)

-- mytable is still accessible
print("mytable Element at index wow is ", mytable["wow"])

mytable = nil
print("mytable is ", mytable)
```

```bash
lua /share/lesson/lua/table-sample.lua
```

康康

## 表操作

下面是用于表操作的内置函数，它们列在下表格中。

| 编号 | 方法                                       | 作用                                                 |
| ---- | ------------------------------------------ | ---------------------------------------------------- |
| 1    | `table.concat (table [, sep [, i [, j]]])` | 根据给定的参数连接表中的字符串。详细信息请参见示例。 |
| 2    | `table.insert (table, [pos,] value)`       | 在指定位置的表中插入值。                             |
| 3    | `table.maxn (table)`                       | 返回最大的数字索引。                                 |
| 4    | `table.remove (table [, pos])`             | 从表中删除值。                                       |
| 5    | `table.sort (table [, comp])`              | 根据可选的比较器参数对表进行排序。                   |

下面来看看一些上述功能的示例。

#### 1. 表连接

使用`concat`函数来连接两个表

文件名:table1.lua

```lua
fruits = {"banana","orange","apple"}

-- returns concatenated string of table
print("Concatenated string ",table.concat(fruits))

--concatenate with a character
print("Concatenated string ",table.concat(fruits,", "))

--concatenate fruits based on index
print("Concatenated string ",table.concat(fruits,", ", 2,3))
```

```bash
lua /share/lesson/lua/table1.lua
```

康康

#### 2. 插入和删除

在表操作中，最常见的是在表中插入和删除项目。如下解释。

文件名:table2.lua

```lua
fruits = {"banana","orange","apple"}

-- insert a fruit at the end
table.insert(fruits,"mango")
print("Fruit at index 4 is ",fruits[4])

--insert fruit at index 2
table.insert(fruits,2,"grapes")
print("Fruit at index 2 is ",fruits[2])

print("The maximum elements in table is",table.maxn(fruits))

print("The last element is",fruits[5])

table.remove(fruits)
print("The previous last element is",fruits[5])
```

```bash
lua /share/lesson/lua/table2.lua
```

康康

#### 3. 排序表

有时想要按特定顺序对表进行排序。 排序函数按字母顺序对表中的元素进行排序。 这方面的示例如下所示。

文件名:table3.lua

```lua
fruits = {"banana","orange","apple","grapes"}

for k,v in ipairs(fruits) do
   print(k,v)
end

table.sort(fruits)
print("sorted table")

for k,v in ipairs(fruits) do
   print(k,v)
end
```

```bash
lua /share/lesson/lua/table3.lua
```

康康