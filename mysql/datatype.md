# MySQL 数据类型(datatype)

在本教程中，您将了解MySQL数据类型以及如何在MySQL中设计数据库时有效地使用它们。

数据库表包含具有特定数据类型(如数字或字符串)的多个列。 MySQL提供更多的数据类型，而不仅仅是数字或字符串。 MySQL中的每种数据类型都可以通过以下特征来确定：

- 它用来表示数据值。
- 占用的空间以及值是固定长度还是可变长度。
- 数据类型的值可以被索引。
- MySQL如何比较特定数据类型的值。

| 数据类型     | 指定值和范围                                      |
| ------------ | ------------------------------------------------- |
| `char`       | String(0~255)                                     |
| `varchar`    | String(0~255)                                     |
| `tinytext`   | String(0~255)                                     |
| `text`       | String(0~65536)                                   |
| `blob`       | String(0~65536)                                   |
| `mediumtext` | String(0~16777215)                                |
| `mediumblob` | String(0~16777215)                                |
| `longblob`   | String(0~4294967295)                              |
| `longtext`   | String(0~4294967295)                              |
| `tinyint`    | Integer(-128~127)                                 |
| `smallint`   | Integer(-32768~32767)                             |
| `mediumint`  | Integer(-8388608~8388607)                         |
| `int`        | Integer(-214847668~214847667)                     |
| `bigint`     | Integer(-9223372036854775808~9223372036854775807) |
| `float`      | decimal(精确到23位小数)                           |
| `double`     | decimal(24~54位小数)                              |
| `decimal`    | 将`double`转储为字符串形式                        |
| `date`       | *YYYY-MM-DD*                                      |
| `datetime`   | *YYYY-MM-DD HH:MM:SS*                             |
| `timestamp`  | *YYYYMMDDHHMMSS*                                  |
| `time`       | *HH:MM:SS*                                        |
| `enum`       | 选项值之一                                        |
| `set`        | 选项值子集                                        |
| `boolean`    | tinyint(1)                                        |

## MySQL数值数据类型

在MySQL中，您可以找到所有SQL标准数字类型，包括精确数字数据类型和近似数字数据类型，包括整数，定点和浮点数。 此外，MySQL还具有用于存储位值的BIT数据类型。数字类型可以是有符号或无符号，但`BIT`类型除外。

下表显示了MySQL中数字类型的总结：

| 数字类型    | 描述               |
| ----------- | ------------------ |
| `TINYINT`   | 一个很小的整数     |
| `SMALLINT`  | 一个小的整数       |
| `MEDIUMINT` | 一个中等大小的整数 |
| `INT`       | 一个标准整数       |
| `BIGINT`    | 一个大整数         |
| `DECIMAL`   | 定点数             |
| `FLOAT`     | 单精度浮点数       |
| `DOUBLE`    | 双精度浮点数       |
| `BIT`       | 一个字节字段       |

## MySQL布尔数据类型

MySQL没有内置的BOOLEAN或BOOL]数据类型。所以要表示布尔值，MySQL使用最小的整数类型，也就是`TINYINT(1)`。 换句话说，`BOOLEAN`和`BOOL`是`TINYINT(1)`的同义词。

## MySQL字符串数据类型

在MySQL中，字符串可以容纳从纯文本到二进制数据(如图像或文件)的任何内容。可以通过使用[LIKE](./like.html)运算符，[正则表达式](./regexp.html)和[自然语言全文搜索](./fts.html)，根据模式匹配来比较和搜索字符串。

下表显示了MySQL中的字符串数据类型：

| 字符串类型   | 描述                                      |
| ------------ | ----------------------------------------- |
| `char`       | 固定长度的非二进制(字符)字符串            |
| `varchar`    | 可变长度的非二进制字符串                  |
| `BINARY`     | 一个固定长度的二进制字符串                |
| `VARBINARY`  | 一个可变长度的二进制字符串                |
| `TINYBLOB`   | 一个非常小的BLOB(二进制大对象)            |
| `BLOB`       | 一个小的BLOB(二进制大对象)                |
| `MEDIUMBLOB` | 一个中等大小的BLOB(二进制大对象)          |
| `LONGBLOB`   | 一个大的BLOB(二进制大对象)                |
| `TINYTEXT`   | 一个非常小的非二进制字符串                |
| `TEXT`       | 一个小的非二进制字符串                    |
| `MEDIUMTEXT` | 一个中等大小的非二进制字符串              |
| `LONGTEXT`   | 一个很大的非二进制字符串                  |
| `ENUM`       | 枚举; 每个列值可以被分配一个枚举成员      |
| `SET`        | 集合; 每个列值可以分配零个或多个`SET`成员 |

## MySQL日期和时间数据类型

MySQL提供日期和时间的类型以及日期和时间的组合。 此外，MySQL还支持时间戳数据类型，用于跟踪表的一行中的更改。如果只想存储没有日期和月份的年份数据，则可以使用`YEAR`数据类型。

下表说明了MySQL日期和时间数据类型：

| 字符串类型  | 描述                                    |
| ----------- | --------------------------------------- |
| `DATE`      | `YYYY-MM-DD`格式的日期值                |
| `TIME`      | `hh:mm:ss`格式的时间值                  |
| `DATETIME`  | `YYYY-MM-DD hh:mm:ss`格式的日期和时间值 |
| `TIMESTAMP` | `YYYY-MM-DD hh:mm:ss`格式的时间戳记值   |
| `YEAR`      | `YYYY`或`YY`格式的年值                  |

## MySQL空间数据类型

MySQL支持许多包含各种几何和地理值的空间数据类型，如下表所示：

| 字符串类型           | 描述                      |
| -------------------- | ------------------------- |
| `GEOMETRY`           | 任何类型的空间值          |
| `POINT`              | 一个点(一对X-Y坐标)       |
| `LINESTRING`         | 曲线(一个或多个`POINT`值) |
| `POLYGON`            | 多边形                    |
| `GEOMETRYCOLLECTION` | `GEOMETRY`值的集合        |
| `MULTILINESTRING`    | `LINESTRING`值的集合      |
| `MULTIPOINT`         | `POINT`值的集合           |
| `MULTIPOLYGON`       | `POLYGON`值的集合         |

## JSON数据类型

MySQL `5.7.8`版本支持原生JSON数据类型，可以更有效地存储和管理JSON文档。 本机JSON数据类型提供JSON文档的自动验证和最佳存储格式。

在本教程中，您学习了各种MySQL数据类型，可帮助您确定在创建表时应使用哪些数据类型。
