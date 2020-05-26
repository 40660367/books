# PHP 函数按值调用

PHP允许通过值和引用调用函数。在通过值调用PHP的情况下，如果在函数内修改，则不会修改实际值。

让我们通过例子的帮助理解按值调用的概念。

## 实例1

在这个例子中，变量`$str`被传递给加法器函数，它与’`Call By Value`‘字符串连接。 但是，打印`$str`变量的结果只是：’`Hello`‘。 这是因为修改值只是在局部变量`$str2`中完成。 它不反映到`$str`变量中。

文件名:function-callbyvalue1.php

```php
<?php  
function adder($str2)  
{  
    $str2 .= 'Call By Value';  
}  
$str = 'Hello ';  
adder($str);  
echo $str;  
?>
```

```bash
php /var/www/html/function-callbyvalue1.php
```

URL预览:`{host0.http_url}function-callbyvalue1.php`

## 实例2

让我们通过另一个例子来理解PHP按值调用的概念。

文件名:function-callbyvalue2.php

```php
<?php  
function increment($i)  
{  
    $i++;  
}  
$i = 10;  
increment($i);  
echo $i;  
?>
```

```bash
php /var/www/html/function-callbyvalue1.php
```

URL预览:`{host0.http_url}function-callbyvalue2.php`