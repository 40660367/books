# HBase 删除数据(delete)

## 从表删除特定单元格

使用 delete 命令，可以在一个表中删除特定单元格。 delete 命令的语法如下：

```
delete '<table name>', '<row>', '<column name >', '<time stamp>'
```

下面是一个删除特定单元格和例子。在这里，我们删除salary

```
delete 'emp', '1', 'personal data:city',
```

## 	删除表的所有单元格

使用“deleteall”命令，可以删除一行中所有单元格。下面给出是 deleteall 命令的语法。

```
deleteall '<table name>', '<row>',
```

这里是使用“deleteall”命令删去 emp 表 row1 的所有单元的一个例子。

```
deleteall 'emp','1'
```

使用scan命令验证表。表被删除后的快照如下。

```
scan 'emp'
```
