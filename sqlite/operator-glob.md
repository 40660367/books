# SQLite GLOB运算符

SQLite **GLOB**运算符用于仅使用通配符将文本值与模式匹配。如果搜索表达式可以与模式表达式匹配，则GLOB运算符将返回true，即为1。与LIKE运算符不同，GLOB区分大小写，并且它遵循UNIX的语法来指定THE以下通配符。

- 星号（*）
- 问号（？）

星号（*）表示零个或多个数字或字符。问号（？）代表单个数字或字符。

## 句法

以下是*****和**？**的基本语法**。**。

```sql
SELECT FROM table_name
WHERE column GLOB 'XXXX*'
or 
SELECT FROM table_name
WHERE column GLOB '*XXXX*'
or
SELECT FROM table_name
WHERE column GLOB 'XXXX?'
or
SELECT FROM table_name
WHERE column GLOB '?XXXX'
or
SELECT FROM table_name
WHERE column GLOB '?XXXX?'
or
SELECT FROM table_name
WHERE column GLOB '????'
```

您可以使用AND或OR运算符组合**N**个条件。在此，XXXX可以是任何数字或字符串值。

## 例

下表列出了许多示例，这些示例显示WHERE部分的LIKE子句带有不同的'*'和'？' 操作员。

| 序号 |                          声明与说明                          |
| ---- | :----------------------------------------------------------: |
| 1个  |      **WHERE SALARY GLOB '200\*'**查找以200开头的任何值      |
| 2    |     **WHERE SALARY GLOB '\*200\*'**查找任何位置有200的值     |
| 3    | **WHERE SALARY GLOB '?00\*'** 查找在第二和第三位置具有00的任何值 |
| 4    | **WHERE SALARY GLOB '2??'** 查找以2开头且长度至少为3个字符的任何值 |
| 5    |        **WHERE SALARY GLOB '\*2'**查找以2结尾的任何值        |
| 6    | **WHERE SALARY GLOB '?2\*3'**查找第二个位置带有2并以3结尾的任何值 |
| 7    | **WALE SALARY GLOB'2 ??? 3'**查找以2开头和3结束的五位数数字中的任何值 |

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

下面是一个示例，它将显示COMPANY表中的所有记录，其中AGE以2开头。

```
ELECT * FROM COMPANY WHERE AGE  GLOB '2*';
```

康康

以下是一个示例，它将显示COMPANY表中的所有记录，其中ADDRESS在文本内将带有连字符（-）-

```
SELECT * FROM COMPANY WHERE ADDRESS  GLOB '*-*';
```

康康

