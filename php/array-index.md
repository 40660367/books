# PHP 数组索引

PHP索引数组是一个数组，默认情况下由索引号表示。 数组的所有元素是由从`0`开始的索引号来表示的。

PHP索引数组可以存储数字，字符串或任何对象。 PHP索引数组也称为数值数组。

## 定义

有两种方法来定义索引数组：

**第一种方式：**

```php
$size=array("Big","Medium","Short");
```

**第二种方式：**

```php
$size[0]="Big";  
$size[1]="Medium";  
$size[2]="Short";
```

## PHP索引数组示例

文件名:array-index1.php

```php
<?php  
$size=array("Big","Medium","Short");  
echo "Size: $size[0], $size[1] and $size[2]";  
?>
```

```bash
php /var/www/html/array-index1.php
```

URL预览:`{host0.http_url}array-index1.php`

文件名：array-index2.php

```php
<?php  
$size[0]="Big";  
$size[1]="Medium";  
$size[2]="Short";  
echo "Size: $size[0], $size[1] and $size[2]";  
?>
```

```bash
php /var/www/html/array-index2.php
```

URL预览:`{host0.http_url}array-index2.php`

## 遍历PHP索引数组

我们可以使用`foreach`循环在PHP中来遍历数组。 下面来看看一个简单遍历PHP数组的所有元素的例子。

文件名:array-index3.php

```php
<?php  
$size=array("Big","Medium","Short");  
foreach( $size as $s )  
{  
  echo "Size is: $s<br />";  
}  
?>
```

```bash
php /var/www/html/array-index3.php
```

URL预览:`{host0.http_url}array-index3.php`

## PHP索引数组的计数长度

PHP提供`count()`函数来计算并返回数组的长度。

文件名:array-index4.php

```php
<?php  
$size=array("Big","Medium","Short");  
echo count($size);  
?>
```

```bash
php /var/www/html/array-index4.php
```

URL预览:`{host0.http_url}array-index4.php`