# Python实现数据结构  队列(queue)

当等待一项服务时，对日常生活中的排队很熟悉。 队列数据结构同样意味着数据元素排列在一个队列中。 队列的唯一性在于项目添加和删除的方式。 这些对象可以放在最后，但从另一端移除。 所以这是先进先出的方法。 可以使用python list实现队列，可以使用`insert()`和`pop()`方法添加和移除元素。它们没有插入，因为数据元素总是添加在队列的末尾。

## 将元素添加到队列

在下面的例子中，我们创建了一个队列类，实现了先进先出方法。 使用内置的`insert()`方法来添加数据元素。

```python
class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False

  def size(self):
      return len(self.queue)

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.size())
```

## 从队列中移除元素

在下面的例子中，我们创建了一个插入数据的队列类，然后使用内置的`pop`方法删除数据。参考以下代码实现 - 

```python
class Queue:

  def __init__(self):
      self.queue = list()

  def addtoq(self,dataval):
# Insert method to add element
      if dataval not in self.queue:
          self.queue.insert(0,dataval)
          return True
      return False
# Pop method to remove element
  def removefromq(self):
      if len(self.queue)>0:
          return self.queue.pop()
      return ("No elements in Queue!")

TheQueue = Queue()
TheQueue.addtoq("Mon")
TheQueue.addtoq("Tue")
TheQueue.addtoq("Wed")
print(TheQueue.removefromq())
print(TheQueue.removefromq())
```