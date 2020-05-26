# Neo4j merge合并子句

MERGE命令是CREATE命令和MATCH命令的组合。

Neo4j CQL MERGE命令在图形中搜索给定的模式。如果存在，则返回结果。

如果图中不存在它，那么它将创建一个新的节点/关系并返回结果。

在本章中，您将学习如何-

- 合并带有标签的节点
- 合并具有属性的节点
- OnCreate和OnMatch
- 合并关系

### 句法

以下是MERGE命令的语法。

```cql
MERGE (node: label {properties . . . . . . . }) 
```

在继续本节中的示例之前，请在数据库中创建两个标签为Dhawan和Ind的节点，然后从Dhawan到Ind创建类型为“ BATSMAN_OF”的关系，如下所示。

```cql
CREATE (Dhawan:player{name: "Shikar Dhawan", YOB: 1985, POB: "Delhi"}) 
CREATE (Ind:Country {name: "India"}) 
CREATE (Dhawan)-[r:BATSMAN_OF]->(Ind) 
```

## 合并带有标签的节点

您可以使用MERGE子句根据标签合并数据库中的节点。如果尝试基于标签合并节点，则Neo4j会验证是否存在带有给定标签的节点。否则，将创建当前节点。

### 句法

以下是基于标签合并节点的语法。

```cql
MERGE (node:label) RETURN node 
```

### 例子1

以下是一个示例Cypher Query，它将一个节点合并到Neo4j中（基于标签）。当您执行此查询时，Neo4j会验证是否存在带有标签**播放器的**节点。如果没有，它将创建一个名为“ Jadeja”的节点并返回它。

如果存在带有给定标签的任何节点，则Neo4j将它们全部返回。

```cql
MERGE (Jadeja:player) RETURN Jadeja 
```

### 例子2

现在，尝试将名为“ CT2013”的节点与名为Tournament的标签合并。由于没有带有该标签的节点，Neo4j将使用给定名称创建一个节点并将其返回。

```cql
MERGE (CT2013:Tournament{name: "ICC Champions Trophy 2013"}) 
RETURN CT2013, labels(CT2013)
```

## 合并具有属性的节点

您还可以合并具有一组属性的节点。如果这样做，Neo4j将为指定节点（包括属性）搜索相等的匹配项。如果找不到，它将创建一个。

### 句法

以下是使用属性合并节点的语法。

```
MERGE (node:label {key1:value, key2:value, key3:value . . . . . . . . }) cql
```

### 例

以下是使用属性合并节点的示例Cypher查询。该查询尝试使用属性和标签合并名为“ jadeja”的节点。由于没有这样的具有确切标签和属性的节点，Neo4j将创建一个节点。

```cql
MERGE (Jadeja:player {name: "Ravindra Jadeja", YOB: 1988, POB: "NavagamGhed"}) 
RETURN Jadeja 
```

## OnCreate和OnMatch

每当我们执行合并查询时，就会匹配或创建一个节点。使用在创建时和在匹配时，可以设置属性以指示节点是创建还是匹配。

### 句法

以下是**OnCreate**和**OnMatch**子句的语法。

```cql
MERGE (node:label {properties . . . . . . . . . . .}) 
ON CREATE SET property.isCreated ="true" 
ON MATCH SET property.isFound ="true"
```

### 例

以下是一个示例Cypher Query，它演示了Neo4j 中**OnCreate**和**OnMatch**子句的用法。如果指定的节点已存在于数据库中，则将匹配该节点，并在该节点中创建键值对isFound =“ true”的属性。

如果指定的节点在数据库中不存在，则将创建该节点，并在其中创建具有键值对isCreated =“ true”的属性。

```cql
MERGE (Jadeja:player {name: "Ravindra Jadeja", YOB: 1988, POB: "NavagamGhed"}) 
ON CREATE SET Jadeja.isCreated = "true" 
ON MATCH SET Jadeja.isFound = "true" 
RETURN Jadeja 
```

## 合并关系

就像节点一样，您也可以使用MERGE子句合并关系。

### 例

以下是一个示例密码查询，该查询使用Neo4j中的MATCH子句合并关系。此查询尝试在节点“ ind”（标签：国家和名称：印度）和ICC13（标签：锦标赛和名称：ICC Champions Trophy 2013）之间合并名为**WINNERS_OF**的关系。

由于这种关系不存在，因此Neo4j创建一个。

```cql
MATCH (a:Country), (b:Tournament) 
   WHERE a.name = "India" AND b.name = "ICC Champions Trophy 2013" 
   MERGE (a)-[r:WINNERS_OF]->(b) 
RETURN a, b 
```

同样，您也可以合并多个关系和无向关系。