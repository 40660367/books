# Neo4j with链接子句

您可以使用WITH子句将查询艺术链接在一起。

## 句法

以下是WITH子句的语法。

```cql
MATCH (n) 
WITH n 
ORDER BY n.property 
RETURN collect(n.property) 
```

## 例

以下是一个示例Cypher查询，演示了WITH子句的用法。

```cql
MATCH (n) 
WITH n 
ORDER BY n.name DESC LIMIT 3 
RETURN collect(n.name) 
```

