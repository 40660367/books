# SQLite LIKE运算符

SQLite **LIKE**运算符用于使用通配符将文本值与模式匹配。如果搜索表达式可以与模式表达式匹配，则LIKE运算符将返回true，即为1。LIKE运算符与两个通配符一起使用-

- 百分号（％）
- 下划线（_）

百分号代表零个，一个或多个数字或字符。下划线表示单个数字或字符。这些符号可以组合使用

## 句法

以下是％和_的基本语法。

```
SELECT FROM table_name
WHERE column LIKE 'XXXX%'
or 
SELECT FROM table_name
WHERE column LIKE '%XXXX%'
or
SELECT FROM table_name
WHERE column LIKE 'XXXX_'
or
SELECT FROM table_name
WHERE column LIKE '_XXXX'
or
SELECT FROM table_name
WHERE column LIKE '_XXXX_'
```

您可以使用AND或OR运算符组合**N**个条件。在此，XXXX可以是任何数字或字符串值。

## 例

[请先进行SQLite3的安装及示例数据库的导入，并查看表格相应数据](/sqlite/setup.html)

下表列出了许多示例，这些示例显示WHERE部分具有不同的LIKE子句，且带有'％'和'_'运算符。

| 序号 |                          声明与说明                          |
| ---- | :----------------------------------------------------------: |
| 1个  |      **WHERE SALARY LIKE '200%'**查找以200开头的任何值       |
| 2    |      **WHERE SALARY LIKE '%200%'**查找任何位置有200的值      |
| 3    | **WHERE SALARY LIKE '_00%'**查找在第二和第三位置具有00的任何值 |
| 4    | **WHERE SALARY LIKE '2_%_%'**查找以2开头且长度至少为3个字符的任何值 |
| 5    |        **WHERE SALARY LIKE '%2'**查找以2结尾的任何值         |
| 6    | **WHERE SALARY LIKE '_2%3'**查找第二个位置带有2并以3结尾的任何值 |
| 7    | **WHERE SALARY LIKE '2___3'**查找以2开头和3结束的五位数数字中的任何值 |

下面是一个示例，它将显示COMPANY表中AGE以2开头的所有记录。

```
SELECT * FROM COMPANY WHERE AGE LIKE '2%';
```

康康

下面是一个示例，它将显示COMPANY表中的所有记录，其中ADDRESS在文本内将带有连字符（-）。

```
SELECT * FROM COMPANY WHERE ADDRESS  LIKE '%-%';
```

康康

