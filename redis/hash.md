# Redis 数据结构-哈希(hash)

Redis Hashes是字符串字段和字符串值之间的映射(类似于PHP中的数组类型)。 因此，它们是表示对象的完美数据类型。

在Redis中，每个哈希(散列)可以存储多达4亿个键-值对。

## Redis哈希命令

下表列出了与哈希/散列相关的一些基本命令。

| 序号 | 命令                                      | 说明                                   |
| ---- | ----------------------------------------- | -------------------------------------- |
| 1    | HDEL key field2 [field2\]                 | 删除一个或多个哈希字段。               |
| 2    | HEXISTS key field                         | 判断是否存在散列字段。                 |
| 3    | HGET key field                            | 获取存储在指定键的哈希字段的值。       |
| 4    | HGETALL key                               | 获取存储在指定键的哈希中的所有字段和值 |
| 5    | HINCRBY key field increment               | 将哈希字段的整数值按给定数字增加       |
| 6    | HINCRBYFLOAT key field increment          | 将哈希字段的浮点值按给定数值增加       |
| 7    | HKEYS key                                 | 获取哈希中的所有字段                   |
| 8    | HLEN key                                  | 获取散列中的字段数量                   |
| 9    | HMGET key field1 [field2\]                | 获取所有给定哈希字段的值               |
| 10   | HMSET key field1 value1 [field2 value2 \] | 为多个哈希字段分别设置它们的值         |
| 11   | HSET key field value                      | 设置散列字段的字符串值                 |
| 12   | HSETNX key field value                    | 仅当字段不存在时，才设置散列字段的值   |
| 13   | HVALS key                                 |                                        |

## 动手试一下

**[环境准备](./setup.html)**

```bash
HMSET myhash name "redis tutorial" 
HMSET myhash like 100 
HMSET myhash author 'redis' 
```
```bash
HGETALL myhash
```

在上面的例子中，在名称为’`myhash`‘的哈希中设置了Redis教程的详细信息(名称，喜欢，访问者)。
