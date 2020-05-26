# Python实现算法:搜索

将数据存储在不同的数据结构中时，搜索是非常基本的必需条件。 最简单的方法是遍历数据结构中的每个元素，并将其与要搜索的值进行匹配。

 这就是所谓的线性搜索。 它效率低下，很少使用。

下面创建一个程序演示如何实现一些高级搜索算法。

## 线性搜索

在这种类型的搜索中，逐个搜索所有项目。 每个项目都会被检查匹配，如果找到匹配项，那么返回该特定项目，否则搜索将继续到数据结构的末尾。

```python
def linear_search(values, search_for):
    search_at = 0
    search_res = False

# Match the value with each data element    
    while search_at < len(values) and search_res is False:
        if values[search_at] == search_for:
            search_res = True
        else:
            search_at = search_at + 1

    return search_res

l = [64, 34, 25, 12, 22, 11, 90]
print(linear_search(l, 12))
print(linear_search(l, 91))
```

## 插值搜索

该搜索算法适用于所需值的探测位置。 为了使该算法正常工作，数据收集应该以排序形式并平均分布。 最初，探针位置是集合中最大项目的位置。如果匹配发生，则返回项目的索引。 如果中间项目大于项目，则再次在中间项目右侧的子数组中计算探针位置。 否则，该项目将在中间项目左侧的子数组中搜索。 这个过程在子数组上继续，直到子数组的大小减小零。

有一个特定的公式来计算下面的程序中指出的中间位置。参考以下代码的实现 - 

```python
def intpolsearch(values,x ):
    idx0 = 0
    idxn = (len(values) - 1)

    while idx0 <= idxn and x >= values[idx0] and x <= values[idxn]:

# Find the mid point
        mid = idx0 +\
               int(((float(idxn - idx0)/( values[idxn] - values[idx0]))
                    * ( x - values[idx0])))

# Compare the value at mid point with search value 
        if values[mid] == x:
            return "Found "+str(x)+" at index "+str(mid)

        if values[mid] < x:
            idx0 = mid + 1
    return "Searched element not in the list"


l = [2, 6, 11, 19, 27, 31, 45, 121]
print(intpolsearch(l, 2))
```

