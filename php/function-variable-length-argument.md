# PHP 可变长度参数函数

PHP支持可变长参数函数。这让我们可以在函数中传递`0`，`1`,`...`或`n`个参数。 为此，您需要在参数名称前使用`3`个省略号(点)。

`3`点(`...`)概念是从**PHP 5.6**开始实现的可变长参数。下面来看看一个简单的例子PHP变长参数函数。

文件名:function-variable-length-argument.php

```php
<?php  
function add(...$numbers) {  
    $sum = 0;  
    foreach ($numbers as $n) {  
        $sum += $n;  
    }  
    return $sum;  
}  

echo add(1, 2, 3, 4);  
?>
```

```bash
php /var/www/html/function-variable-length-argument.php
```

URL预览:`{host0.http_url}function-variable-length-argument.php`