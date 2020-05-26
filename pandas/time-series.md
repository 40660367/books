# Pandas 时间序列(time series)

**Pandas**提供了各种工具(功能)，可以轻松地将`Series`，`DataFrame`对象组合在一起。

```
pd.concat(objs,axis=0,join='outer',join_axes=None,ignore_index=False)
```

其中，

- *objs* - 这是Series，DataFrame或Panel对象的序列或映射。
- *axis* - `{0，1，...}`，默认为`0`，这是连接的轴。
- *join* - `{'inner', 'outer'}`，默认`inner`。如何处理其他轴上的索引。联合的外部和交叉的内部。
- *ignore_index* − 布尔值，默认为`False`。如果指定为`True`，则不要使用连接轴上的索引值。结果轴将被标记为：`0，...，n-1`。
- *join_axes* - 这是Index对象的列表。用于其他`(n-1)`轴的特定索引，而不是执行内部/外部集逻辑。

## 连接对象

`concat()`函数完成了沿轴执行级联操作的所有重要工作。下面代码中，创建不同的对象并进行连接。

```python
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two])
print(rs)
```

假设想把特定的键与每个碎片的DataFrame关联起来。可以通过使用键参数来实现这一点 -

```python
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two],keys=['x','y'])
print(rs)
```

结果的索引是重复的; 每个索引重复。如果想要生成的对象必须遵循自己的索引，请将`ignore_index`设置为`True`。参考以下示例代码 - 

```python
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two],keys=['x','y'],ignore_index=True)

print(rs)
```

观察，索引完全改变，键也被覆盖。如果需要沿`axis=1`添加两个对象，则会添加新列。

```python
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = pd.concat([one,two],axis=1)
print(rs)
```

#### 使用附加连接

连接的一个有用的快捷方式是在Series和DataFrame实例的`append`方法。这些方法实际上早于`concat()`方法。 它们沿`axis=0`连接，即索引 -

```python
import pandas as pd
one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])
two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = one.append(two)
print(rs)
```

`append()`函数也可以带多个对象 -

```python
import pandas as pd

one = pd.DataFrame({
         'Name': ['Alex', 'Amy', 'Allen', 'Alice', 'Ayoung'],
         'subject_id':['sub1','sub2','sub4','sub6','sub5'],
         'Marks_scored':[98,90,87,69,78]},
         index=[1,2,3,4,5])

two = pd.DataFrame({
         'Name': ['Billy', 'Brian', 'Bran', 'Bryce', 'Betty'],
         'subject_id':['sub2','sub4','sub3','sub6','sub5'],
         'Marks_scored':[89,80,79,97,88]},
         index=[1,2,3,4,5])
rs = one.append([two,one,two])
print(rs)
```

## 时间序列

*Pandas*为时间序列数据的工作时间提供了一个强大的工具，尤其是在金融领域。在处理时间序列数据时，我们经常遇到以下情况 -

- 生成时间序列
- 将时间序列转换为不同的频率

*Pandas*提供了一个相对紧凑和自包含的工具来执行上述任务。

### 获取当前时间

`datetime.now()`用于获取当前的日期和时间。

```python
import pandas as pd
pd.datetime.now()
```

#### 创建一个时间戳

时间戳数据是时间序列数据的最基本类型，它将数值与时间点相关联。 对于*Pandas*对象来说，意味着使用时间点。举个例子 -

```python
import pandas as pd
time = pd.Timestamp('2018-11-01')
print(time)
```

也可以转换整数或浮动时期。这些的默认单位是纳秒(因为这些是如何存储时间戳的)。 然而，时代往往存储在另一个可以指定的单元中。 再举一个例子 - 

```python
import pandas as pd
time = pd.Timestamp(1588686880,unit='s')
print(time)
```

#### 创建一个时间范围

```python
import pandas as pd

time = pd.date_range("12:00", "23:59", freq="30min").time
print(time)
```

#### 改变时间的频率

```python
import pandas as pd

time = pd.date_range("12:00", "23:59", freq="H").time
print(time)
```

#### 转换为时间戳

要转换类似日期的对象(例如字符串，时代或混合)的序列或类似列表的对象，可以使用`to_datetime`函数。当传递时将返回一个Series(具有相同的索引)，而类似列表被转换为`DatetimeIndex`。 看看下面的例子 -

```python
import pandas as pd

time = pd.to_datetime(pd.Series(['Jul 31, 2009','2019-10-10', None]))
print(time)
```

`NaT`表示不是一个时间的值(相当于`NaN`)

举一个例子，

```python
import pandas as pd
import pandas as pd
time = pd.to_datetime(['2009/11/23', '2019.12.31', None])
print(time)
```

