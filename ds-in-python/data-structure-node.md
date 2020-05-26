# Python实现数据结构 节点(node)

在有些情况下，存储数据的内存分配不能位于连续的内存块中。 所以接受指针的帮助，其中数据和数据元素的下一个位置的地址也被存储。 所以从当前数据元素的值中知道下一个数据元素的地址。通常这样的结构被称为指针。 但在Python中，将它们称为节点。

节点是各种其他数据结构链表和树在python中处理的基础。

```python
class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Tue')
e3 = daynames('Wed')

e1.nextval = e3
e3.nextval = e2
```

## 遍历节点元素

可以通过创建一个变量并为其分配第一个元素来遍历上面创建的节点的元素。 然后使用`while`循环和`nextval`指针来打印出所有的节点元素。 请注意，我们还有一个额外的数据元素，并将`nextval`指针正确排列，以便按照正确的顺序将输出作为一周中的某天。

```python
class daynames:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

e1 = daynames('Mon')
e2 = daynames('Wed')
e3 = daynames('Tue')
e4 = daynames('Thu')

e1.nextval = e3
e3.nextval = e2
e2.nextval = e4

thisvalue = e1

while thisvalue:
        print(thisvalue.dataval)
        thisvalue = thisvalue.nextval
```

插入和删除等附加操作可以通过在链表和树等通用数据结构中，使用此节点容器来实现适当的方法来完成。 我们将在接下来的章节中进行研究和学习。