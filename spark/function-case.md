# Spark 函数(function)

[环境准备](./setup.html)

## Map函数示例

Map通过函数传递源的每个元素，并形成新的分布式数据集。

在此示例中，我们为每个元素添加一个常量值`10`。

使用并行化集合创建RDD。

```scale
val data = sc.parallelize(List(10,20,30))
```

现在，可以使用以下命令读取生成的结果。

```scale
data.collect
```

应用map函数并传递执行所需的表达式。

```scale
val mapfunc = data.map(x => x+10)
```

现在，可以使用以下命令读取生成的结果。

```scale
mapfunc.collect
```

## Filter函数示例

在Spark中，Filter函数返回一个新数据集，该数据集是通过选择函数返回`true`的源元素而形成的。因此，它仅检索满足给定条件的元素。

在此示例中，将过滤给定数据并检索除`35`之外的所有值。

使用并行化集合创建RDD。

```shell
val data = sc.parallelize(List(10,20,35,40))
```

现在，可以使用以下命令读取生成的结果。

```shell
data.collect
```

应用过滤器函数并传递执行所需的表达式。

```shell
val filterfunc = data.filter(x => x!=35)
```

现在，可以使用以下命令读取生成的结果。

```shell
filterfunc.collect
```

## count函数的示例

在Spark中，`count`函数返回数据集中存在的元素数。

在此示例中，计算数据集中存在的元素数量。使用并行化集合创建RDD。

```
val data = sc.parallelize(List(1,2,3,4,5))
```

现在，可以使用以下命令读取生成的结果。

```
data.collect
```

应用`count()`函数来计算元素数。

```
scala> val countfunc = data.count()
```

## Distinct函数的示例

在Spark中，`Distinct`函数返回提供的数据集中的不同元素。

在此示例中，忽略重复元素并仅检索不同的元素

使用并行化集合创建RDD。

```
val data = sc.parallelize(List(10,20,20,40))
```

现在，可以使用以下命令读取生成的结果。

```
data.collect
```

应用`distinct()`函数来忽略重复的元素。

```
val distinctfunc = data.distinct()
```

现在，可以使用以下命令读取生成的结果。

```
distinctfunc.collect
```

## Union函数示例

在Spark中，`Union`函数返回一个新数据集，其中包含不同数据集中存在的元素组合。

在此示例中，组合了两个数据集的元素。

使用并行化集合创建RDD。

```scale
val data1 = sc.parallelize(List(1,2))
```

现在，可以使用以下命令读取生成的结果。

```scale
data1.collect
```

使用并行化集合创建另一个RDD。

```scale
val data2 = sc.parallelize(List(3,4,5))
```

现在，可以使用以下命令读取生成的结果。

```scale
data2.collect
```

应用`union()`函数返回元素的并集。

```scala
val unionfunc = data1.union(data2)
```

现在，可以使用以下命令读取生成的结果。

```scale
unionfunc.collect
```