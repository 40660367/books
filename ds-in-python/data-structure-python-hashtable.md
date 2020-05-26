# Python实现数据结构 哈希表(hash table)

散列表(也叫哈希表)是一种数据结构，其数据元素的地址或索引值由散列函数生成。 这使得访问数据的速度更快，因为索引值是数据值的关键字。 换句话说，哈希表存储键值对，但键是通过哈希函数生成的。

因此，数据元素的搜索和插入函数变得更快，因为键值本身成为存储数据的数组的索引。

在Python中，字典数据类型表示哈希表的实现。字典中的键满足以下要求。

- 字典的键是可散列的，即通过散列函数生成该散列函数，该散列函数为提供给散列函数的每个唯一值生成唯一结果。
- 字典中数据元素的顺序不固定。

所以可通过使用下面的字典数据类型来看到哈希表的实现。

## 在字典中访问值

要访问字典元素，可以使用熟悉的方括号 - `[]` 来获取它的值。

```python
# Declare a dictionary 
dict1 = {'Name': 'maxsu', 'Age': 27, 'Class': 'First'}

# Accessing the dictionary with its key
print("dict1['Name']: ", dict1['Name'])
print("dict1['Age']: ", dict1['Age'])
```

## 更新字典元素

可以通过添加新条目或键值对，修改现有条目或删除现有条目来更新字典，如简单示例中所示 -

```python
# Declare a dictionary
dict2 = {'Name': 'Maxsu', 'Age': 26, 'Class': 'First'}
dict2['Age'] = 8; # update existing entry
print("dict2['Age']: ", dict2['Age'])
```

## 删除字典元素

可以删除单个字典元素，也可以清除字典的全部内容。 也可以在一个操作中删除整个字典。 要显式删除整个字典，只需使用`del`语句。 参考以下代码 -

```python
dict3 = {'Name': 'Maxsu', 'Age': 26, 'Class': 'First'}
del dict3['Name']; # remove entry with key 'Name'
dict3.clear();     # remove all entries in dict
del dict3 ;        # delete entire dictionary

print ("dict3['Age']: ", dict3['Age'])
print ("dict3['School']: ", dict[3'School'])
```

> 请注意，由于在执行`del`语句之后，字典不再存在之后会引发异常。