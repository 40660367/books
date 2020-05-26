# Neo4j foreach子句

所述**FOREACH**子句用于更新数据的列表中是否聚集的结果的路径的部件，或。

## 句法

以下是FOREACH子句的语法。

```cql
MATCH p = (start node)-[*]->(end node) 
WHERE start.node = "node_name" AND end.node = "node_name" 
FOREACH (n IN nodes(p)| SET n.marked = TRUE) 
```

## 例

在继续该示例之前，如下所示在Neo4j数据库中创建路径**p**。

```cql
CREATE p = (Dhawan {name:"Shikar Dhawan"})-[:TOPSCORRER_OF]->(Ind{name: 
   "India"})-[:WINNER_OF]->(CT2013{name: "Champions Trophy 2013"}) 
RETURN p 
```

以下是一个示例密码查询，该查询使用FOREACH子句向沿路径的所有节点添加属性。

```cql
MATCH p = (Dhawan)-[*]->(CT2013) 
   WHERE Dhawan.name = "Shikar Dhawan" AND CT2013.name = "Champions Trophy 2013" 
FOREACH (n IN nodes(p)| SET n.marked = TRUE)
```

## 验证

要验证节点的创建，请在Dollar提示符下键入并执行以下查询。

```cql
MATCH (n) RETURN n 
```

该查询返回数据库中的所有节点（我们将在接下来的章节中详细讨论该查询）。