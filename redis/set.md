# Redis 数据结构-集合(set)

Redis集合是唯一字符串的无序集合。 唯一值表示集合中不允许键中有重复的数据。

在Redis中设置添加，删除和测试成员的存在(恒定时间O(1)，而不考虑集合中包含的元素数量)。列表的最大长度为`2^32 - 1`个元素(即4294967295，每组集合超过40亿个元素)。

## Redis集合命令

下表列出了与集合相关的一些基本命令。

| 序号 | 命令                                            | 说明                             |
| ---- | ----------------------------------------------- | -------------------------------- |
| 1    | SADD key member1 [member2\]                     | 将一个或多个成员添加到集合       |
| 2    | SCARD key                                       | 获取集合中的成员数               |
| 3    | SDIFF key1 [key2\]                              | 减去多个集合                     |
| 4    | SDIFFSTORE destination key1 [key2\]             | 减去多个集并将结果集存储在键中   |
| 5    | SINTER key1 [key2\]                             | 相交多个集合                     |
| 6    | SINTERSTORE destination key1 [key2\]            | 交叉多个集合并将结果集存储在键中 |
| 7    | SISMEMBER key member                            | 判断确定给定值是否是集合的成员   |
| 8    | SMOVE source destination member                 | 将成员从一个集合移动到另一个集合 |
| 9    | SPOP key                                        | 从集合中删除并返回随机成员       |
| 10   | SRANDMEMBER key [count\]                        | 从集合中获取一个或多个随机成员   |
| 11   | SREM key member1 [member2\]                     | 从集合中删除一个或多个成员       |
| 12   | SUNION key1 [key2\]                             | 添加多个集合                     |
| 13   | SUNIONSTORE destination key1 [key2\]            | 添加多个集并将结果集存储在键中   |
| 14   | SSCAN key cursor [MATCH pattern\] [COUNT count] | 递增地迭代集合中的元素           |

## 动手试一下

**[环境准备](./setup.html)**

**示例**

```shell
SADD myset "redis" 
SADD myset "mongodb" 
SADD myset "mysql" 
SADD myset "mysql"
```

```shell
SMEMBERS "myset"  
```

在上面的示例中，通过命令`SADD`将三个值插入到名称为“`myset`”的Redis集合中。
