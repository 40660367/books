# Scala 集(collection)

Scala拥有丰富的集合库。集合是一种用来存储各种对象和数据的容器。 这些容器可以被排序，诸如列表，元组，选项，映射等的线性集合。集合可以具有任意数量的元素或被限制为零或一个元素(例如，`Option`)。

集合可以是严格的(`strict`)或懒惰的(`Lazy`)。 懒惰集合的元素在访问之前可能不会使用内存，例如`Ranges`。 此外，集合可能是可变的(引用的内容可以改变)或不可变的(引用引用的东西从不改变)。 请注意，不可变集合可能包含可变项目。

对于一些问题，可变集合的工作更好，而对于其他集合，不可变集合的工作更好。 如果有疑问，最好从不可变集合开始，如果需要可变集合，可以更改为可变集合。

本章将介绍最常用的集合类型以及对这些集合最常用的操作。

| 序号 | 方法                                                 | 描述                                                |
| ---- | ---------------------------------------------------- | --------------------------------------------------- |
| 1    | [Scala 链表(list)](./collection-list.html)           | Scala List[T]是`T`型链表。                          |
| 2    | [Scala 集合(set)](./collection-set.html)             | 一组是相同类型的成对不同元素的集合。                |
| 3    | [Scala 映射(map)](./collection-map.html)             | 映射是键/值对的集合，任何值都可以根据其键进行检索。 |
| 4    | [Scala 元组(tuple)](./collection-tuple.html)         | 与数组或列表不同，元组可以容纳不同类型的对象。      |
| 5    | [Scala option](./collection-option.html)             | `Option[T]`提供一个给定类型的零个或一个元素的容器。 |
| 6    | [Scala 迭代器(iterator)](./collection-iterator.html) | 迭代器不是集合，而是一种逐个访问集合元素的方法。    |