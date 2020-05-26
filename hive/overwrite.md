# Hive 数据导出(overwrite)

[环境安装](./setup.html)  [Hive 示例数据准备](./data-import.html)

## Hive数据导出示例

### 直接拷贝数据文件

将表中数据导出。其实Hive表的数据就保存在表目录下。如果保存格式便是所需格式，则直接将表目录下文件下载到指定目录即可。

```bash
mkdir -p ~/hive/products
hadoop fs -get /user/hive/warehouse/products/* ~/hive/products/
cat ~/hive/products/products.dat 
```

### 单个查询导出数据

通过单个查询，将查询结果导出到指定目录。
如下，查询china_products表中food类型的商品，将查询结果写入本地目录下。如果无`local`关键字，则指定路径为hdfs路径。

```hql
insert overwrite local directory '~/hive/products/'
select id,name,price
from products;
```

### 多个查询导出数据

在一次扫描表时，设定多种查询条件，将各自符合的查询结果导出到不同目录下。比如，将china_products表中数据按type的类型，分别保存到不同目录下。

```bash
mkdir -p ~/hive/products-food
mkdir -p ~/hive/products-electronics
```

```hql
from products
insert overwrite local directory '~/hive/products-food/'
select id,name,price where type='food'
insert overwrite local directory '~/hive/products-electronics/'
select id,name,price where type='electronics';
```

