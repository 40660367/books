# Neo4j CQL运算符

以下是Neo4j Cypher Query语言支持的运算符列表。

| 序号 |             类型             |               运算符                |
| :--: | :--------------------------: | :---------------------------------: |
|  1   |       代数Mathematical       |          +，-，*，/，％，^          |
|  2   |        比较Comparison        |        +，<>，<，>，<=，> =         |
|  3   |        布尔型Boolean         |          AND，OR，XOR，NOT          |
|  4   |         字符串String         |                  +                  |
|  5   |           列表List           |         +, IN, [X], [X…..Y]         |
|  6   | 正则表达式Regular Expression |                 =-                  |
|  7   |  字符串匹配String matching   | STARTS WITH, ENDS WITH, CONSTRAINTS |

## Neo4j CQL中的布尔运算符

Neo4j支持以下布尔运算符，以在Neo4j CQL WHERE子句中使用以支持多个条件。

| 序号 | 布尔运算符 |                             描述                             |
| :--: | :--------: | :----------------------------------------------------------: |
|  1   |    AND     | 它是Neo4j CQL关键字，用于支持AND运算。就像SQL AND运算符一样。 |
|  2   |     OR     | 它是Neo4j CQL关键字，用于支持OR操作。就像SQL AND运算符一样。 |
|  3   |    NOT     |  它是Neo4j CQL关键字，支持NOT操作。就像SQL AND运算符一样。   |
|  4   |    XOR     | 它是Neo4j CQL关键字，用于支持XOR操作。就像SQL AND运算符一样。 |

## Neo4j CQL中的比较运算符

Neo4j支持以下在Neo4j CQL WHERE子句中使用的比较运算符以支持条件。

| 序号 | 布尔运算符 |               描述                |
| :--: | :--------: | :-------------------------------: |
|  1   |     =      |    它是Neo4j CQL“等于”运算符。    |
|  2   |     <>     |   它是Neo4j CQL“不等于”运算符。   |
|  3   |     <      |    它是Neo4j CQL“小于”运算符。    |
|  4   |     >      |    它是Neo4j CQL“大于”操作员。    |
|  5   |     <=     | 它是Neo4j CQL“小于或等于”运算符。 |
|  6   |    > =     | 它是Neo4j CQL“大于或等于”运算符。 |

