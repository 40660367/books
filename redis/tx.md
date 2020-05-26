# Redis 事务(transaction)

Redis事务允许在单个步骤中执行一组命令。以下是事务的两个属性：

- 事务中的所有命令作为单个隔离操作并按顺序执行。不可以在执行Redis事务的中间向另一个客户端发出的请求。
- Redis事务也是原子的。原子意味着要么处理所有命令，要么都不处理。

## 语法示例

Redis事务由命令`MULTI`命令启动，然后需要传递一个应该在事务中执行的命令列表，然后整个事务由`EXEC`命令执行。

```
MULTI 
List of commands here 
EXEC
```

## Redis事务命令

下表列出了与Redis事务相关的一些基本命令。

| 序号 | 命令               | 说明                                   |
| ---- | ------------------ | -------------------------------------- |
| 1    | DISCARD            | 丢弃在MULTI之后发出的所有命令          |
| 2    | EXEC               | 执行MULTI后发出的所有命令              |
| 3    | MULTI              | 标记事务块的开始                       |
| 4    | UNWATCH            | 取消 WATCH 命令对所有 key 的监视。     |
| 5    | WATCH key [key …\] | 监视给定的键以确定MULTI / EXEC块的执行 |

## 动手试一下

**[环境准备](./setup.html)**

**示例**

以下示例说明了如何启动和执行Redis事务。

```shell
MULTI 
SET mykey "redis" 
GET mykey 
INCR visitors 
EXEC  
```
