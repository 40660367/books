# MySQL 交叉连接(CROSS JOIN)			

在本教程中，您将了解MySQL `CROSS JOIN`子句以及如何应用它来解决一些有趣的数据问题。

## MySQL CROSS JOIN子句简介

`CROSS JOIN`子句从连接的表返回行的笛卡儿乘积。

假设使用`CROSS JOIN`连接两个表。 结果集将包括两个表中的所有行，其中结果集中的每一行都是第一个表中的行与第二个表中的行的组合。 当连接的表之间没有关系时，会使用这种情况。

要特别注意的是，如果每个表有`1000`行，那么结果集中就有`1000 x 1000 = 1,000,000`行，那么数据量是非常巨大的。

下面说明连接两个表：`T1`和`T2`的`CROSS JOIN`子句的语法：

```sql
SELECT 
    *
FROM
    T1
        CROSS JOIN
    T2;
```

请注意，与[INNER JOIN](./join-inner.html)或[LEFT JOIN](./join-left.html)子句不同，`CROSS JOIN`子句不具有连接条件。

如果添加了`WHERE`子句，如果`T1`和`T2`有关系，则`CROSS JOIN`的工作方式与`INNER JOIN`子句类似，如以下查询所示：

```sql
SELECT 
    *
FROM
    T1
        CROSS JOIN
    T2
WHERE
    T1.id = T2.id;
```

## MySQL CROSS JOIN子句示例

下面我们将使用以下几个表来演示`CROSS JOIN`的工作原理。

```sql
CREATE DATABASE IF NOT EXISTS testdb;
USE testdb;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    id INT PRIMARY KEY AUTO_INCREMENT,
    product_name VARCHAR(100),
    price DECIMAL(13 , 2 )
);

DROP TABLE IF EXISTS sales;

CREATE TABLE stores (
    id INT PRIMARY KEY AUTO_INCREMENT,
    store_name VARCHAR(100)
);

DROP TABLE IF EXISTS sales;

CREATE TABLE sales (
    product_id INT,
    store_id INT,
    quantity DECIMAL(13 , 2 ) NOT NULL,
    sales_date DATE NOT NULL,
    PRIMARY KEY (product_id , store_id),
    FOREIGN KEY (product_id)
        REFERENCES products (id)
        ON DELETE CASCADE ON UPDATE CASCADE,
    FOREIGN KEY (store_id)
        REFERENCES stores (id)
        ON DELETE CASCADE ON UPDATE CASCADE
);
```

上面语句中，创建了三个表：

- 产品(`products`)表包含产品编号，产品名称和销售价格等产品主要数据。
- 商店(`stores`)表包含销售产品的商店信息。
- 销售(`sales`)表包含在特定商店按数量和日期销售的产品。

假设有三个产品：`iPhone`，`iPad`和`Macbook Pro`，在北部(`North`)和南部(`South`)的这两个商店中出售。

```sql
INSERT INTO products(product_name, price)
VALUES('iPhone', 699),
      ('iPad',599),
      ('Macbook Pro',1299);

INSERT INTO stores(store_name)
VALUES('North'),
      ('South');

INSERT INTO sales(store_id,product_id,quantity,sales_date)
VALUES(1,1,20,'2017-01-02'),
      (1,2,15,'2017-01-05'),
      (1,3,25,'2017-01-05'),
      (2,1,30,'2017-01-02'),
      (2,2,35,'2017-01-05');
```

要获得每个商店和每个产品的总销售额，您可以计算销售额，并按商店和产品分组如下：

```sql
SELECT 
    store_name,
    product_name,
    SUM(quantity * price) AS revenue
FROM
    sales
        INNER JOIN
    products ON products.id = sales.product_id
        INNER JOIN
    stores ON stores.id = sales.store_id
GROUP BY store_name , product_name;
```

现在，如果你想知道哪个商店中的哪些产品的没有销售怎么办？ 上面的查询无法回答这个问题。

要解决这个问题，可以使用`CROSS JOIN`子句。

首先，使用`CROSS JOIN`子句来获取所有商店和产品的组合：

```sql
SELECT 
    store_name, product_name
FROM
    stores AS a
        CROSS JOIN
    products AS b;
```

接下来，将上述查询的结果与按商店和产品返回总销售额的查询相结合。以下查询说明了这个想法：

```sql
SELECT 
    b.store_name,
    a.product_name,
    IFNULL(c.revenue, 0) AS revenue
FROM
    products AS a
        CROSS JOIN
    stores AS b
        LEFT JOIN
    (SELECT 
        stores.id AS store_id,
        products.id AS product_id,
        store_name,
            product_name,
            ROUND(SUM(quantity * price), 0) AS revenue
    FROM
        sales
    INNER JOIN products ON products.id = sales.product_id
    INNER JOIN stores ON stores.id = sales.store_id
    GROUP BY store_name , product_name) AS c ON c.store_id = b.id
        AND c.product_id= a.id
ORDER BY b.store_name;
```

请注意，如果收入为`NULL`(表示商店没有销售的产品)，则查询使用IFNULL函数返回`0`。

通过这样使用`CROSS JOIN`子句，可以解决类似这样的问题，例如销售人员按月查找销售收入，即使推销员在特定月份没有销售产品。