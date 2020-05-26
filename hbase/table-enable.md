# HBase 启用表(enable)

启用表的语法：

```
enable 'tablename'
```

给出下面是一个例子，使一个表启用。

```
enable 'emp'
```

## 验证

启用表之后，扫描。如果能看到的模式，那么证明表已成功启用。

```
scan 'emp'
```

## is_enabled

此命令用于查找表是否被启用。它的语法如下：

```
is_enabled 'tablename'
```

下面的代码验证表emp是否启用。如果启用，它将返回true，如果没有，它会返回false。

```
is_enabled 'emp'
```