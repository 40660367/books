# PHP 多维数组

PHP多维数组也称为数组数组。 它允许您将表式数据存储在数组中。 PHP多维数组可以以由**行 \*列**表示的矩阵形式表示。

**定义**

```php
$emp = array  
  (  
  array(1,"sonoo",400000),  
  array(2,"john",450000),  
  array(3,"rahul",300000)  
  );
```

## PHP多维数组示例

下面来看看一个简单的PHP多维数组的例子，如下面的表格数据。 在这个例子中，显示`3`行和`3`列。

| 编号 | 姓名  | 薪水   |
| ---- | ----- | ------ |
| 1    | sonoo | 400000 |
| 2    | john  | 450000 |
| 3    | rahul | 30000  |

*文件：array-md1.php*

```php
<?php    
$emp = array  
  (  
  array(1,"sonoo",400000),  
  array(2,"john",450000),  
  array(3,"rahul",300000)  
  );  

for ($row = 0; $row < 3; $row++) {  
  for ($col = 0; $col < 3; $col++) {  
    echo $emp[$row][$col]."  ";  
  }  
  echo "<br/>";  
}  
?>
```

```bash
php /var/www/html/array-md1.php
```

URL预览:`{host0.http_url}array-md1.php`