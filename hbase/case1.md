# HBase Shell操作案例1

[环境准备](./setup.html)

#### 测试说明

这里我们用一个学生成绩表作为例子，对 HBase 的基本操作和基本概念进行讲解。

下面是学生的成绩表：

```
name   grad      course:math   course:art
Tom     1            87           97
Jerry   2            100          80
```

这里 grad 对于表来说是一个列，course 对于表来说是一个列族，这个列族由两个列组成 :math 和 :art，当然我们可以根据需要在 course 中建立更多的列族，如 computer、physics 等相应的列添加入 course 列族。

**建立一个表格 scores 具有两个列族 grad 和 courese**

```hbase
create 'scores', 'grade', 'course'
```

**查看当前 HBase 中具有哪些表**

```hbase
list
```

**查看表的构造**

```hbase
describe 'scores'
```

**插入数据**

新建 Tom 行健并插入数据：

```hbase
put 'scores', 'Tom', 'grade:', '1'
put 'scores', 'Tom', 'course:math', '87'
put 'scores', 'Tom', 'course:art', '97'
```

新建 Jerry 行健并插入数据：

```hbase
put 'scores', 'Jerry', 'grade:', '2'
put 'scores', 'Jerry', 'course:math', '100'
put 'scores', 'Jerry', 'course:art', '80'
```

**查看 scores 表中 Tom 的相关数据**

```hbase
get 'scores', 'Tom'
```

**查看 scores 表中所有数据**

```hbase
scan 'scores'
```
