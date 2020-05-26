# Lua 迭代器(iterator)	

迭代器是一个构造，可以用来遍历集合或容器的元素。 在Lua中，这些集合通常引用表，这些表用于创建各种数据结构，如数组。

## 迭代器泛型

迭代器泛型提供集合中每个元素的键值对。 下面给出一个简单的例子。

文件名:iterator-sample.lua

```lua
array = {"Lua", "Tutorial"}

for key,value in ipairs(array) 
do
   print(key, value)
end
```

```bash
lua /share/lesson/lua/iterator-sample.lua
```

康康

上面的例子使用了Lua提供的默认`ipairs`迭代器函数。

在Lua中，使用函数来表示迭代器。 基于这些迭代器函数中的状态维护，有两种主要类型 - 

- 无状态迭代器
- 有状态迭代器

#### 1. 无状态迭代器

通过名称，可以理解这种类型的迭代器函数不会保留任何状态。下面来看一个使用打印`n`个数字的函数`square`创建迭代器的示例。

```lua
function square(iteratorMaxCount,currentNumber)

   if currentNumber<iteratorMaxCount
   then
      currentNumber = currentNumber+1
      return currentNumber, currentNumber*currentNumber
   end

end

for i,n in square,3,0
do
   print(i,n)
end
```

稍微修改上面的代码，以模仿迭代器的`ipairs`函数的工作方式。 如下代码所示

文件名:iterator1.lua

```lua
function square(iteratorMaxCount,currentNumber)

   if currentNumber<iteratorMaxCount
   then
      currentNumber = currentNumber+1
      return currentNumber, currentNumber*currentNumber
   end

end

function squares(iteratorMaxCount)
   return square,iteratorMaxCount,0
end  

for i,n in squares(3)
do 
   print(i,n)
end
```

```bash
lua /share/lesson/lua/iterator1.lua
```

康康

#### 2. 有状态迭代器

上面使用函数的迭代示例不保留状态。 每次调用该函数时，它都会根据发送给函数的第二个变量返回集合的下一个元素。 要保持当前元素的状态，可使用闭包(`Closure`)。 闭包在函数调用中保留变量值。 要创建一个新的闭包，这里首先创建两个函数，包括闭包本身和一个工厂，即创建闭包的函数。

现在来看看一个创建迭代器的例子，并将使用闭包。

文件名:iterator2.lua

```lua
array = {"Lua", "Tutorial"}

function elementIterator (collection)

   local index = 0
   local count = #collection

   -- The closure function is returned

   return function ()
      index = index + 1

      if index <= count
      then
         -- return the current element of the iterator
         return collection[index]
      end

   end

end

for element in elementIterator(array)
do
   print(element)
end
```

```bash
lua /share/lesson/lua/iterator2.lua
```

康康

在上面的例子中，可以看到`elementIterator`中有另一个方法，它使用局部外部变量`index`和`count`来通过每次调用函数时递增索引来返回集合中的每个元素。
可使用闭包创建函数迭代器，如上所示，它可以为迭代整个集合的每个时间返回多个元素