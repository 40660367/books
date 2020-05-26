# Python3 数据类型-集合(set)

集合(set)是一个无序的不重复元素序列。

## 创建Python集合

可以使用大括号 `{ }` 或者 `set()` 函数创建集合

**注意：**

创建一个空集合必须用`set()`而不是 `{}`，因为 `{}` 是用来创建一个空字典。

创建格式：`parame = {value01,value02,...};set(value)`

#### 练习:创建Python集合
```Python
basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # 这里演示的是去重功能

print('orange' in basket)                 # 快速判断元素是否在集合内

print('crabgrass' in basket)
```

#### 练习:两个集合间的运算.
```Python
a = set('abracadabra')
b = set('alacazam')
print(a)                          
print(a - b)                               # 集合a中包含而集合b中不包含的元素
print(a | b)                               # 集合a或b中包含的所有元素
print(a & b)                               # 集合a和b中都包含了的元素
print(a ^ b)                               # 不同时包含于a和b的元素
```
#### 练习:集合推导式(Set comprehension)

```Python
a = {x for x in 'abracadabra' if x not in 'abc'}
a
```

## 集合的基本操作

### 1、添加元素

语法格式如下：`s.add( x )`

将元素 x 添加到集合`s`中，如果元素已存在，则不进行任何操作。

#### 练习:Python集合添加元素

```Python
aset = set(("Google", "Python", "Taobao"))
aset.add("Facebook")
print(aset)
```

还有一个方法，也可以添加元素，且参数可以是列表，元组，字典等，语法格式如下：

```Python
aset = set(("Google", "Python", "Taobao"))
bset=set(("Bilibili",))
bset.update( aset )
bset
```

`bset`可以有多个，用逗号分开。

```Python
thisset = set(("Google", "Python", "Taobao"))
thisset.update({1,3})
print(thisset)
thisset.update([1,4],[5,6])  
print(thisset)
```

### 2、移除元素

语法格式：`s.remove( x )`

将元素 x 从集合 s 中移除，如果元素不存在，则会发生错误。

#### 练习:Python集合移除元素
```Python
cset = set(("Google", "Python", "Taobao"))
cset.remove("Taobao")

print(cset)

cset.remove("Facebook")   # 不存在会发生错误
```

此外还有一个方法也是移除集合中的元素，且如果元素不存在，不会发生错误。格式如下所示：`s.discard( x )`

```Python
cset = set(("Google", "Python", "Taobao")) 
cset.discard("Facebook")  # 不存在不会发生错误 
print(cset)
```

我们也可以设置随机删除集合中的一个元素，语法格式如下：`s.pop()`

#### 练习:脚本模式实现

```Python
%%writefile dset.py
thisset = set(("Google", "Python", "Taobao", "Facebook"))
x = thisset.pop() 
print(x)
```
执行并查看

```Python
!python3 dset.py
```

多次执行测试结果都不一样。

set 集合的`pop()`方法会对集合进行无序的排列，然后将这个无序排列集合的左面第一个元素进行删除。

### 3、计算集合元素个数

语法格式：`len(s)`

#### 练习:Python计算集合元素个数

```Python
dset = set(("Google", "Python", "Taobao"))
len(dset)
```
### 4、清空集合

语法格式：`s.clear()`


#### 练习:清空Python集合 
```Python
eset = set(("Google", "Python", "Taobao"))
eset.clear()
print(eset)
```

### 5、判断元素是否在集合中存在

语法格式：`x in s`

判断元素`x`是否在集合`s`中，存在返回 True，不存在返回 False。

#### 练习:Python集合 判断
```Python
thisset = set(("Google", "Python", "Taobao"))
print("Python" in thisset)
print("Facebook" in thisset)
```
### 集合内置方法完整列表

```Python
dir(set())
```

| 方法                    | 描述                                         |
| :---------------------- | :------------------------------------------- |
| `add()`                 | 为集合添加元素                               |
| `clear()`               | 移除集合中的所有元素                         |
| `copy()`                | 拷贝一个集合                                 |
| `difference()`          | 返回多个集合的差集                           |
| `difference_update()`   | 移除集合中的元素，该元素在指定的集合也存在。 |
| `discard()`             | 删除集合中指定的元素                         |
| `intersection()`        | 返回集合的交集                               |
| `intersection_update()` | 返回集合的交集。                             |