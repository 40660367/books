# Neo4j skip跳过子句

SKIP子句用于定义从哪一行开始，包括输出中的行。

### 例

在继续该示例之前，请创建5个节点，如下所示。

```cql
CREATE(Dhawan:player{name:"shikar Dhawan", YOB: 1985, runs:363, country: "India"})
CREATE(Jonathan:player{name:"Jonathan Trott", YOB:1981, runs:229, country:"South Africa"})
CREATE(Sangakkara:player{name:"Kumar Sangakkara", YOB:1977, runs:222, country:"Srilanka"})
CREATE(Rohit:player{name:"Rohit Sharma", YOB: 1987, runs:177, country:"India"})
CREATE(Virat:player{name:"Virat Kohli", YOB: 1988, runs:176, country:"India"})
```

以下是一个示例密码查询，该查询将跳过前三个节点，返回数据库中的所有节点。

```cql
MATCH (n)  
RETURN n.name, n.runs 
ORDER BY n.runs DESC 
SKIP 3 
```

## 使用表达式的跳过子句

您可以使用表达式跳过结果的记录。

### 例

以下是使用SKIP子句和表达式的Cypher Query示例。

```cql
MATCH (n)  
RETURN n.name, n.runs 
ORDER BY n.runs DESC 
SKIP toInt (2*rand())+ 1 
```
