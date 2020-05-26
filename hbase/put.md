# HBase 创建数据(put)

HBase每次执行写操作都会写入两个地方：预写式日志（write-ahead log，也称HLog）和MemStore（写入缓冲区），以保证数据持久化，只有当这两个地方的变化信息都写入并确认后，才认为写动作完成。MemStore是内存里的写入缓冲区，HBase中数据在永久写入硬盘之前在这里累积，当MemStore填满后，其中的数据会刷写到硬盘，生成一个HFile。

本章将介绍如何在HBase表中创建的数据。要在HBase表中创建的数据，可以下面的命令和方法：

- **put** 命令,
- **add() -** Put类的方法
- **put() -** HTable 类的方法.

## 插入数据

使用put命令，可以插入行到一个表。

**它的语法如下：**

```
put '<table name>','row1','<colfamily:colname>','<value>'
```

**示例** 

将第一行的值插入到emp表如下所示。

```hbase
put 'emp','1','personal data:name','raju';
put 'emp','1','personal data:city','hyderabad';
put 'emp','1','professional;
put 'emp','1','professional data:salary','50000';
```

以相同的方式使用put命令插入剩余的行。如果插入完成整个表格，会得到下面的输出。

```hbase
scan 'emp'
```

## 更新数据

可以使用put命令更新现有的单元格值。按照下面的语法，并注明新值，如下图所示。

```
put ‘table name’,’row ’,'Column family:column name',’new value’
```

新给定值替换现有的值，并更新该行。

**示例** 

假设HBase中有一个表emp拥有下列数据

```
scan 'emp'
```

以下命令将更新名为“Raju'员工的城市值为'Delhi'。

```hbase
put 'emp','row1','personal:city','Delhi'
```

更新后的表如下所示，观察这个城市Raju的值已更改为“Delhi”。



