# Python实现数据结构 双端队列(deque) 			

双端队列(或两端队列)具有从任一端添加和删除元素的功能。 `Deque`模块是集合库的一部分。 它具有添加和删除可以直接用参数调用的元素的方法。 在下面的程序中，将导入`collections`模块并声明一个双端队列。 不需要任何类，直接使用内置的实现这些方法。

参数以下代码实现 - 

```python
import collections
# Create a deque
DoubleEnded = collections.deque(["Mon","Tue","Wed"])
print (DoubleEnded)

# Append to the right
print("Adding to the right: ")
DoubleEnded.append("Thu")
print (DoubleEnded)

# append to the left
print("Adding to the left: ")
DoubleEnded.appendleft("Sun")
print (DoubleEnded)

# Remove from the right
print("Removing from the right: ")
DoubleEnded.pop()
print (DoubleEnded)

# Remove from the left
print("Removing from the left: ")
DoubleEnded.popleft()
print (DoubleEnded)

# Reverse the dequeue
print("Reversing the deque: ")
DoubleEnded.reverse()
print (DoubleEnded)
```