# PHP 关联数组

PHP允许在PHP中使用`=>`符号将名称/标签与每个数组元素相关联。使用这种方式，可以很容易记住元素，因为每个元素由标号表示一个递增的数字。

## 定义

有两种方法来定义关联数组：

**第一种方式：**

```php
$salary=array("Hema"=>"550000","Vimal"=>"250000","Ratan"=>"200000");
```

**第二种方式：**

```php
$salary["Hema"]="550000";  
$salary["Vimal"]="250000";  
$salary["Ratan"]="200000";
```

**示例1**

文件名:array-associative1.php

```php
<?php    
$salary=array("Hema"=>"550000","Vimal"=>"250000","Ratan"=>"200000");  
echo "Hema salary: ".$salary["Hema"]."<br/>";  
echo "Vimal salary: ".$salary["Vimal"]."<br/>";  
echo "Ratan salary: ".$salary["Ratan"]."<br/>";  
?>
```

```bash
php /var/www/html/array-associative1.php
```

URL预览:`{host0.http_url}array-associative1.php`

**示例2**

文件名:array-associative2.php

```php
<?php    
$salary["Maxsu"]="550000";  
$salary["Vimal"]="250000";  
$salary["Ratan"]="200000";   
echo "Maxsu salary: ".$salary["Maxsu"]."<br/>";  
echo "Vimal salary: ".$salary["Vimal"]."<br/>";  
echo "Ratan salary: ".$salary["Ratan"]."<br/>";  
?>
```

```bash
php /var/www/html/array-associative2.php
```

URL预览:`{host0.http_url}array-associative2.php`

## 遍历PHP关联数组

使用PHP的foreach循环，我们可以很容易地遍历PHP关联数组的元素。

**示例3**

文件名:array-foreach.php

```php
<?php    
$salary=array("Maxsu"=>"550000","Vimal"=>"250000","Ratan"=>"200000");  
foreach($salary as $k => $v) {  
    echo "Key: ".$k." Value: ".$v."<br/>";  
}  
?>
```

```bash
php /var/www/html/array-foreach.php
```

URL预览:`{host0.http_url}array-foreach.php`