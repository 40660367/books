# Python实现数据结构 栈(stack)

在英语词典中，堆(`Stack`)表示将对象放在另一个对象上。 在这个数据结构中分配内存的方式是一样的。 它以类似的方式存储数据元素，类似在厨房中一堆盘子:一个在另一个之上存放。 所以堆栈数据数据允许操作的一端可以称为**栈顶**。 可在**栈顶**上添加元素或仅从堆栈中移除元素。

在堆栈中，顺序排列的最后一个元素将首先出现，因为只能从堆栈顶部移除。 这种功能称为后进先出(LIFO)功能。 添加和删除元素的操作称为`PUSH`和`POP`。 在下面的程序中，我们将它实现为`add`和`remove`函数。首先声明一个空列表并使用`append()`和`pop()`方法来添加和删除数据元素。

**推入堆栈**

```python
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False
# Use peek to look at the top of the stack

    def peek(self):     
        return self.stack[0]

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
AStack.peek()
print(AStack.peek())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.peek())
```

**堆栈移除**

只能从堆栈中移除数据元素，下面实现了一个可以实现这一功能的python程序。 以下程序中的`remove`函数返回最上面的元素。 首先通过计算堆栈的大小来检查顶层元素，然后使用内置的`pop()`方法找出最顶层的元素。参考以下代码实现 - 

```python
class Stack:

    def __init__(self):
        self.stack = []

    def add(self, dataval):
# Use list append method to add element
        if dataval not in self.stack:
            self.stack.append(dataval)
            return True
        else:
            return False

# Use list pop method to remove element
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

AStack = Stack()
AStack.add("Mon")
AStack.add("Tue")
print(AStack.remove())
AStack.add("Wed")
AStack.add("Thu")
print(AStack.remove())
```

