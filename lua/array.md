# Lua 数组(array)

数组是对象的有序排列，可以是包含行集合的一维数组或包含多个行和列的多维数组。

在Lua中，使用带整数的索引表实现数组。 数组的大小不固定，它可以根据要求增长，受内存限制。

## 一维数组

一维数组可以使用简单的表结构表示，并且可以使用`for`循环进行初始化和读取。 如下例子所示。

文件名:array1.lua

```lua
array = {"Lua", "Tutorial"}

for i = 0, 2 do
   print(array[i])
end
```

```bash
lua /share/lesson/lua/array1.lua
```

康康

正如在上面的代码中所看到的，当尝试访问数组中不存在的索引中的元素时，它返回`nil`值。 在Lua中，索引通常从索引`1`开始。但是也可以在索引`0`和`0`以下(负数)创建对象。 使用负索引的数组如下所示，使用`for`循环初始化数组。

文件名:array2.lua

```lua
array = {}

for i= -2, 2 do
   array[i] = i *2
end

for i = -2,2 do
   print(array[i])
end
```

```bash
lua /share/lesson/lua/array2.lua
```

康康

## 多维数组

多维数组有两种方式实现。它们分别如下 - 

- 数组的数组
- 通过操纵一维数组的索引

下面是使用数组阵列 `3 x 3`的多维数组的示例。

文件名:array-md1.lua

```lua
-- 初始化数组
array = {}

for i=1,3 do
   array[i] = {}

   for j=1,3 do
      array[i][j] = i*j
   end

end

-- 访问数组

for i=1,3 do

   for j=1,3 do
      print(array[i][j])
   end

end
```

```bash
lua /share/lesson/lua/array-md1.lua
```

康康



下面使用操作索引显示多维数组的示例。

文件名:array-md2.lua

```lua
-- 初始化数组

array = {}

maxRows = 3
maxColumns = 3

for row=1,maxRows do

   for col=1,maxColumns do
      array[row*maxColumns +col] = row*col
   end

end

-- 访问数组

for row=1,maxRows do

   for col=1,maxColumns do
      print(array[row*maxColumns +col])
   end

end
```

```bash
lua /share/lesson/lua/array-md2.lua
```

康康



如在上面的示例中所看到的，数据是基于索引存储的。 可以以稀疏的方式放置元素，这是Lua实现数组的方式。 在Lua中由于它没有存储`nil`值，因此与其他编程语言中使用的特殊技术相比，Lua中可以节省大量内存而无需任何特殊技术。