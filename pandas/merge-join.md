# Pandas 合并/连接

Pandas具有功能全面的高性能内存中连接操作，与SQL等关系数据库非常相似。
Pandas提供了一个单独的`merge()`函数，作为DataFrame对象之间所有标准数据库连接操作的入口 -

```
pd.merge(left, right, how='inner', on=None, left_on=None, right_on=None,
left_index=False, right_index=False, sort=True)
```

在这里，有以下几个参数可以使用 -

- *left* - 一个DataFrame对象。
- *right* - 另一个DataFrame对象。
- *on* - 列(名称)连接，必须在左和右DataFrame对象中存在(找到)。
- *left_on* - 左侧DataFrame中的列用作键，可以是列名或长度等于DataFrame长度的数组。
- *right_on* - 来自右的DataFrame的列作为键，可以是列名或长度等于DataFrame长度的数组。
- *left_index* - 如果为`True`，则使用左侧DataFrame中的索引(行标签)作为其连接键。 在具有MultiIndex(分层)的DataFrame的情况下，级别的数量必须与来自右DataFrame的连接键的数量相匹配。
- *right_index* - 与右DataFrame的*left_index*具有相同的用法。
- *how* - 它是*left*, *right*, *outer*以及*inner*之中的一个，默认为内*inner*。 下面将介绍每种方法的用法。
- *sort* - 按照字典顺序通过连接键对结果DataFrame进行排序。默认为`True`，设置为`False`时，在很多情况下大大提高性能。

现在创建两个不同的DataFrame并对其执行合并操作。

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
print(left)
print("========================================")
print(right)
```

**在一个键上合并两个数据帧**

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on='id')
print(rs)
```

**合并多个键上的两个数据框**

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left,right,on=['id','subject_id'])
print(rs)
```

## 合并使用“how”的参数

如何合并参数指定如何确定哪些键将被包含在结果表中。如果组合键没有出现在左侧或右侧表中，则连接表中的值将为`NA`。

这里是`how`选项和SQL等效名称的总结 -

| 合并方法 | SQL等效            | 描述             |
| -------- | ------------------ | ---------------- |
| `left`   | `LEFT OUTER JOIN`  | 使用左侧对象的键 |
| `right`  | `RIGHT OUTER JOIN` | 使用右侧对象的键 |
| `outer`  | `FULL OUTER JOIN`  | 使用键的联合     |
| `inner`  | `INNER JOIN`       | 使用键的交集     |

**Left Join示例**

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='left')
print(rs)
```

**Right Join示例**

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='right')
print(rs)
```

**Outer Join示例**

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, how='outer', on='subject_id')
print(rs)
```

**Inner Join示例**

连接将在索引上进行。连接(`Join`)操作将授予它所调用的对象。所以，`a.join(b)`不等于`b.join(a)`。

```python
import pandas as pd
left = pd.DataFrame({
         'id':[1,2,3,4,5],
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5']})
right = pd.DataFrame(
         {'id':[1,2,3,4,5],
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5']})
rs = pd.merge(left, right, on='subject_id', how='inner')
print(rs)
```