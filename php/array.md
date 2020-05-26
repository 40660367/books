# PHP 数组

PHP数组是一个有序映射(包含基于键的值)。 它用于在单个变量中保存相似类型的多个值。

## PHP数组的优点

**更少的代码：**不需要定义多个变量。
**易于遍历：** 通过使用单循环，遍历数组的所有元素。
**排序：** 可以对数组的元素进行排序。

## PHP数组类型

PHP中有`3`种类型的数组。

- 索引数组
- 关联数组
- 多维数组

## PHP索引数组

PHP索引是由从`0`开始的数字表示。我们可以在PHP数组中存储数字，字符串和对象。 默认情况下，所有PHP数组元素都被分配给索引号。

有两种方法来定义索引数组：
**第一种方式：**

```php
<?php
$season=array("summer","winter","spring","autumn");  
// 等效于以下方式
$season=array(0=>"summer",1=>"winter",2=>"spring",3=>"autumn");  
?>
```

**第二种方式：**

```php
<?php
$season[0]="summer";  
$season[1]="winter";  
$season[2]="spring";  
$season[3]="autumn";
?>
```

## 示例

文件名：array1.php

```php
<?php  
$season=array("summer","winter","spring","autumn");  
echo "Season are: $season[0], $season[1], $season[2] and $season[3]";  
?>
```

```bash
php /var/www/html/array1.php
```

URL预览:`{host0.http_url}array1.php`

文件名: array2.php

```php
<?php  
$season[0]="summer";  
$season[1]="winter";  
$season[2]="spring";  
$season[3]="autumn";  
echo "Season are: $season[0], $season[1], $season[2] and $season[3]";  
?>
```

```bash
php /var/www/html/array2.php
```

URL预览:`{host0.http_url}array2.php`

## PHP关联数组

我们可以使用`=>`符号将名称与PHP中的每个数组元素的值相关联。

有两种方法来定义关联数组：

**第一种方式：**

```php
<?php  
$salary=array("key1"=>"350000","key2"=>"450000","minsu"=>"200000");  
?>
```

**第二种方式：**

```php
<?php  
$salary["key1"]="350000";  
$salary["key2"]="450000";  
$salary["minsu"]="200000";  
?>
```

## 关联数组示例

文件名: arrayassociative1.php

```php
<?php    
$salary=array("Hema"=>"350000","John"=>"450000","Kartik"=>"200000");    
echo "Hema salary: ".$salary["Hema"]."<br/>";  
echo "John salary: ".$salary["John"]."<br/>";  
echo "Kartik salary: ".$salary["Kartik"]."<br/>";  
?>
```

```bash
php /var/www/html/arrayassociative1.php
```

URL预览:`{host0.http_url}arrayassociative1.php`

文件名: arrayassociative2.php

```php
<?php    
$salary["Hema"]="350000";    
$salary["John"]="450000";    
$salary["Kartik"]="200000";    
echo "Hema salary: ".$salary["Hema"]."<br/>";  
echo "John salary: ".$salary["John"]."<br/>";  
echo "Kartik salary: ".$salary["Kartik"]."<br/>";  
?>
```

```bash
php /var/www/html/arrayassociative2.php
```

URL预览:`{host0.http_url}arrayassociative2.php`