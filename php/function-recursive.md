# PHP 递归函数

PHP还支持递归函数调用像`C/C++`。 在这种情况下，我们在函数内调用当前函数。 它也称为递归。

建议避免递归函数调用超过`200`个递归级别，因为它可能会摧毁堆栈，并最终可能导致脚本的终止。

## 示例1：打印数字

文件名:function-recursive1.php

```php
<?php    
function display($number) {    
    if($number<=5){    
     echo "$number <br/>";    
     display($number+1);    
    }  
}    

display(1);    
?>
```

```bash
php /var/www/html/function-recursive1.php
```

URL预览:`{host0.http_url}function-recursive1.php`

## 示例2：数字阶乘

文件名:function-recursive2.php

```php
<?php    
function factorial($n)    
{    
    if ($n < 0)    
        return -1; /*Wrong value*/    
    if ($n == 0)    
        return 1; /*Terminating condition*/    
    return ($n * factorial ($n -1));    
}    

echo factorial(5);    
?>
```

```bash
php /var/www/html/function-recursive2.php
```

URL预览:`{host0.http_url}function-recursive2.php`