# Python自带数据结构 集合(set)

在数学上，集合(Set)是不以任何特定顺序的数据项。 Python集合与此数学定义类似，但有以下附加条件。

- 集合中的元素不能重复。
- 集合中的元素是不可变的(不能被修改)，但集合作为一个整体是可变的。
- 附加到python集合中的任何元素不需要索引。所以集合不支持任何索引或切片操作。

## 集合操作

python中的集合通常用于像联合，相交，异同和补充等数学运算。下面创建一个集合，访问它的元素并执行这些数学运算。参考以下示例代码 - 

**创建一个集合**

通过使用`set()`函数或将所有元素放置在一对大括号内创建一个集合。

```python
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
Months={"Jan","Feb","Mar"}
Dates={21,22,17}
print(Days)
print(Months)
print(Dates)
```

**访问集合中的值**

我们无法访问集合中的单个值。只能如上所示访问所有元素。 但是也可以通过遍历该集合来获取单个元素的列表。

```python
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])

for d in Days:
    print(d)
```

**将项目添加到集合**

可以使用`add()`方法将元素添加到集合中。附加到新添加的元素不需要指定索引。

```python
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])

Days.add("Sun")
print(Days)
```

**从集合中删除项目**

可以使用`discard()`方法从集合中删除元素。参考以下代码实现 - 

```python
Days=set(["Mon","Tue","Wed","Thu","Fri","Sat"])

Days.discard("Sun")
print(Days)
```

**集合的联合操作**

两个集合上的联合操作产生一个包含来自两个集合的所有不同元素的新集合。 在下面的例子中，元素`"Wed"`出现在两个集合中。

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA|DaysB
print(AllDays)
```

**集合的交集**

两个集合上的交集操作产生一个新的集合，其中只包含来自两个集合的共同元素。 在下面的例子中，元素`"Wed"`出现在两个集合中。

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA & DaysB
print(AllDays)
```

 **集合的差集**

对两组进行差异化操作会产生一个新的集合，其中只包含来自第一集合的元素，而不包含第二集合中的元素。 在下面的例子中，元素`Wed`出现在两个集合中，所以它不会在结果集中找到。

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Wed","Thu","Fri","Sat","Sun"])
AllDays = DaysA - DaysB
print(AllDays)
```

**比较集合**

可以检查一个给定的集合是否是另一个集合的子集或超集。 结果是`True`或`False`，取决于组中存在的元素。

```python
DaysA = set(["Mon","Tue","Wed"])
DaysB = set(["Mon","Tue","Wed","Thu","Fri","Sat","Sun"])
SubsetRes = DaysA <= DaysB
SupersetRes = DaysB >= DaysA
print(SubsetRes)
print(SupersetRes)
```

