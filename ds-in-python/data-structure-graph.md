# Python实现数据结构 图(graph)

图是一组对象通过链接连接的一组对象的图形表示。 互连对象由称为顶点的点表示，连接顶点的链接称为边。 在这里详细描述了与图相关的各种术语和功能。 在本章中，我们将演示如何使用python程序创建图并向其添加各种数据元素。 以下是在图表上执行的基本操作。

- 显示图形顶点
- 显示图形边缘
- 添加一个顶点
- 添加边缘
- 创建一个图

可以使用python字典数据类型轻松呈现图。 我们将顶点表示为字典的关键字，顶点之间的连接也称为边界，作为字典中的值。

看看下面的图 -

![img](./images/graph)

在上面的图中 - 

```
V = {a, b, c, d, e}
E = {ab, ac, bd, cd, de}
```

可以在下面的python程序中展示这个图 - 

```python
# Create the dictionary with graph elements
graph = { "a" : ["b","c"],
          "b" : ["a", "d"],
          "c" : ["a", "d"],
          "d" : ["e"],
          "e" : ["d"]
         }

# Print the graph
print(graph)
```

**显示图的顶点**

要显示图顶点，简单地找到图字典的关键字，使用`keys()`方法。

```python
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = []
        self.gdict = gdict

# Get the keys of the dictionary
    def getVertices(self):
        return list(self.gdict.keys())

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

print(g.getVertices())
```

**显示图的边缘**

寻找图边缘比顶点少一些，因为必须找到每对顶点之间有一个边缘的顶点。 因此，创建一个空边列表，然后迭代与每个顶点关联的边值。 一个列表形成了包含从顶点找到的不同组的边。

```
[{'a', 'b'}, {'c', 'a'}, {'d', 'b'}, {'c', 'd'}, {'d', 'e'}]
```

**添加一个顶点**

添加一个顶点很简单,直接添加另一个键到图字典。

```python
class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def getVertices(self):
        return list(self.gdict.keys())

# Add the vertex as a key
    def addVertex(self, vrtx):
       if vrtx not in self.gdict:
            self.gdict[vrtx] = []

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)

g.addVertex("f")

print(g.getVertices())
```

**添加边**

将边添加到现有图, 涉及将新顶点视为元组并验证边是否已经存在。 如果不存在，则添加边缘。

```python
class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def edges(self):
        return self.findedges()
# Add the new edge

    def AddEdge(self, edge):
        edge = set(edge)
        (vrtx1, vrtx2) = tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1] = [vrtx2]

# List the edge names
    def findedges(self):
        edgename = []
        for vrtx in self.gdict:
            for nxtvrtx in self.gdict[vrtx]:
                if {nxtvrtx, vrtx} not in edgename:
                    edgename.append({vrtx, nxtvrtx})
        return edgename

# Create the dictionary with graph elements
graph_elements = { "a" : ["b","c"],
                "b" : ["a", "d"],
                "c" : ["a", "d"],
                "d" : ["e"],
                "e" : ["d"]
                }

g = graph(graph_elements)
g.AddEdge({'a','e'})
g.AddEdge({'a','c'})
print(g.edges())
```