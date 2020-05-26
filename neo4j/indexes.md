# Neo4j Index索引

Neo4j SQL支持节点或关系属性上的索引，以提高应用程序的性能。我们可以为所有具有相同标签名称的节点的属性创建索引。

我们可以在MATCH或WHERE或IN运算符上使用这些索引列来改善CQL命令的执行。

在本章中，我们将讨论如何-

- 创建一个索引
- 删除索引

## 创建索引

Neo4j CQL提供“ CREATE INDEX”命令来在Node或Relationship属性上创建索引。

### 句法

以下是在Neo4j中创建索引的语法。

```cql
CREATE INDEX ON:label (node) 
```

### 例

在继续该示例之前，如下所示创建一个节点Dhawan。

```cql
CREATE (Dhawan:player{name: "shikar Dhawan", YOB: 1995, POB: "Delhi"})
```

以下是一个示例密码查询，用于在Neo4j中的节点Dhawan上创建索引。

```cql
CREATE INDEX ON:player(Dhawan) 
```

## 删除索引

Neo4j CQL提供“ DROP INDEX”命令来删除Node或Relationshis属性的现有索引。

### 句法

以下是在Neo4j中创建索引的语法。

```cql
DROP INDEX ON:label(node) 
```

### 例

以下是示例Cypher查询，用于在Neo4j中名为“ Dhawan”的节点上创建索引。

```cql
DROP INDEX ON:player(Dhawan) 
```
