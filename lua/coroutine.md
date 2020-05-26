# Lua 协同程序(coroutine)

协同程序本质上是协作的，它允许两种或多种方法以受控方式执行。 使用协同程序，在任何给定时间，只有一个协同程序运行，并且此运行协程仅在显式请求暂停时暂停执行。

上述定义可能看起来含糊不清。 假设有两种方法，一种是主程序方法，另一种是协程。 当使用`resume`函数调用一个协程时，它会开始执行，当调用`yield`函数时，它会暂停执行。 同样的协同程序可以继续执行另一个恢复函数调用，协同程序就会暂停。 该过程可以持续到协程执行结束。

## 协同程序函数

下表列出了Lua中协程的所有可用函数及其相应的用法。

| 编号 | 方法                                  | 作用或目的                                                   |
| ---- | ------------------------------------- | ------------------------------------------------------------ |
| 1    | `coroutine.create (f)`                | 使用函数`f`创建一个新的协同程序，并返回`thread`类型的对象。  |
| 2    | `coroutine.resume (co [, val1, ...])` | 恢复协程`co`并传递参数(如果有的话)。它返回操作状态和可选的其他返回值。 |
| 3    | `coroutine.running ()`                | 如果在主线程中调用，则返回正在运行的协同程序或`nil`。        |
| 4    | `coroutine.status (co)`               | 根据协同程序的状态返回`running`，`normal`，`suspended`或`dead`中的一个值。 |
| 5    | `coroutine.wrap (f)`                  | 与`coroutine.create`一样，`coroutine.wrap`函数也会创建一个协同程序，但它不会返回协同程序本身，而是返回一个函数，当调用它时，它会恢复协同程序。 |
| 6    | `coroutine.yield (...)`               | 暂停正在运行的协同程序。 传递给此方法的参数充当`resume`函数的附加返回值。 |

**示例**
下面来看一个例子，通过此示例来理解协同程序的概念。

文件名:coroutine1.lua

```lua
co = coroutine.create(function (value1,value2)
   local tempvar3 = 10
   print("coroutine section 1", value1, value2, tempvar3)

   local tempvar1 = coroutine.yield(value1+1,value2+1)
   tempvar3 = tempvar3 + value1
   print("coroutine section 2",tempvar1 ,tempvar2, tempvar3)

   local tempvar1, tempvar2= coroutine.yield(value1+value2, value1-value2)
   tempvar3 = tempvar3 + value1
   print("coroutine section 3",tempvar1,tempvar2, tempvar3)
   return value2, "end"
end)

print("main", coroutine.resume(co, 3, 2))
print("main", coroutine.resume(co, 12,14))
print("main", coroutine.resume(co, 5, 6))
print("main", coroutine.resume(co, 10, 20))
```

```bash
lua /share/lesson/lua/coroutine1.lua
```

康康

**上面的例子是实现什么功能？**

如前所述，使用`resume`函数来启动操作和`yield`函数来停止操作。 此外，可以看到`coroutine`的恢复功能接收到多个返回值。

- 首先，创建一个协同程序并分配给变量名称`co`，协同程序将两个变量作为参数。
- 当调用第一个恢复函数时，值`3`和`2`保留在临时变量`value1`和`value2`中，直到协程结束。
- 使用了一个变量`tempvar3`，它最初值是`10`，并且通过后续的协程调用更新为`13`和`16`，在整个协程的执行过程中`value1`的值保持为`3`。
- 第一个`coroutine.yield`将两个值`4`和`3`返回到`resume`函数，通过更新`yield`语句中的输入参数为`3`和`2`。 它还接收协程执行的`true/false`状态。
- 关于协同程序的另一个问题是，在上面的例子中如何处理下一个`resume`调用的句子; 可以看到变量`coroutine.yield`接收下一个调用参数，它提供了一种强大的方法，可以通过保留现有的参数值来进行新的操作。
- 最后，当协程中的所有语句都执行后，后续调用将返回`false`并且响应语句为：*cannot resume dead coroutine*。

#### 另一个协同程序示例

下面来看一个简单的协同程序示例，它使用`yield`函数和`resume`函数返回`1`到`5`之间的数字。 如果不可用它会创建协程，或者恢复现有的协程。

文件名:coroutine2.lua

```lua
function getNumber()
   local function getNumberHelper()
      co = coroutine.create(function ()
      coroutine.yield(1)
      coroutine.yield(2)
      coroutine.yield(3)
      coroutine.yield(4)
      coroutine.yield(5)
      end)
      return co
   end

   if(numberHelper) then
      status, number = coroutine.resume(numberHelper);

      if coroutine.status(numberHelper) == "dead" then
         numberHelper = getNumberHelper()
         status, number = coroutine.resume(numberHelper);
      end

      return number
   else
      numberHelper = getNumberHelper()
      status, number = coroutine.resume(numberHelper);
      return number
   end

end

for index = 1, 10 do
   print(index, getNumber())
end
```

```bash
lua /share/lesson/lua/coroutine2.lua
```

康康

通常会将协同程序与多路程序设计语言的线程进行比较，但需要了解协同程序具有类似的线程功能，但协同程序一次只执行一个程序，并且永远不会同时执行。

通过暂时保留某些信息来控制程序执行顺序以满足需求。 使用带有协同程序的全局变量为协同程序提供了更大的灵活性。