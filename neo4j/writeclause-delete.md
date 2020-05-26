# Neo4j delete删除子句

您可以使用DELETE子句从数据库中删除节点和关系。

## 删除所有节点和关系

以下是使用DELETE子句删除数据库中所有节点和关系的查询。

### 询问

```cql
MATCH (n) DETACH DELETE n
```

要执行上述查询，请执行以下步骤-

## 删除特定节点

要删除特定节点，需要在上述查询中的“ n”处指定该节点的详细信息。

### 句法

以下是使用DELETE子句从Neo4j删除特定节点的语法。

```cql
MATCH (node:label {properties . . . . . . . . . .  }) 
DETACH DELETE node
```

### 例

在继续该示例之前，如下所示在Neo4j数据库中创建一个节点“ Ishant”。

```cql
CREATE (Ishant:player {name: "Ishant Sharma", YOB: 1988, POB: "Delhi"}) 
```

以下是一个示例密码查询，该查询使用DELETE子句删除上面创建的节点。

```cql
MATCH (Ishant:player {name: "Ishant Sharma", YOB: 1988, POB: "Delhi"}) 
DETACH DELETE Ishant
```
