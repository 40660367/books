# Python实现算法:图遍历

图在解决许多重要的数学难题中是非常有用的数据结构。 例如计算机网络拓扑或分析化学化合物的分子结构。 它们还用于城市交通或路线规划，甚至用于人类语言和语法。 所有这些应用程序都有遍历图的共同挑战，并确保图的所有节点都被访问。 有两种常见的已建立的方法来进行这种遍历，下面将对其进行描述。

## 深度优先遍历:

也称为深度优先搜索(DFS)，该算法使用堆栈记住在任何迭代中发生死角时开始搜索的下一个顶点。 使用设置的数据类型在python中实现DFS图，因为它们提供了跟踪访问和未访问节点所需的功能。

参考以下代码的实现 - 

```python
class graph:

    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict
# Check for the visisted and unvisited nodes
def dfs(graph, start, visited = None):
    if visited is None:
        visited = set()
    visited.add(start)
    print(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited

gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }


dfs(gdict, 'a')
```

## 广度优先遍历

也称为广度优先搜索(BFS)，该算法使用队列记住当任何迭代中发生死角时，获取下一个顶点以开始搜索。

我们使用之前讨论的队列数据结构在python中实现BFS。 当继续访问相邻的未访问节点并继续将其添加到队列中。然后，开始只出现没有未访问节点的节点。 当没有下一个相邻节点被访问时，停止程序。

参考以下代码的实现 - 

```python
import collections
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

def bfs(graph, startnode):
# Track the visited and unvisited nodes using queue
        seen, queue = set([startnode]), collections.deque([startnode])
        while queue:
            vertex = queue.popleft()
            marked(vertex)
            for node in graph[vertex]:
                if node not in seen:
                    seen.add(node)
                    queue.append(node)

def marked(n):
    print(n)

# The graph dictionary
gdict = { "a" : set(["b","c"]),
                "b" : set(["a", "d"]),
                "c" : set(["a", "d"]),
                "d" : set(["e"]),
                "e" : set(["a"])
                }

bfs(gdict, "a")
```

