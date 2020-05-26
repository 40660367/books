# Redis 配置(redis.conf)

在Redis中，在Redis的根目录下有一个配置文件(`redis.conf`)。当然您可以通过Redis `CONFIG`命令获取和设置所有的**Redis**配置。

**语法**
以下是Redis中的`CONFIG`命令的基本语法。

```
CONFIG GET CONFIG_SETTING_NAME
```

**示例**

```shell
redis-cli
```
```shell
CONFIG GET loglevel
```

> 要获取所有配置设置，请使用`*`代替`CONFIG_SETTING_NAME`

## 编辑配置

要更新配置，可以直接编辑`redis.conf`文件，也可以通过`CONFIG set`命令更新配置。

**语法**
以下是`CONFIG SET`命令的基本语法。

```
CONFIG SET CONFIG_SETTING_NAME NEW_CONFIG_VALUE
```

**示例**

```shell
redis-cli
```

```shell
CONFIG SET loglevel "notice" 
```

```shell
CONFIG GET loglevel  
```