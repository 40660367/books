# Python3 数据类型-字典(dict)

字典(Dict)是另一种可变容器模型，且可存储任意类型对象。

## 字典的键值对应

字典的每个键值(key=>value)对用冒号`:`分割，每个对之间用逗号,分割，整个字典包括在花括号`{}`中 

格式：`d = {key1 : value1, key2 : value2 }`

键必须是唯一的，但值则不必。

值可以取任何数据类型，但键必须是不可变的，如字符串，数字或元组。

#### 练习：创建字典

```Python
dict1 = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
dict1
```

也可如此创建字典：

```Python
dict1 = { 'abc': 456 }
dict2 = { 'abc': 123, 98.6: 37 }
print(dict1)
print(dict2)
```

## 访问字典内对象

#### 练习：访问字典内对象

把相应的键放入到方括号中。

```Python
dict = {'Name': 'Python', 'Age': 30, 'Class': 'First'}
 
print("dict['Name']: ", dict['Name'])
print("dict['Age']: ", dict['Age'])
```

如果用字典里没有的键访问数据，会输出错误如下：

```Python
print("dict['Alice']: ", dict['Alice'])#KeyError: 'Alice'
```

## 修改字典内对象

向字典添加新内容的方法是增加新的键/值对，修改或删除已有键/值对如下实例:

#### 练习：修改字典内对象

```Python
dict1 = {'Name': 'Python', 'Age': 30, 'Class': 'First'}
 
del dict1['Name'] # 删除键 'Name'
 
print("dict['Age']:", dict1['Age'])
print("dict['Name']:", dict1['Name'])#KeyError: 'Name'

dict1.clear()     # 清空字典
del dict1         # 删除字典
```

## 删除字典内对象

能删单一的元素也能清空字典，清空只需一项操作。显示删除一个字典用`del`命令。

#### 练习：删除字典内对象

```Python
dict1 = {'Name': 'Python', 'Age': 7, 'Class': 'First'}
 
del dict1['Name'] # 删除键 'Name'

print("dict1['Age']: ", dict1['Age'])#Age键存在
print("dict1['Name']: ", dict1['Name'])#Name键已经删除，该行会报错
```

但这会引发一个异常，因为用执行`del`操作后字典不再存在。

### 字典键的特性

#### 练习:字典键的使用

字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。

两个重要的点需要记住：

1）不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：

```Python
dict2 = {'Name': 'Python1', 'Age': 7, 'Name': 'Python2'}
 
print("dict2['Name']: ", dict2['Name'])
```

2) 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行，如下实例：

```Python
dict3 = {['Name']: 'Python', 'Age': 7}
 
print("dict3['Name']: ", dict3['Name'])
```

## 字典内置函数&方法

Python字典包含了以下内置函数：

| 序号 | 函数及描述                                                   | 实例                                                         |
| :--- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 1    | `len(dict) `计算字典元素个数，即键的总数。                   | `dict = {'Name': 'Python', 'Age': 22, 'Class': 'First'};len(dict)` |
| 2    | `str(dict) `输出字典，以可打印的字符串表示。                 | `dict = {'Name': 'Python', 'Age': 22, 'Class': 'First'} ;str(dict) ` |
| 3    | `type(variable) `返回输入的变量类型，如果变量是字典就返回字典类型。 | `type({})`                                                   |

## Python字典包含了以下内置方法：

```Python
help({})
```