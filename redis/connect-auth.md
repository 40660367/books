# Redis管理连接

Redis中的连接命令基本上是用于管理与Redis服务器的客户端连接。

## Redis 设置pass验证		

Redis数据库可以使用安全的方案，使得进行连接的任何客户端在执行命令之前都需要进行身份验证。

要保护Redis安全，需要在配置文件中设置密码。

## 动手试一下

**[环境准备](./setup.html)**

下面的示例显示了设置Redis实例pass的步骤。

查看密码配置
```shell
CONFIG get requirepass 
```
默认情况下此属性为空，这表示还没有为此实例设置密码。您可以通过执行以下命令更改此属性。如下所示
```
1) "requirepass"
2) ""
```

进行密码配置
```shell
CONFIG set requirepass "pwd-store-in-server" 
```

```shell
CONFIG get requirepass 
```
设置密码后，如果任何客户端运行命令而不进行身份验证，则会返回一个**(error) NOAUTH Authentication required.**的错误信息。 因此，客户端需要使用AUTH命令来验证。

## AUTH命令语法

以下是AUTH命令的基本语法。
```
AUTH YourNewPassword
```

## Redis连接命令

下表列出了与Redis连接相关的一些基本命令。

| 序号 | 命令          | 说明                     |
| ---- | ------------- | ------------------------ |
| 1    | AUTH password | 使用给定的密码验证服务器 |
| 2    | ECHO message  | 打印给定的字符串信息     |
| 3    | PING          | 检查服务器是否正在运行   |
| 4    | QUIT          | 关闭当前连接             |
| 5    | SELECT index  | 更改当前连接的所选数据库 |

## 动手试一下

**[环境准备](./setup.html)**

下边语句会报错，因为redis-server需要pass

```shell
CONFIG get requirepass 
```

#进行验证后，操作可正常进行。
```shell
AUTH "pwd-store-in-server" 
```
```shell
CONFIG get requirepass 
```

```shell
SET mykey "Test value" 
GET mykey 
```
