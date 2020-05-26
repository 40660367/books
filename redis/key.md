# Redis 数据结构-键(key)		

Redis键命令用于管理**Redis**中的键。以下是使用redis键命令的语法。

**语法**
```
COMMAND KEY_NAME
```

## Redis键命令

下表列出了与键相关的一些基本命令。

| 编号 | 命令                                                         | 描述                                                         |
| ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| 1    | DEL key         | 此命令删除一个指定键(如果存在)。                             |
| 2    | DUMP key      | 此命令返回存储在指定键的值的序列化版本。                     |
| 3    | EXISTS key  | 此命令检查键是否存在。                                       |
| 4    | EXPIRE key seconds | 设置键在指定时间秒数之后到期/过期。                          |
| 5    | EXPIREAT key timestamp | 设置在指定时间戳之后键到期/过期。这里的时间是Unix时间戳格式。 |
| 6    | PEXPIRE key milliseconds | 设置键的到期时间(以毫秒为单位)。                             |
| 7    | PEXPIREAT key milliseconds-timestamp | 以Unix时间戳形式来设置键的到期时间(以毫秒为单位)。           |
| 8    | KEYS pattern   | 查找与指定模式匹配的所有键。                                 |
| 9    | MOVE key db    | 将键移动到另一个数据库。                                     |
| 10   | PERSIST key | 删除指定键的过期时间，得永生。                               |
| 11   | PTTL key       | 获取键的剩余到期时间。                                       |
| 12   | RANDOMKEY | 从Redis返回一个随机的键。                                    |
| 13   | RENAME key newkey | 更改键的名称。                                               |
| 14   | PTTL key       | 获取键到期的剩余时间(以毫秒为单位)。                         |
| 15   | RENAMENX key newkey | 如果新键不存在，重命名键。                                   |
| 16   | TYPE key       | 返回存储在键中的值的数据类型。                               |

## 动手试一下

**[环境准备](./setup.html)**

**示例:**

```bash
SET akey redis
```

```bash
DEL akey
```

```bash
GET akey
```

在上面的例子中，`DEL`是Redis的命令，而`akey`是键的名称。如果键被删除，则命令的输出将为`(integer) 1`，否则为`(integer) 0`。