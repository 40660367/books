# Python实现算法:树遍历

遍历是访问树的所有节点的过程，也可以打印它们的值。 因为所有节点都通过边(链接)连接，所以始终从根(头)节点开始。 也就是说，我们不能随机访问树中的一个节点。 这里介绍三种方式来遍历一棵树 -

- 顺序遍历
- 前序遍历
- 后序遍历

## 按顺序遍历

在这种遍历方法中，首先访问左侧子树，然后访问根，然后访问右侧子树。 我们应该永远记住每个节点本身可能代表一个子树。

在下面的python程序中，使用`Node`类为根节点以及左右节点创建占位符。 然后创建一个`insert()`函数来将数据添加到树中。 最后，`Inorder`遍历逻辑通过创建一个空列表，并首先添加添加根节点或父节点，然后左节点来实现。 最后添加左节点以完成`Inorder`遍历。 请注意，对于每个子树重复此过程，直到遍历所有节点。

```python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Inorder traversal
# Left -> Root -> Right
    def inorderTraversal(self, root):
        res = []
        if root:
            res = self.inorderTraversal(root.left)
            res.append(root.data)
            res = res + self.inorderTraversal(root.right)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.inorderTraversal(root))
```

## 前序遍历

在这种遍历方法中，首先访问根节点，然后访问左边的子树，最后访问右边的子树。

在下面的python程序中，使用`Node`类为根节点以及左右节点创建占位符。 然后创建一个`insert()`函数来将数据添加到树中。 最后，前序遍历遍历逻辑通过创建一个空列表并首先添加根节点，然后添加左节点来实现。 最后添加右节点以完成前序遍历。 请注意，对于每个子树重复此过程，直到遍历所有节点。

```python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Preorder traversal
# Root -> Left ->Right
    def PreorderTraversal(self, root):
        res = []
        if root:
            res.append(root.data)
            res = res + self.PreorderTraversal(root.left)
            res = res + self.PreorderTraversal(root.right)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PreorderTraversal(root))
```

## 后序遍历

在这个遍历方法中，最后访问根节点。 首先遍历左子树，然后遍历右子树，最后遍历根节点。

在下面的python程序中，使用`Node`类为根节点以及左右节点创建占位符。 然后创建一个`insert()`函数来将数据添加到树中。 最后，通过创建一个空列表并添加左节点，然后添加右节点来实现后序遍历逻辑。 最后，添加根或父节点以完成后序遍历。 请注意，对于每个子树重复此过程，直到遍历所有节点。参考以下代码实现 - 

```python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data
# Insert Node
    def insert(self, data):

        if self.data:
            if data < self.data:
                if self.left is None:
                    self.left = Node(data)
                else:
                    self.left.insert(data)
            elif data > self.data:
                if self.right is None:
                    self.right = Node(data)
                else:
                    self.right.insert(data)
        else:
            self.data = data

# Print the Tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()

# Postorder traversal
# Left ->Right -> Root
    def PostorderTraversal(self, root):
        res = []
        if root:
            res = self.PostorderTraversal(root.left)
            res = res + self.PostorderTraversal(root.right)
            res.append(root.data)
        return res

root = Node(27)
root.insert(14)
root.insert(35)
root.insert(10)
root.insert(19)
root.insert(31)
root.insert(42)
print(root.PostorderTraversal(root))
```

