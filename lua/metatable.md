# Lua 元表(metatable)

元表(`metatable`)是一个表，它是使用键集和相关元方法来修改附加到的表的行为。 这些元方法是强大的Lua功能，可实现如下功能 - 

- 在表上更改/添加功能到操作符。
- 使用元表中的`__index`在表中没有键时查找元表。

在处理元表时有两种重要的方法，包括 - 

- `setmetatable(table，metatable)` - 此方法用于为表设置元表。
- `getmetatable(table)` - 此方法用于获取表的元表。

首先来看看如何将一个表设置为另一个表的元表。 如下所示 -

```lua
mytable = {}
mymetatable = {}
setmetatable(mytable,mymetatable)
```

上面的代码可以用一行表示，如下所示 -

```shell
mytable = setmetatable({},{})
```

#### _index

下表显示了元表在表中不可用时查找元表的示例。

文件名:metatable_index.lua

```lua
mytable = setmetatable({key1 = "value1"}, {
   __index = function(mytable, key)

      if key == "key2" then
         return "metatablevalue"
      else
         return mytable[key]
      end
   end
})

print(mytable.key1,mytable.key2)
```

```bash
lua /share/lesson/lua/metatable_index.lua
```

康康

下面来逐步看看上面例子中发生的事情。

- 这里表`mytable`是`{key1 = "value1"}`。
- 元表设置为`mytable`，其中包含`__index`的函数，它称为元方法。
- 元方法执行查找索引`key2`，如果找到它，则返回`metatablevalue`，否则返回相应索引的`mytable`值。

#### __newindex

当将`__newindex`添加到`metatable`时，如果表中没有键，则新键的行为将由元方法定义。 下面给出了当主表中没有索引时设置`metatable`索引的简单示例。

文件名:metatable__newindex.lua

```lua
mymetatable = {}
mytable = setmetatable({key1 = "value1"}, { __newindex = mymetatable })

print(mytable.key1)

mytable.newkey = "new value 2"
print(mytable.newkey,mymetatable.newkey)

mytable.key1 = "new  value 1"
print(mytable.key1,mymetatable.newkey1)
```
如果主表中存在一个键，它只会更新它。 当维护中的键不可用时，它会将该键添加到`metatable`中。
```bash
lua /share/lesson/lua/metatable_index.lua
```

康康

使用`rawset`函数更新同一个表的另一个示例如下所示

文件名:metatable_rawset.lua

```lua
mytable = setmetatable({key1 = "value1"}, {

   __newindex = function(mytable, key, value)
      rawset(mytable, key, "\""..value.."\"")
   end
})

mytable.key1 = "new value"
mytable.key2 = 4

print(mytable.key1,mytable.key2)
```
`rawset`设置值而不使用元表的`__newindex`。 类似地，有一个`rawget`可以在不使用`__index`的情况下获取值。


```bash
lua /share/lesson/lua/metatable_rawset.lua
```

康康

#### 向表中添加运算符行为

使用`+`运算符组合两个表的简单示例如下所示 - 

文件名:metatable_add.lua

```lua
mytable = setmetatable({ 1, 2, 3 }, {
   __add = function(mytable, newtable)

      for i = 1, table.maxn(newtable) do
         table.insert(mytable, table.maxn(mytable)+1,newtable[i])
      end
      return mytable
   end
})

secondtable = {4,5,6}
mytable = mytable + secondtable

for k,v in ipairs(mytable) do
   print(k,v)
end
```

`__add`键包含在元表中以添加运算符 `+` 的行为。

```bash
lua /share/lesson/lua/metatable_add.lua
```

康康

键表和相应的操作符如下所示。

| 编号 | 模式       | 描述                   |
| ---- | ---------- | ---------------------- |
| 1    | `__add`    | 改变运算符`+`的行为。  |
| 2    | `__sub`    | 改变运算符`-`的行为。  |
| 3    | `__mul`    | 改变运算符`*`的行为。  |
| 4    | `__div`    | 改变运算符`/`的行为。  |
| 5    | `__mod`    | 改变运算符`%`的行为。  |
| 6    | `__unm`    | 改变运算符`-`的行为。  |
| 7    | `__concat` | 改变运算符`..`的行为。 |
| 8    | `__eq`     | 改变运算符`==`的行为。 |
| 9    | `__lt`     | 改变运算符`<`的行为。  |
| 10   | `__le`     | 改变运算符`<=`的行为。 |

#### __call

使用`__call`语句添加方法调用的行为。 一个简单的示例，它返回主表中的值与传递的表的总和。

文件名:metatable_call.lua

```lua
mytable = setmetatable({10}, {
   __call = function(mytable, newtable)
   sum = 0

      for i = 1, table.maxn(mytable) do
         sum = sum + mytable[i]
      end

      for i = 1, table.maxn(newtable) do
         sum = sum + newtable[i]
      end

      return sum
   end
})

newtable = {10,20,30}
print(mytable(newtable))
```

```bash
lua /share/lesson/lua/metatable_call.lua
```

康康

#### __tostring

要更改`print`语句的行为，可以使用`__tostring`元方法。 一个简单的例子如下所示。

文件名:metatable_tostring.lua

```lua
mytable = setmetatable({ 10, 20, 30 }, {
   __tostring = function(mytable)
   sum = 0

      for k, v in pairs(mytable) do
         sum = sum + v
      end

      return "The sum of values in the table is " .. sum
   end
})
print(mytable)
```

如果完全了解元表的功能，那么可以真正执行很多非常复杂的操作。 因此，尝试使用元表中可用的不同选项的元表更多地工作。

```bash
lua /share/lesson/lua/metatable_tostring.lua
```

康康