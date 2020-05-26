# elasticsearch 数据查询

## 准备数据

```bash
curl -X PUT 'localhost:9200/querycourse/person/1' -H 'content-Type:application/json' -d '
{
    "user" : "joe",
    "title" : "artist"
}' 

curl -X PUT 'localhost:9200/querycourse/person/2' -H 'content-Type:application/json' -d '
{
    "user" : "steve",
    "title" : "ceo",
    "inc" : "apple"
}' 
curl -X PUT 'localhost:9200/querycourse/person/3' -H 'content-Type:application/json' -d '
{
    "user" : "nancy",
    "title" : "engineer"
}' 
curl -X PUT 'localhost:9200/querycourse/person/4' -H 'content-Type:application/json' -d '
{
    "user" : "lily",
    "title" : "ceo"
}' 
curl -X PUT 'localhost:9200/querycourse/person/5' -H 'content-Type:application/json' -d '
{
    "user" : "jacob",
    "title" : "engineer"
}' 
```

###  返回所有记录

使用 GET 方法，直接请求`/Index/Type/_search`，就会返回所有记录。

```bash
curl 'localhost:9200/querycourse/person/_search?pretty'
```

上面代码中，返回结果的 `took`字段表示该操作的耗时（单位为毫秒），`timed_out`字段表示是否超时，`hits`字段表示命中的记录，里面子字段的含义如下。

> - `total`：返回记录数，本例是2条。
> - `max_score`：最高的匹配程度，本例是`1.0`。
> - `hits`：返回的记录组成的数组。

返回的记录中，每条记录都有一个`_score`字段，表示匹配的程序，默认是按照这个字段降序排列。

### 全文搜索

Elastic 的查询非常特别，使用自己的[查询语法](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/query-dsl.html)，要求 GET 请求带有数据体。

```bash
curl 'localhost:9200/querycourse/person/_search?pretty' -H 'content-Type:application/json' -d '{
"query" : { "match" : { "title" : "engineer" }}
}'
```

上面代码使用 [Match 查询](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/query-dsl-match-query.html)，指定的匹配条件是`desc`字段里面包含"系统管理"这个词。返回结果如下。

Elastic 默认一次返回10条结果，可以通过`size`字段改变这个设置。

```bash
curl 'localhost:9200/querycourse/person/_search?pretty' -H 'content-Type:application/json' -d '
{
"query" : { "match" : { "title" : "artist" }},
"size": 1
}'
```

上面代码指定，每次只返回一条结果。

还可以通过`from`字段，指定位移。

```bash
curl 'localhost:9200/querycourse/person/_search?pretty' -H 'content-Type:application/json' -d '{
"query" : { "match" : { "title" : "artist" }},
"from": 1,
"size": 1
}'
```

上面代码指定，从位置1开始（默认是从位置0开始），只返回一条结果。

### 逻辑运算

如果有多个搜索关键字， Elastic 认为它们是`or`关系。

```bash
curl 'localhost:9200/querycourse/person/_search?pretty'  -H 'content-Type:application/json' -d '{
"query" : { "match" : { "title" : "artist ceo" }}
}'
```

上面代码搜索的是`garden` `or` `engineer`。

如果要执行多个关键词的`and`搜索，必须使用[布尔查询](https://www.elastic.co/guide/en/elasticsearch/reference/5.5/query-dsl-bool-query.html)。

```bash
curl 'localhost:9200/querycourse/person/_search?pretty' -H 'content-Type:application/json' -d '
{
"query": {
 "bool": {
   "must": [
     { "match": { "title": "ceo" } },
     { "match": { "inc": "apple" } }
   ]
 }
}
}'
```