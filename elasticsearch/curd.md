# elasticsearch 数据操作

### 新增记录

向指定的 /Index/Type 发送 PUT 请求，就可以在 Index 里面新增一条记录。比如，向`/accounts/person`发送请求，就可以新增一条人员记录。

```bash
curl -X PUT 'localhost:9200/accounts/person/1' -H 'content-Type:application/json' -d '
{
    "user" : "joe",
    "title" : "engineer"
}' 

curl -X PUT 'localhost:9200/accounts/person/2' -H 'content-Type:application/json' -d '
{
    "user" : "steve",
    "title" : "ceo"
}' 
```

服务器返回的 JSON 对象，会给出 Index、Type、Id、Version 等信息。

如果你仔细看，会发现请求路径是`/accounts/person/1`，最后的`1`是该条记录的 Id。它不一定是数字，任意字符串（比如`abc`）都可以。

新增记录的时候，也可以不指定 Id，这时要改成 POST 请求。

```bash
curl -X POST 'localhost:9200/accounts/person?pretty' -H 'content-Type:application/json' -d '
{
    "user": "john",
    "title": "artist"
}'
```

上面代码中，向`/accounts/person`发出一个 POST 请求，添加一个记录。

这时，服务器返回的 JSON 对象里面，`_id`字段就是一个随机字符串。

注意，如果没有先创建 Index（这个例子是`accounts`），直接执行上面的命令，Elastic 也不会报错，而是直接生成指定的 Index。所以，打字的时候要小心，不要写错 Index 的名称。

### 查看记录

向`/Index/Type/Id`发出 GET 请求，就可以查看这条记录。

```bash
curl 'localhost:9200/accounts/person/1?pretty' 
```

上面代码请求查看`/accounts/person/1`这条记录，URL 的参数`pretty=true`表示以易读的格式返回。

返回的数据中，`found`字段表示查询成功，`_source`字段返回原始记录。

如果 Id 不正确，就查不到数据，`found`字段就是`false`。

### 更新记录

更新记录就是使用 PUT 请求，重新发送一次数据。

```bash
curl -X PUT 'localhost:9200/accounts/person/1?pretty' -H 'content-Type:application/json' -d '
{
 "user" : "joe",
 "title" : "gardener"
}' 
```

可以看到，记录的 Id 没变，但是版本（version）从`1`变成`2`，操作类型（result）从`created`变成`updated`，`created`字段变成`false`，因为这次不是新建记录。

### 删除记录

删除记录就是发出 DELETE 请求。

```bash
curl -X DELETE 'localhost:9200/accounts/person/1' 
```
