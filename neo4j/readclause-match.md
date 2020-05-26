# Neo4j match匹配子句

在本章中，我们将学习匹配子句以及可以使用此子句执行的所有功能。

## 使用匹配获取所有节点

使用Neo4j的MATCH子句，您可以检索Neo4j数据库中的所有节点。

### 例

在继续该示例之前，如下所示创建3个节点和2个关系。

```cql
CREATE (Dhoni:player {name: "MahendraSingh Dhoni", YOB: 1981, POB: "Ranchi"}) 
CREATE (Ind:Country {name: "India", result: "Winners"}) 
CREATE (CT2013:Tornament {name: "ICC Champions Trophy 2013"}) 
CREATE (Ind)-[r1:WINNERS_OF {NRR:0.938 ,pts:6}]->(CT2013) 

CREATE(Dhoni)-[r2:CAPTAIN_OF]->(Ind)  
CREATE (Dhawan:player{name: "shikar Dhawan", YOB: 1995, POB: "Delhi"}) 
CREATE (Jadeja:player {name: "Ravindra Jadeja", YOB: 1988, POB: "NavagamGhed"})  

CREATE (Dhawan)-[:TOP_SCORER_OF {Runs:363}]->(Ind) 
CREATE (Jadeja)-[:HIGHEST_WICKET_TAKER_OF {Wickets:12}]->(Ind) 
```

以下是返回Neo4j数据库中所有节点的查询。

```cql
MATCH (n) RETURN n 
```

## 在特定标签下获取所有节点

使用match子句，可以获得特定标签下的所有节点。

### 句法

以下是获取特定标签下所有节点的语法。

```cql
MATCH (node:label) 
RETURN node 
```

### 例

以下是一个示例Cypher Query，它返回标签**player**下的数据库中的所有节点。

```cql
MATCH (n:player) 
RETURN n 
```

## 按关系匹配

您可以使用MATCH子句根据关系检索节点。

### 句法

以下是使用MATCH子句根据关系检索节点的语法。

```cql
MATCH (node:label)<-[: Relationship]-(n) 
RETURN n 
```

### 例

以下是一个示例Cypher Query，用于使用MATCH子句根据关系检索节点。

```cql
MATCH (Ind:Country {name: "India", result: "Winners"})<-[: TOP_SCORER_OF]-(n) 
RETURN n.name 
```

## 删除所有节点

您可以使用MATCH子句删除所有节点。

### 询问

以下是删除Neo4j中所有节点的查询。

```cql
MATCH (n) detach delete n 
```

# Neo4j OptionalMatch可选匹配子句

所述**可选匹配**子句用于搜索中所述的图案，同时使用空值缺失的图案的零件。

OPTIONAL MATCH与match子句相似，唯一的区别是由于缺少模式部分，它返回null。

## 句法

以下是具有关系的可选匹配的语法。

```cql
MATCH (node:label {properties. . . . . . . . . . . . . .}) 
OPTIONAL MATCH (node)-->(x) 
RETURN x
```

## 例

以下是一个样本密码查询，它试图从节点ICCT2013中检索关系。由于没有这样的节点，因此它返回null。

```cql
MATCH (a:Tornament {name: "ICC Champions Trophy 2013"}) 
OPTIONAL MATCH (a)-->(x) 
RETURN x 
```
