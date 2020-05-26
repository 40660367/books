# Python实现算法:递归(recursion) 			

递归允许函数自调用。 修复代码的步骤会一次又一次地执行新值。 还必须设置判断递归调用何时结束的标准。 在下面的例子中，演示如何使用二进制搜索的递归方法。采用一个排序列表，并将其索引范围作为递归函数的输入。

**使用递归进行二进制搜索**

使用python实现二进制搜索算法，如下所示。 我们使用有序的项目列表，并设计一个递归函数，将起始索引和结束索引作为输入列表。 然后二进制搜索函数自行调用，直到搜索到项目或在列表中结束。

参考以下代码实现 - 

```python
def bsearch(list, idx0, idxn, val):

    if (idxn < idx0):
        return None
    else:
        midval = idx0 + ((idxn - idx0) // 2)
# Compare the search item with middle most value

        if list[midval] > val:
            return bsearch(list, idx0, midval-1,val)
        elif list[midval] < val:
            return bsearch(list, midval+1, idxn, val)
        else:
            return midval

list = [8,11,24,56,88,131]
print(bsearch(list, 0, 5, 24))
print(bsearch(list, 0, 5, 51))
```