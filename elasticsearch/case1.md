# elasticsearch 示例1

## 导入示例数据

```bash
cp /share/lesson/elasticsearch/accounts.json .
curl -XPOST 127.0.0.1:9200/bank/account/_bulk?pretty --data-binary @accounts.json
```

https://cloud.tencent.com/developer/article/1612516

**注意：**

1. 需要在accounts.json所在的目录运行curl命令。
2. 127.0.0.1:9200是ES得访问地址和端口
3. bank是索引的名称
4. account是类型的名称
5. 索引和类型的名称在文件中如果有定义，可以省略；如果没有则必须要指定
6. _bulk是rest得命令，可以批量执行多个操作（操作是在json文件中定义的，原理可以参考之前的翻译）
7. pretty是将返回的信息以可读的JSON形式返回。

```bash
#验证
curl 'localhost:9200/_cat/indices?v'
```

## 查询

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match_all": {} }
}'
```

参数可以控制返回的结果：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match_all": {} },
  "size": 1
}'
```

上面的命令返回了所有文档数据中的第一条文档。如果size不指定，那么默认返回10条。

 下面的命令请求了第10-20的文档。

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match_all": {} },
  "from": 10,
  "size": 10
}'
```

下面的命令指定了文档返回的排序方式：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match_all": {} },
  "sort": { "balance": { "order": "desc" } }
}'
```

##  执行搜索

之前的返回数据都是返回文档的所有内容，这种对于网络的开销肯定是有影响的，下面的例子就指定了返回特定的字段：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match_all": {} },
  "_source": ["account_number", "balance"]
}'
```

再回到query，之前的查询都是查询所有的文档，并不能称之为搜索引擎。下面就通过match方式查询特定字段的特定内容，比如查询余额为20的账户信息：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match": { "account_number": 20 } }
}'
```

查询地址为mill的信息：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match": { "address": "mill" } }
}'
```

查询地址为mill或者lane的信息：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match": { "address": "mill lane" } }
}'
```

如果我们想要返回同时包含mill和lane的，可以通过match_phrase查询：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": { "match_phrase": { "address": "mill lane" } }
}'
```

ES提供了bool查询，可以把很多小的查询组成一个更为复杂的查询，比如查询同时包含mill和lane的文档：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

修改bool参数，可以改为查询包含mill或者lane的文档：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": {
    "bool": {
      "should": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

也可以改写为must_not，排除包含mill和lane的文档：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": {
    "bool": {
      "must_not": [
        { "match": { "address": "mill" } },
        { "match": { "address": "lane" } }
      ]
    }
  }
}'
```

bool查询可以同时使用must, should, must_not组成一个复杂的查询：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": {
    "bool": {
      "must": [
        { "match": { "age": "40" } }
      ],
      "must_not": [
        { "match": { "state": "ID" } }
      ]
    }
  }
}'
```

## 过滤查询

之前说过score字段指定了文档的分数，使用查询会计算文档的分数，最后通过分数确定哪些文档更相关，返回哪些文档。

**有的时候我们可能对分数不感兴趣，就可以使用filter进行过滤，它不会去计算分值，因此效率也就更高一些。**

filter过滤可以嵌套在bool查询内部使用，比如想要查询在2000-3000范围内的所有文档，可以执行下面的命令：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "query": {
    "bool": {
      "must": { "match_all": {} },
      "filter": {
        "range": {
          "balance": {
            "gte": 20000,
            "lte": 30000
          }
        }
      }
    }
  }
}'
```

ES除了上面介绍过的范围查询range、match_all、match、bool、filter还有很多其他的查询方式，这里就先不一一说明了。

## 聚合

聚合提供了用户进行分组和数理统计的能力，可以把聚合理解成SQL中的GROUP BY和分组函数。在ES中，你可以在一次搜索查询的时间内，即完成搜索操作也完成聚合操作，这样就降低了多次使用REST API造成的网络开销。

下面就是通过terms聚合的简单样例：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state"
      }
    }
  }
}'
```

它类似于SQL中的下面的语句：

```sql
SELECT state, COUNT(*) FROM bank GROUP BY state ORDER BY COUNT(*) DESC
```

由于size设置为0，它并没有返回文档的信息，只是返回了聚合的结果。

比如统计不同账户状态下的平均余额：

```bash
curl -XPOST 'localhost:9200/bank/_search?pretty' -H 'content-Type:application/json' -d '
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state"
      },
      "aggs": {
        "average_balance": {
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  }
}'
```

聚合支持嵌套，举个例子，先按范围分组，在统计不同性别的账户余额：

```bash
curl -X GET "localhost:9200/bank/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "aggs": {
    "group_by_state": {
      "terms": {
        "field": "state.keyword",
        "order": {
          "average_balance": "desc"
        }
      },
      "aggs": {
        "average_balance": {
          "avg": {
            "field": "balance"
          }
        }
      }
    }
  }
}
'
```

```bash
curl -X GET "localhost:9200/bank/_search?pretty" -H 'Content-Type: application/json' -d'
{
  "size": 0,
  "aggs": {
    "group_by_age": {
      "range": {
        "field": "age",
        "ranges": [
          {
            "from": 20,
            "to": 30
          },
          {
            "from": 30,
            "to": 40
          },
          {
            "from": 40,
            "to": 50
          }
        ]
      },
      "aggs": {
        "group_by_gender": {
          "terms": {
            "field": "gender.keyword"
          },
          "aggs": {
            "average_balance": {
              "avg": {
                "field": "balance"
              }
            }
          }
        }
      }
    }
  }
}
'
```

聚合可以实现很多复杂的功能，而且ES也提供了很多复杂的聚合