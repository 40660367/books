# Python自带数据结构 字典(dict)

在Python字典中，每个键和值之间使用冒号(`:`)分隔，每个项之间用逗号(`,`)隔开，整个字典数据用大括号括起来。 如果是没有任何项目的空字典则使用两个大括号编写，如下所示:`{}`。

键在字典中是唯一的，而值可能不是唯一的。 字典的值可以是任何类型，但键必须是不可变的数据类型，例如:字符串，数字或元组。

## 访问字典中的值

要访问字典元素，可以使用方括号和键来获取它的值。 以下是一个简单的例子 -

```python
dict = {'Name': 'Maxsu', 'Age': 27, 'Class': 'First'}
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
```

如果尝试使用不属于字典的键来访问数据项，那么会得到错误，如下 -

```python
dict = {'Name': 'Maxsu', 'Age': 27, 'Class': 'First'}
print ("dict['Alice']: ", dict['Gender'])
```

## 更新字词

可以通过添加新条目或键值对，修改现有条目或删除现有条目来更新字典，如简单示例中所示 -

```python
dict = {'Name': 'Maxsu', 'Age': 25, 'Class': 'First'}
dict['Age'] = 28; # update existing entry
dict['School'] = "DPS School"; # Add new entry

print ("dict['Age']: ", dict['Age'])
print ("dict['School']: ", dict['School'])
```

## 删除字典元素

可以删除单个字典元素，也可以清除字典的全部内容。 也可以在一个操作中删除整个字典。
要显式删除整个字典，只需使用`del`语句。 以下是一个简单的例子 -

```python
dict = {'Name': 'Maxsu', 'Age': 27, 'Class': 'First'}
del dict['Name']; # remove entry with key 'Name'
dict.clear();     # remove all entries in dict
del dict ;        # delete entire dictionary

print("dict['Age']: ", dict['Age'])
print("dict['School']: ", dict['School'])
```

> 请注意，由于执行`del dict`之后，字典不再存在所以这里会引发异常

## 字典键的属性

字典值没有限制。 它们可以是任何任意的Python对象，无论是标准对象还是用户定义的对象。 但是，对于键就有所限制了。

关于字典键有两点要记住 -

**第1点:** 每个键不得超过一个条目，这意味着不允许重复键。 在分配过程中遇到重复键时，则以最后一次分配的为准。 例如 -

```python
dict = {'Name': 'maxsu', 'Age': 27, 'Name': 'Manni'}
print ("dict['Name']: ", dict['Name'])
```

**第2点:** 键必须是不可变的。 这意味着您可以使用字符串，数字或元组作为字典的键，但不允许使用`['key']`。 以下是一个简单的例子 -

```python
#!/usr/bin/python

dict = {['Name']: 'Maxsu', 'Age': 27}
print ("dict['Name']: ", dict['Name'])
```