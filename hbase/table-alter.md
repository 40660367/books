# HBase 表描述和修改

## 描述

该命令返回表的说明。它的语法如下：

```
describe 'table name'
```

下面给出的是对emp表的 **describe** 命令的输出。

```
describe 'emp'
```

## 修改

alter用于更改现有表的命令。使用此命令可以更改列族的单元，设定最大数量和删除表范围运算符，并从表中删除列家族。

### 更改列族单元格的最大数目

下面给出的语法来改变列家族单元的最大数目。

```
alter 't1', NAME => 'f1', VERSIONS => 5
```

在下面的例子中，单元的最大数目设置为5。

```
alter 'emp', NAME => 'personal data', VERSIONS => 5
```

## 表范围运算符

使用alter，可以设置和删除表范围，运算符，如MAX_FILESIZE，READONLY，MEMSTORE_FLUSHSIZE，DEFERRED_LOG_FLUSH等。

### 设置只读

下面给出的是语法，是用以设置表为只读。

```
alter 'tablename', READONLY(option)
```

在下面的例子中，我们已经设置表emp为只读。

```
alter 'emp', READONLY
```

### 删除表范围运算符

也可以删除表范围运算。下面给出的是语法，从emp表中删除“MAX_FILESIZE”。

```
alter 'emp', METHOD => 'table_att_unset', NAME => 'MAX_FILESIZE'
```

### 删除列族

使用alter，也可以删除列族。下面给出的是使用alter删除列族的语法。

```
alter 'tablename', 'delete' => 'column family' 
```

下面给出的是一个例子，从“emp”表中删除列族。

假设在HBase中有一个employee表。

```
scan 'employee'
```

现在使用alter命令删除指定的 professional 列族。

```
alter 'employee','delete'=>'professional'
```

现在验证该表中变更后的数据。观察列族“professional”也没有了，因为前面已经被删除了。

```
scan 'employee'
```

