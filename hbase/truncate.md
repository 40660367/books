# HBase 计数和截断

## count

可以使用count命令计算表的行数量。

**它的语法如下：**

```
count '<table name>'
```

删除第一行后，表emp就只有两行。验证它，如下图所示。

```
count 'emp'
```

## truncate

此命令将禁止删除并重新创建一个表。

**truncate 的语法如下：**

```
truncate 'table name'
```

下面给出是 truncate 命令的例子。在这里，我们已经截断了emp表。

```
truncate 'emp'
```

截断表之后，使用scan 命令来验证。会得到表的行数为零。

```
scan 'emp'
```