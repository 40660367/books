# Neo4j orderby排序子句

您可以使用ORDER BY子句按顺序排列结果数据。

### 句法

以下是ORDER BY子句的语法。

```cql
MATCH (n)  
RETURN n.property1, n.property2 . . . . . . . .  
ORDER BY n.property
```

### 例

在继续该示例之前，如下所示，在Neo4j数据库中创建5个节点。

```cql
CREATE(Dhawan:player{name:"shikar Dhawan", YOB: 1985, runs:363, country: "India"})
CREATE(Jonathan:player{name:"Jonathan Trott", YOB:1981, runs:229, country:"South Africa"})
CREATE(Sangakkara:player{name:"Kumar Sangakkara", YOB:1977, runs:222, country:"Srilanka"})
CREATE(Rohit:player{name:"Rohit Sharma", YOB: 1987, runs:177, country:"India"})
CREATE(Virat:player{name:"Virat Kohli", YOB: 1988, runs:176, country:"India"})
```

以下是样本密码查询，该查询按玩家使用ORDERBY子句计分的奔跑顺序返回上述创建的节点。

```cql
MATCH (n)  
RETURN n.name, n.runs 
ORDER BY n.runs 
```

## 通过多个属性对节点排序

您可以使用**ORDEYBY**子句基于多个属性来安排节点。

### 句法

以下是使用ORDERBY子句按多个属性排列节点的语法。

```cql
MATCH (n) 
RETURN n 
ORDER BY n.age, n.name 
```

### 例

以下是一个Cypher Query示例，它根据属性-运行和国家/地区排列了本章前面创建的节点。

```cql
MATCH (n) 
RETURN n.name, n.runs, n.country 
ORDER BY n.runs, n.country
```

## 通过降序对节点排序

您可以使用**ORDERBY**子句按降序排列数据库中的节点。

### 句法

以下是在数据库中排列节点的语法。

```cql
MATCH (n) 
RETURN n 
ORDER BY n.name DESC 
```

### 例

以下是一个示例密码查询，该查询使用ORDERBY子句按降序排列数据库中的节点。

```cql
MATCH (n)  
RETURN n.name, n.runs 
ORDER BY n.runs DESC 
```
