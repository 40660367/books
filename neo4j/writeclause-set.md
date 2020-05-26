# Neo4j set设置子句

使用Set子句，可以将新属性添加到现有的Node或Relationship中，还可以添加或更新现有的Properties值。

在本章中，我们将讨论如何-

- 设置属性
- 移除财产
- 设置多个属性
- 在节点上设置标签
- 在一个节点上设置多个标签

## 设置属性

使用SET子句，可以在节点中创建新属性。

### 句法

以下是设置属性的语法。

```cql
MATCH (node:label{properties . . . . . . . . . . . . . . }) 
SET node.property = value 
RETURN node
```

### 例

在继续该示例之前，首先创建一个名为Dhawan的节点，如下所示。

```cql
CREATE (Dhawan:player{name: "shikar Dhawan", YOB: 1985, POB: "Delhi"}) 
```

以下是一个示例Cypher Query，用于创建一个名为*“ highestscore”*，值为*“ 187”*的属性。

```cql
MATCH (Dhawan:player{name: "shikar Dhawan", YOB: 1985, POB: "Delhi"}) 
SET Dhawan.highestscore = 187 
RETURN Dhawan
```

## 删除属性

您可以通过将**NULL**作为值传递给现有属性来删除它。

### 句法

以下是使用SET子句从节点删除属性的语法。

```cql
MATCH (node:label {properties}) 
SET node.property = NULL 
RETURN node 
```

### 例

在继续该示例之前，首先创建一个节点“ jadeja”，如下所示。

```cql
Create (Jadeja:player {name: "Ravindra Jadeja", YOB: 1988, POB: "NavagamGhed"})
```

以下是一个示例密码查询，该查询使用SET子句从该节点删除名为POB的属性，如下所示。

```cql
MATCH (Jadeja:player {name: "Ravindra Jadeja", YOB: 1988, POB: "NavagamGhed"}) 
SET Jadeja.POB = NULL 
RETURN Jadeja 
```

## 设置多个属性

同样，您可以使用Set子句在节点中创建多个属性。为此，您需要用逗号指定这些键值对。

### 句法

以下是使用SET子句在节点中创建多个属性的语法。

```cql
MATCH (node:label {properties}) 
SET node.property1 = value, node.property2 = value 
RETURN node 
```

### 例

以下是一个示例密码查询，该查询使用Neo4j中的SET子句在节点中创建多个属性。

```cql
MATCH (Jadeja:player {name: "Ravindra Jadeja", YOB: 1988})  
SET Jadeja.POB: "NavagamGhed", Jadeja.HS = "90" 
RETURN Jadeja
```

## 在节点上设置标签

您可以使用SET子句为现有节点设置标签。

### 句法

以下是将标签设置到现有节点的语法。

```cql
MATCH (n {properties . . . . . . . }) 
SET n :label 
RETURN n 
```

### 例c

在继续该示例之前，首先创建一个节点“ Anderson”，如下所示。

```cql
CREATE (Anderson {name: "James Anderson", YOB: 1982, POB: "Burnely"})
```

以下是一个示例Cypher Query，用于使用SET子句在节点上设置标签。该查询将标签“ player”添加到节点Anderson并返回它。

```cql
MATCH (Anderson {name: "James Anderson", YOB: 1982, POB: "Burnely"}) 
SET Anderson: player 
RETURN Anderson 
```

## 在节点上设置多个标签

您可以使用SET子句为现有节点设置多个标签。在这里，您需要使用冒号“：”将标签分开来指定标签。

### 句法

以下是使用SET子句为现有节点设置多个标签的语法。

```cql
MATCH (n {properties . . . . . . . }) 
SET n :label1:label2 
RETURN n 
```

### 例

在继续该示例之前，首先创建一个名为“ Ishant”的节点，如下所示。

```cql
CREATE (Ishant {name: "Ishant Sharma", YOB: 1988, POB: "Delhi"}) 
```

以下是一个示例Cypher Query，用于使用SET子句在节点上创建多个标签。

```cql
MATCH (Ishant {name: "Ishant Sharma", YOB: 1988, POB: "Delhi"}) 
SET Ishant: player:person 
RETURN Ishant 
```
