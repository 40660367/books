# Neo4j limit限制子句

CQL的**限制**子句用于限制输出的行数。

## 限制子句

### 句法

以下是LIMIT子句的语法。

```cql
MATCH (n) 
RETURN n 
ORDER BY n.name 
LIMIT 3 
```

### 例

在继续该示例之前，如下所示在Neo4j数据库中创建5个节点。

```cql
CREATE(Dhawan:player{name:"shikar Dhawan", YOB: 1985, runs:363, country: "India"})
CREATE(Jonathan:player{name:"Jonathan Trott", YOB:1981, runs:229, country:"South Africa"})
CREATE(Sangakkara:player{name:"Kumar Sangakkara", YOB:1977, runs:222, country:"Srilanka"})
CREATE(Rohit:player{name:"Rohit Sharma", YOB: 1987, runs:177, country:"India"})
CREATE(Virat:player{name:"Virat Kohli", YOB: 1988, runs:176, country:"India"})
```

以下是一个示例密码查询，该查询以降序返回上面创建的节点，并将结果中的记录限制为3。

```cql
MATCH (n)  
RETURN n.name, n.runs 
ORDER BY n.runs DESC 
LIMIT 3 
```

## 限制表达式

您还可以在表达式中使用LIMIT子句。

### 例

以下是一个示例Cypher Query，它使用表达式来限制记录。

```cql
MATCH (n) 
RETURN n.name, n.runs 
ORDER BY n.runs DESC 
LIMIT toInt(3 * rand())+ 1 
```
