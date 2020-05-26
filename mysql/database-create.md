# MySQL 创建数据库

在本教程中，您将学习如何在MySQL中管理数据库。例如，学习如何创建新的数据库，删除现有数据库以及显示MySQL数据库服务器中的所有数据库。

下面让我们演示如何在MySQL中创建一个新的数据库。

## 创建数据库

在与数据进行任何其他操作之前，需要创建一个数据库。数据库是数据的容器。它可以用于存储联系人，供应商，客户或任何想存储的数据。 在MySQL中，数据库是用于存储和操作诸如表，数据库视图，触发器，存储过程等数据的对象的集合。

要在MySQL中创建数据库，请使用`CREATE DATABASE`语句，如下：

```sql
CREATE DATABASE [IF NOT EXISTS] database_name;
```

我们来更详细地看看`CREATE DATABASE`语句：

- `CREATE DATABASE`语句的后面是要创建的数据库名称。建议数据库名称尽可能是有意义和具有一定的描述性。
- `IF NOT EXISTS`是语句的可选子句。 `IF NOT EXISTS`子句可防止创建数据库服务器中已存在的新数据库的错误。不能在MySQL数据库服务器中具有相同名称的数据库。

例如，要创建一个名称为`mytestdb`数据库，可以执行`CREATE DATABASE`语句后接数据库名称：`mytestdb`，如果当前MySQL服务器中没有数据库：`mytestdb`，则创建成功，如下所示：

```sql
CREATE DATABASE IF NOT EXISTS mytestdb;
```

执行此语句后，MySQL返回一条消息，通知新数据库是否已成功创建。

**显示数据库**

`SHOW DATABASES`语句显示MySQL数据库服务器中的所有数据库。您可以使用`SHOW DATABASES`语句来查看您要创建的数据库，或者在创建新数据库之前查看数据库服务器上的所有数据库，例如：

```sql
SHOW DATABASES;
```
在此MySQL数据库服务器中有`6`个数据库。 `information_schema`，`performance_schema`和`mysql`是我们安装MySQL时可用的默认数据库，而`mytestdb`是刚刚创建的新数据库。

**选择要使用的数据库**

在使用指定数据库之前，必须通过使用`USE`语句告诉MySQL要使用哪个数据库。

您可以使用`USE`语句选择示例数据库(`mytestdb`)，如下所示：

```sql
USE mytestdb;
```

从现在开始，所有操作(如查询数据，创建新表或调用存储过程)都将对当前数据库(即`mytestdb`)产生影响。
