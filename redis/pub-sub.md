# Redis 发送订阅(pub sub)

Redis发布订阅(pub/sub)是一种消息通信模式：发送者(pub)发送消息，订阅者(sub)接收消息。
Redis 发布订阅(pub/sub)实现了消息系统，发送者(在redis术语中称为发布者)在接收者(订阅者)接收消息时发送消息。传送消息的链路称为信道。

在Redis中，客户端可以订阅任意数量的信道。

## Redis发布订阅命令

下表列出了与Redis发布订阅相关的一些基本命令。

| 序号 | 命令                                      | 说明                               |
| ---- | ----------------------------------------- | ---------------------------------- |
| 1    | PSUBSCRIBE pattern [pattern …\]           | 订阅一个或多个符合给定模式的频道。 |
| 2    | PUBSUB subcommand [argument [argument …\] | 查看订阅与发布系统状态。           |
| 3    | PUBLISH channel message                   | 将信息发送到指定的频道。           |
| 4    | PUNSUBSCRIBE [pattern [pattern …\]        | 退订所有给定模式的频道。           |
| 5    | SUBSCRIBE channel [channel …\]            | 订阅给定的一个或多个频道的信息。   |
| 6    | UNSUBSCRIBE [channel [channel …\]         | 退订给定的频道。                   |

## 动手试一下

**[环境准备](./setup.html)**

以下示例说明了发布用户概念的工作原理。 在以下示例中，一个客户端订阅名为“`redisChat`”的信道。

```bash
SUBSCRIBE redisChat  
```

现在，两个客户端在名称为“`redisChat`”的相同信道上发布消息，并且上述订阅的客户端接收消息。

```bash
PUBLISH redisChat "Redis is a great caching technique"  
```

```bash
PUBLISH redisChat "Learn redis"  
```
