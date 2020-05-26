# PHP 函数按引用调用

在PHP中，通过引用调用的情况下，如果在函数内修改实际值，则修改了变量的值。 在这种情况下，需要使用`＆`(和号)符号与形式参数。 `＆`表示变量的引用。

让我们通过下面的例子来帮助理解引用调用的概念。

## 实例1

在这个例子中，变量`$str`被传递给加法器函数，它与“`Call By Reference`”字符串连接。 在这里，打印`$str`变量的结果值为：’`this is Call By Reference`‘。 这是因为改变的是变量`$str`的实际值。

文件名:function-callbyref1.php

```php
<?php  
function adder(&$str2)  
{  
    $str2 .= 'Call By Reference';  
}  
$str = 'This is ';  
adder($str);  
echo $str;  
?>
```

```bash
php /var/www/html/function-callbyref1.php
```

URL预览:`{host0.http_url}function-callbyref1.php`

## 实例2

让我们通过另一个例子来理解PHP中引用调用的概念。

文件名:function-callbyref1.php

```php
<?php  
function increment(&$i)  
{  
    $i++;  
}  
$i = 10;  
increment($i);  
echo $i;  
?>
```

```bash
php /var/www/html/function-callbyref1.php
```

URL预览:`{host0.http_url}function-callbyref1.php`