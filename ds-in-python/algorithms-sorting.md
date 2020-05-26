# Python实现算法:排序

排序是指以特定格式排列数据。 排序算法指定按特定顺序排列数据的方式。 最常见的排序是数字或字典顺序。

排序的重要性在于，如果数据是以分类方式存储，数据搜索可以优化到非常高的水平。 排序也用于以更易读的格式表示数据。 下面来看看python中实现的5种排序方式。

- 冒泡排序
- 合并排序
- 插入排序
- 希尔排序
- 选择排序

## 冒泡排序

它是一种基于比较的算法，其中每对相邻元素进行比较，如果元素不合适，元素将进行交换。

```python
def bubblesort(list):

# Swap the elements to arrange in order
    for iter_num in range(len(list)-1,0,-1):
        for idx in range(iter_num):
            if list[idx]>list[idx+1]:
                temp = list[idx]
                list[idx] = list[idx+1]
                list[idx+1] = temp


list = [19,2,31,45,6,11,121,27]
bubblesort(list)
print(list)
```

## 合并排序

合并排序首先将数组分成相等的一半，然后以排序的方式组合它们。参考以下代码实现 - 

```python
def merge_sort(unsorted_list):
    if len(unsorted_list) <= 1:
        return unsorted_list
# Find the middle point and devide it
    middle = len(unsorted_list) // 2
    left_list = unsorted_list[:middle]
    right_list = unsorted_list[middle:]

    left_list = merge_sort(left_list)
    right_list = merge_sort(right_list)
    return list(merge(left_list, right_list))

# Merge the sorted halves

def merge(left_half,right_half):

    res = []
    while len(left_half) != 0 and len(right_half) != 0:
        if left_half[0] < right_half[0]:
            res.append(left_half[0])
            left_half.remove(left_half[0])
        else:
            res.append(right_half[0])
            right_half.remove(right_half[0])
    if len(left_half) == 0:
        res = res + right_half
    else:
        res = res + left_half
    return res

unsorted_list = [64, 34, 25, 12, 22, 11, 90]

print(merge_sort(unsorted_list))
```

## 插入排序

插入排序包括为排序列表中的给定元素找到正确的位置。 所以在开始时比较前两个元素并通过比较来对它们进行排序。 然后选取第三个元素，并在前两个排序元素中找到它的正确位置。 通过这种方式，逐渐将更多元素添加到已排序的列表中，并将它们置于适当的位置。

参考下面代码的实现 - 

```python
def insertion_sort(InputList):
    for i in range(1, len(InputList)):
        j = i-1
        nxt_element = InputList[i]
# Compare the current element with next one
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j]
            j=j-1
        InputList[j+1] = nxt_element

list = [19,2,31,45,30,11,121,27]
insertion_sort(list)
print(list)
Python
```

## 希尔排序

希尔排序涉及排序远离其他的元素。对给定列表的大型子列表进行排序，并继续缩小列表的大小，直到所有元素都被排序。 下面的程序通过将其等于列表大小的一半来找到间隙，然后开始对其中的所有元素进行排序。 然后不断重置差距，直到整个列表被排序。

```python
def shellSort(input_list):

    gap = len(input_list) / 2
    while gap > 0:

        for i in range(gap, len(input_list)):
            temp = input_list[i]
            j = i
# Sort the sub list for this gap

            while j >= gap and input_list[j - gap] > temp:
                input_list[j] = input_list[j - gap]
                j = j-gap
            input_list[j] = temp

# Reduce the gap for the next element

        gap = gap/2

list = [19,2,31,45,30,11,121,27]

shellSort(list)
print(list)
```

## 选择排序

在选择排序中，首先查找给定列表中的最小值并将其移至排序列表。 然后为未排序列表中的每个剩余元素重复该过程。 输入排序列表的下一个元素将与现有元素进行比较并放置在正确的位置。 所以最后所有来自未排序列表的元素都被排序。参考以下代码实现 - 

```python
def selection_sort(input_list):

    for idx in range(len(input_list)):

        min_idx = idx
        for j in range( idx +1, len(input_list)):
            if input_list[min_idx] > input_list[j]:
                min_idx = j
# Swap the minimum value with the compared value

        input_list[idx], input_list[min_idx] = input_list[min_idx], input_list[idx]


l = [19,2,31,45,30,11,121,27]
selection_sort(l)
print(l)
```

