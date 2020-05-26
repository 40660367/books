# Python实现算法:搜索树(binary search tree)

二叉搜索树(BST)是一棵树，其所有节点都遵循下述属性 - 节点的左子树的键小于或等于其父节点的键。 节点的右子树的键大于其父节点的键。 因此，`BST`将其所有子树分成两部分; 左边的子树和右边的子树，可以定义为 -

```python
left_subtree (keys)  ≤  node (key)  ≤  right_subtree (keys)
```

**在B树搜索的值**

在树中搜索值涉及比较输入值与退出节点的值。 在这里，也从左到右遍历节点，最后是父节点。 如果搜索到的值与任何退出值都不匹配，则返回未找到的消息，否则返回找到的消息。

```python
class Node:

    def __init__(self, data):

        self.left = None
        self.right = None
        self.data = data

# Insert method to create nodes
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
# findval method to compare the value with nodes
    def findval(self, lkpval):
        if lkpval < self.data:
            if self.left is None:
                return str(lkpval)+" Not Found"
            return self.left.findval(lkpval)
        elif lkpval > self.data:
            if self.right is None:
                return str(lkpval)+" Not Found"
            return self.right.findval(lkpval)
        else:
            print(str(self.data) + ' is found')
# Print the tree
    def PrintTree(self):
        if self.left:
            self.left.PrintTree()
        print( self.data),
        if self.right:
            self.right.PrintTree()


root = Node(12)
root.insert(6)
root.insert(14)
root.insert(3)
print(root.findval(7))
print(root.findval(14))
```

