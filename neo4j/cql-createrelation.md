# Neo4j CQL建立关系

在Noe4j中，关系是一个元素，通过它我们可以连接图的两个节点。这些关系具有方向，类型和数据的形式模式。本章教你如何-

- 建立关系
- 在现有节点之间创建关系
- 使用标签和属性创建关系

## 建立关系

我们可以使用CREATE子句创建关系。我们将根据括号中的连字符“-”和箭头“→”之间的关系的方向在方括号“ []”中指定关系，如以下语法所示。

### 句法

以下是使用CREATE子句创建关系的语法。

```
CREATE (node1)-[:RelationshipType]->(node2) 
```

### 例

首先，在数据库中创建两个节点Ind和Dhawan，如下所示。

```
CREATE (Dhawan:player{name: "Shikar Dhawan", YOB: 1985, POB: "Delhi"}) 
CREATE (Ind:Country {name: "India"})
```

现在，在这两个节点之间创建一个名为**BATSMAN_OF**的关系，如下所示：

```
CREATE (Dhawan)-[r:BATSMAN_OF]->(Ind) 
```

最后，返回两个节点以查看创建的关系。

```
RETURN Dhawan, Ind 
```

将所需查询复制并粘贴到美元提示中，然后按以下屏幕截图中突出显示的播放按钮（以执行查询）。

## 在现有节点之间创建关系

您还可以使用**MATCH**子句在现有节点之间创建关系。

### 句法

以下是使用MATCH子句创建关系的语法。

```cql
MATCH (a:LabeofNode1), (b:LabeofNode2) 
   WHERE a.name = "nameofnode1" AND b.name = " nameofnode2" 
CREATE (a)-[: Relation]->(b) 
RETURN a,b 
```

### 例

以下是一个示例Cypher查询，它使用match子句创建关系。

```cql
MATCH (a:player), (b:Country) WHERE a.name = "Shikar Dhawan" AND b.name = "India" 
CREATE (a)-[r: BATSMAN_OF]->(b) 
RETURN a,b 
```

## 使用标签和属性创建关系

您可以使用CREATE子句来创建带有标签和属性的关系。

### 句法

以下是使用CREATE子句与标签和属性建立关系的语法。

```cql
CREATE (node1)-[label:Rel_Type {key1:value1, key2:value2, . . . n}]-> (node2) 
```

### 例

以下是一个示例Cypher查询，它创建了带有标签和属性的关系。

```cql
MATCH (a:player), (b:Country) WHERE a.name = "Shikar Dhawan" AND b.name = "India" 
CREATE (a)-[r:BATSMAN_OF {Matches:5, Avg:90.75}]->(b)  
RETURN a,b 
```

## 创建完整路径

在Neo4j中，使用连续关系形成路径。可以使用create子句创建路径。

### 句法

以下是使用CREATE子句在Neo4j中创建路径的语法。

```cql
CREATE p = (Node1 {properties})-[:Relationship_Type]->
   (Node2 {properties})[:Relationship_Type]->(Node3 {properties}) 
RETURN p 
```
