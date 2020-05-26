# Hbase 列族(column family)

hbase表中的每个列，都归属与某个列族。列族是表的chema的一部分(而列不是)，必须在使用表之前定义。列名都以列族作为前缀。例如courses:history，courses:math都属于courses这个列族。

访问控制、磁盘和内存的使用统计都是在列族层面进行的。

实际应用中，列族上的控制权限能帮助我们管理不同类型的应用：我们允许一些应用可以添加新的基本数据、一些应用可以读取基本数据并创建继承的列族、一些应用则只允许浏览数据（甚至可能因为隐私的原因不能浏览所有数据）。

### 单元Cell

HBase中通过{row key, columnFamily, version} 唯一确定的一个存贮单元称为cell。由{row key, column( =`<family>` + `<label>`), version} 唯一确定的单元。cell中的数据是没有类型的，全部是字节码形式存储。

### Time Stamp

每个cell都保存着同一份数据的多个版本。版本通过时间戳来索引。时间戳的类型是 64位整型。时间戳可以由hbase(在数据写入时自动 )赋值，此时时间戳是精确到毫秒的当前系统时间。时间戳也可以由客户显式赋值。如果应用程序要避免数据版本冲突，就必须自己生成具有唯一性的时间戳。每个cell中，不同版本的数据按照时间倒序排序，即最新的数据排在最前面。



HBase 目前对于两列族或三列族以上的任何项目都不太合适，因此请将模式中的列族数量保持在较低水平。目前，flushing 和 compactions 是按照每个区域进行的，所以如果一个列族承载大量数据带来的 flushing，即使所携带的数据量很小，也会 flushing 相邻的列族。当许多列族存在时，flushing 和 compactions 相互作用可能会导致一堆不必要的 I/O（要通过更改 flushing 和 compactions 来针对每个列族进行处理）。

如果你可以在你的模式中尝试使用一个列族。在数据访问通常是列作用域的情况下，仅引入第二和第三列族；即你查询一个列族或另一个列族，但通常不是两者同时存在。

**ColumnFamilies的基数**

在一个表中存在多个 ColumnFamilies 的情况下，请注意基数（即行数）。如果 ColumnFamilyA 拥有100万行并且 ColumnFamilyB 拥有10亿行，则ColumnFamilyA 的数据可能会分布在很多很多地区（以及 Region Server）中。这使得 ColumnFamilyA 的大规模扫描效率较低。