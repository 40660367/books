# Neo4j CQL创建节点

节点是图形数据库中的数据/记录。您可以使用**CREATE**子句在Neo4j中创建一个节点。本章教你如何-

- 创建一个节点
- 创建多个节点
- 创建带有标签的节点
- 创建具有多个标签的节点
- 创建具有属性的节点
- 返回创建的节点

## 创建一个节点

您可以在Neo4j中创建节点，只需指定要创建的节点的名称以及CREATE子句即可。

### 句法

以下是使用Cypher Query Language创建节点的语法。

```cql
CREATE (node_name); 
```

**注意** -分号（;）是可选的。

### 例

环境准备：

以下是一个示例Cypher查询，它在Neo4j中创建一个节点。

```cql
CREATE (sample) 
```

### 验证

要验证节点类型的创建，请在Dollar提示符下执行以下查询。

```cql
MATCH (n) RETURN n
```

该查询返回数据库中的所有节点（我们将在接下来的章节中详细讨论该查询）。

执行后，此查询将显示创建的节点，如以下屏幕截图所示。

## 创建多个节点

Neo4j CQL的create子句还用于同时创建多个节点。为此，您需要传递要创建的节点的名称，并以逗号分隔。

### 句法

以下是使用CREATE子句创建多个节点的语法。

```cql
CREATE (node1),(node2)
```

### 例

以下是一个示例密码查询，该查询在Neo4j中创建多个节点。

```cql
CREATE (sample1),(sample2) 
```

### 验证

要验证节点的创建，请在Dollar提示符下键入并执行以下查询。

```
MATCH (n) RETURN n 
```

## 创建带有标签的节点

Neo4j中的标签用于使用标签对节点进行分组（分类）。您可以使用CREATE子句在Neo4j中为节点创建标签。

### 句法

以下是使用Cypher Query Language创建带有标签的节点的语法。

```cql
CREATE (node:label) 
```

### 例

以下是一个示例密码查询，该查询创建带有标签的节点。

```cql
CREATE (Dhawan:player) 
```

要执行上述查询，请执行以下步骤-

### 验证

要验证节点的创建，请在Dollar提示符下键入并执行以下查询。

```
MATCH (n) RETURN n 
```

该查询返回数据库中的所有节点（我们将在接下来的章节中详细讨论该查询）。

## 创建具有多个标签的节点

您还可以为单个节点创建多个标签。您需要通过用冒号“：”分隔节点来指定节点的标签。

### 句法

以下是创建具有多个标签的节点的语法。

```cql
CREATE (node:label1:label2:. . . . labeln) 
```

### 例

以下是一个示例密码查询，该查询在Neo4j中创建带有多个标签的节点。

```cql
CREATE (Dhawan:person:player) 
```

### 验证

要验证节点的创建，请在Dollar提示符下键入并执行以下查询。

```cql
MATCH (n) RETURN n 
```

该查询返回数据库中的所有节点（我们将在接下来的章节中详细讨论该查询）。

## 创建具有属性的节点

属性是节点用于存储数据的键值对。您可以使用CREATE子句创建具有属性的节点。您需要在花括号“ {}”中指定这些属性，并用逗号分隔。

### 句法

以下是创建具有属性的节点的语法。

```cql
CREATE (node:label { key1: value, key2: value, . . . . . . . . .  }) 
```

### 例

以下是一个示例Cypher查询，该查询创建具有属性的节点。

```cql
CREATE (Dhawan:player{name: "Shikar Dhawan", YOB: 1985, POB: "Delhi"}) 
```

要执行上述查询，请执行以下步骤-

### 验证

要验证节点的创建，请在Dollar提示符下键入并执行以下查询。

```cql
MATCH (n) RETURN n 
```

该查询返回数据库中的所有节点（我们将在接下来的章节中详细讨论该查询）。

## 返回创建的节点

在本章中，我们使用**MATCH（n）RETURN n**查询来查看创建的节点。该查询返回数据库中所有现有的节点。

取而代之的是，我们可以将RETURN子句与CREATE一起使用以查看新创建的节点。

### 句法

以下是在Neo4j中返回节点的语法。

```cql
CREATE (Node:Label{properties. . . . }) RETURN Node 
```

### 例

以下是一个示例Cypher Query，该查询创建具有属性的节点并将其返回。

```cql
CREATE (Dhawan:player{name: "Shikar Dhawan", YOB: 1985, POB: "Delhi"}) RETURN Dhawan 
```

### 验证

要验证节点的创建，请在Dollar提示符下键入并执行以下查询。

```cql
MATCH (n) RETURN n 
```

该查询返回数据库中的所有节点（我们将在接下来的章节中详细讨论该查询）。