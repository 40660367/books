# Neo4j remove清除子句

REMOVE子句用于从图形元素（节点或关系）中删除属性和标签。

Neo4j CQL DELETE和REMOVE命令之间的主要区别是-

- DELETE操作用于删除节点和关联的关系。
- 删除操作用于删除标签和属性。

## 删除属性

您可以使用MATCH和REMOVE子句删除节点的属性。

### 句法

以下是使用REMOVE子句删除节点属性的语法。

```cql
MATCH (node:label{properties . . . . . . . }) 
REMOVE node.property 
RETURN node 
```

### 例

在继续该示例之前，如下所示创建一个名为**Dhoni**的节点。

```cql
CREATE (Dhoni:player {name: "MahendraSingh Dhoni", YOB: 1981, POB: "Ranchi"})
```

以下是一个示例Cypher Query，它使用REMOVE子句删除了上面创建的节点。

```cql
MATCH (Dhoni:player {name: "MahendraSingh Dhoni", YOB: 1981, POB: "Ranchi"}) 
REMOVE Dhoni.POB 
RETURN Dhoni 
```

## 从节点删除标签

与属性类似，您也可以使用remove子句从现有节点中删除标签。

### 句法

以下是从节点删除标签的语法。

```cql
MATCH (node:label {properties . . . . . . . . . . . }) 
REMOVE node:label 
RETURN node 
```

### 例

以下是一个示例Cypher查询，用于使用remove子句从现有节点中删除标签。

```cql
MATCH (Dhoni:player {name: "MahendraSingh Dhoni", YOB: 1981, POB: "Ranchi"}) 
REMOVE Dhoni:player 
RETURN Dhoni 
```

## 删除多个标签

您也可以从现有节点中删除多个标签。

### 句法

以下是从节点删除多个标签的语法。

```
MATCH (node:label1:label2 {properties . . . . . . . . }) 
REMOVE node:label1:label2 
RETURN node
```

### 例

在继续该示例之前，如下所示创建节点Ishant。

```
CREATE (Ishant:player:person {name: "Ishant Sharma", YOB: 1988, POB: "Delhi"}) 
```

以下是一个示例Cypher查询，用于从节点中删除多个标签。

```
MATCH (Ishant:player:person {name: "Ishant Sharma", YOB: 1988, POB: "Delhi"}) 
REMOVE Ishant:player:person 
RETURN Ishant 
```
