# elasticsearch 索引

## 新建Index

新建 Index，可以直接向 Elastic 服务器发出 PUT 请求。下面的例子是新建一个名叫`weather`的 Index。

```bash
curl -X PUT 'localhost:9200/testindex'
```

服务器返回一个 JSON 对象，里面的`acknowledged`字段表示操作成功。

## 查看索引

**查看多索引** 

```bash
curl -XGET 'http://localhost:9200/index1,index2,index3/_search?pretty'
```

**所有索引的_all关键字**

```bash
curl -XGET 'http://localhost:9200/_all/_search?pretty'
```

**查看所有的索引**

```bash
curl -X GET "localhost:9200/_cat/indices?v"
```

## 删除Index

然后，我们发出 DELETE 请求，删除这个 Index。

```bash
curl -X DELETE 'localhost:9200/testindex'
```
