# HBase 读取数据

get命令和HTable类的get()方法用于从HBase表中读取数据。使用 get 命令，可以同时获取一行数据。它的语法如下：

```
get '<table name>','row1'
```

下面的例子说明如何使用get命令。扫描emp表的第一行。

```
get 'emp', '1'
```

## 	读取指定列

下面给出的是语法，使用get方法读取指定列。

```
get 'table name', ‘rowid’, {COLUMN => ‘column family:column name ’}
```

下面给出的示例，是用于读取HBase表中的特定列。

```
get 'emp', 'row1', {COLUMN=>'personal:name'}
```
