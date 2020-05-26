# elasticsearch 查询语言DSL

ES支持一种JSON格式的查询，叫做DSL，**D**omain **S**pecific **L**anguage。

ES提供了两种搜索的方式：**请求参数方式** 和 **请求体方式**。

**请求参数方式**

```
curl 'localhost:9200/bank/_search?q=*&pretty'
```

其中bank是查询的索引名称，q后面跟着搜索的条件：q=*表示查询所有的内容

**请求体方式（推荐这种方式）**

```
curl -XPOST 'localhost:9200/bank/_search?pretty' -d '
{
  "query": { "match_all": {} }
}'
```

query定义了查询，match_all声明了查询的类型，指定可以搜索全部的文档：

这种方式会把查询的内容放入body中，会造成一定的开销，但是易于理解。

**返回的内容解读如下：**

took：是查询花费的时间，毫秒单位

time_out：标识查询是否超时

_shards：描述了查询分片的信息，查询了多少个分片、成功的分片数量、失败的分片数量等

hits：搜索的结果，total是全部的满足的文档数目，hits是返回的实际数目（默认是10）

_score是文档的分数信息，与排名相关度有关，参考各大搜索引擎的搜索结果，就容易理解。 

由于ES是一次性返回所有的数据，因此理解返回的内容是很必要的。