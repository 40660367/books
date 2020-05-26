# Neo4j 计数功能count

假设我们在数据库中创建了一个带有以下详细信息的图形。

## 计数

的**count()**函数是用来计数行数。

### 句法

以下是count函数的语法。

```cql
MATCH (n { name: 'A' })-->(x) 
RETURN n, count(*) 
```

### 例

以下是一个示例Cypher Query，它演示了**count（）**函数的用法。

```cql
Match(n{name: "India", result: "Winners"})--(x)  
RETURN n, count(*) 
```

## 组数

该**COUNT**子句也可用于计算的关系类型的群体。

### 例

以下是一个示例Cypher查询，该查询计算并返回参与每个关系的节点数。

```cql
Match(n{name: "India", result: "Winners"})-[r]-(x)  
RETURN type (r), count(*) 
```
