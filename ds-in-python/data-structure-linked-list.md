# Python实现数据结构 链表(linked list)

链表是一系列数据元素，通过链接连接在一起。 每个数据元素都以指针的形式包含到另一个数据元素的连接。 Python在其标准库中没有链接列表。 我们使用前一章讨论的节点概念来实现链表的概念。 我们已经知道如何创建节点类以及如何遍历节点的元素。 在本章中，将学习链表的类型:单链表。 在这种类型的数据结构中，任何两个数据元素之间只有一个链接。 创建一个链表并使用一些方法来插入，更新和从列表中移除元素。

## 创建链表

通过使用在上一章中学习的节点类来创建链表。创建一个`Node`对象并创建另一个类来使用这个节点对象。 通过节点对象传递适当的值来指向下一个数据元素。 下面的程序使用三个数据元素创建链接列表。 在下一节中，将学习如何遍历链表。

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

list1 = SLinkedList()
list1.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
# Link first Node to second node
list1.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3
```

## 遍历链表

从第一个数据元素开始，单向链表只能在向前遍历。 只需通过将下一个节点的指针指向当前数据元素来打印下一个数据元素的值。

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

# Link first Node to second node
list.headval.nextval = e2

# Link second Node to third node
e2.nextval = e3

list.listprint()
```

## 向链表插入数据

在链表中插入元素涉及将指针从现有节点重新分配给新插入的节点。 取决于新数据元素是在链表的开始位置还是在中间位置或末尾插入，有以下解决方案。

**在链接列表的开头插入**

这涉及到将新数据节点的下一个指针指向链表的当前头部。 因此，链表的当前头成为第二个数据元素，新节点成为链表的头部。

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval
    def AtBegining(self,newdata):
        NewNode = Node(newdata)

# Update the new nodes next val to existing node
        NewNode.nextval = self.headval
        self.headval = NewNode

list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtBegining("Sun")

list.listprint()
```

**在链表的末尾插入**

这包括将链表的当前最后一个节点的下一个指针指向新的数据节点。 因此链表的当前最后一个节点成为倒数第二个数据节点，新节点成为链表的最后一个节点。参考以下代码实现 - 

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add newnode
    def AtEnd(self, newdata):
        NewNode = Node(newdata)
        if self.headval is None:
            self.headval = NewNode
            return
        laste = self.headval
        while(laste.nextval):
            laste = laste.nextval
        laste.nextval=NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Wed")

list.headval.nextval = e2
e2.nextval = e3

list.AtEnd("Thu")

list.listprint()
```

**在两个数据节点之间插入**

这涉及到将指定节点的指针指向新节点。 这可以通过传入新节点和现有节点，然后插入新节点。 所以定义一个额外的类，将新节点的下一个指针改变为中间节点的下一个指针。 然后将新节点分配给中间节点的下一个指针。参考以下代码实现 - 

```python
class Node:
    def __init__(self, dataval=None):
        self.dataval = dataval
        self.nextval = None

class SLinkedList:
    def __init__(self):
        self.headval = None

# Function to add node
    def Inbetween(self,middle_node,newdata):
        if middle_node is None:
            print("The mentioned node is absent")
            return

        NewNode = Node(newdata)
        NewNode.nextval = middle_node.nextval
        middle_node.nextval = NewNode

# Print the linked list
    def listprint(self):
        printval = self.headval
        while printval is not None:
            print (printval.dataval)
            printval = printval.nextval


list = SLinkedList()
list.headval = Node("Mon")
e2 = Node("Tue")
e3 = Node("Thu")

list.headval.nextval = e2
e2.nextval = e3

list.Inbetween(list.headval.nextval,"Fri")

list.listprint()
```

## 从链表中删除项目

可以使用该节点的键来删除一个节点。 在下面的程序中，找到要删除的节点的前一个节点。 然后将该节点的下一个指针指向要删除的节点的下一个节点。

```python
class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class SLinkedList:
    def __init__(self):
        self.head = None

    def Atbegining(self, data_in):
        NewNode = Node(data_in)
        NewNode.next = self.head
        self.head = NewNode

# Function to remove node
    def RemoveNode(self, Removekey):

        HeadVal = self.head

        if (HeadVal is not None):
            if (HeadVal.data == Removekey):
                self.head = HeadVal.next
                HeadVal = None
                return

        while (HeadVal is not None):
            if HeadVal.data == Removekey:
                break
            prev = HeadVal
            HeadVal = HeadVal.next

        if (HeadVal == None):
            return

        prev.next = HeadVal.next

        HeadVal = None

    def LListprint(self):
        printval = self.head
        while (printval):
            print(printval.data),
            printval = printval.next


llist = SLinkedList()
llist.Atbegining("Mon")
llist.Atbegining("Tue")
llist.Atbegining("Wed")
llist.Atbegining("Thu")
llist.RemoveNode("Tue")
llist.LListprint()
```

