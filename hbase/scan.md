# HBase 检索数据(scan)

**scan** 命令用于查看HTable数据。使用 **scan** 命令可以得到表中的数据。

**它的语法如下：**

```
scan '<table name>'
```

下面的示例演示了如何使用scan命令从表中读取数据。在这里读取的是emp表。

```hbase
scan 'emp'
```