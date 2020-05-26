# Redis 数据结构-列表(list)

Redis列表只是字符串列表，按插入顺序排序。可以在列表的头部或尾部添加Redis列表中的元素。

列表的最大长度为`2^32 - 1`个元素(即`4294967295`，每个列表可存储超过40亿个元素)。

## Redis列表命令

下表列出了与列表相关的一些基本命令。

| 序号 | 命令                                  | 说明                                                         |
| ---- | ------------------------------------- | ------------------------------------------------------------ |
| 1    | BLPOP key1 [key2 \] timeout           | 删除并获取列表中的第一个元素，或阻塞，直到有一个元素可用     |
| 2    | BRPOP key1 [key2 \] timeout           | 删除并获取列表中的最后一个元素，或阻塞，直到有一个元素可用   |
| 3    | BRPOPLPUSH source destination timeout | 从列表中弹出值，将其推送到另一个列表并返回它; 或阻塞，直到一个可用 |
| 4    | LINDEX key index]                     | 通过其索引从列表获取元素                                     |
| 5    | LINSERT key BEFORE/AFTER pivot value  | 在列表中的另一个元素之前或之后插入元素                       |
| 6    | LLEN key                              | 获取列表的长度                                               |
| 7    | LPOP key                              | 删除并获取列表中的第一个元素                                 |
| 8    | LPUSH key value1 [value2\]            | 将一个或多个值添加到列表                                     |
| 9    | LPUSHX key value]                     | 仅当列表存在时，才向列表添加值                               |
| 10   | LRANGE key start stop                 | 从列表中获取一系列元素                                       |
| 11   | LREM key count value                  | 从列表中删除元素                                             |
| 12   | LSET key index value                  | 通过索引在列表中设置元素的值                                 |
| 13   | LTRIM key start stop                  | 修剪列表的指定范围                                           |
| 14   | RPOP key                              | 删除并获取列表中的最后一个元素                               |
| 15   | RPOPLPUSH source destination          | 删除列表中的最后一个元素，将其附加到另一个列表并返回         |
| 16   | RPUSH key value1 [value2\]            | 将一个或多个值附加到列表                                     |
| 17   | RPUSHX key value                      | 仅当列表存在时才将值附加到列表                               |

## 动手试一下

**[环境准备](./setup.html)**

**示例:**

```shell
redis-cli
```
```shell
LPUSH mylist "redis" 
LPUSH mylist "mongodb"
LPUSH mylist "mysql"
LRANGE mylist 0 10
```

在上面的示例中，通过命令`LPUSH`将三个值插入到名称为“`mylist`”的Redis列表中。

