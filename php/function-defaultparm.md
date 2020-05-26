# PHP 带默认参数值函数

PHP允许您定义C++样式的默认参数值。 在这种情况下，如果不传递任何值到函数，它将使用默认参数值。

下面来看看看在PHP函数中使用默认参数的简单例子。



## 实例1 ![./setup.html](./images/env.png)

文件名:function-defaultparm1.php

```php
<?php  
function sayHello($name="Ram"){  
echo "Hello $name<br/>";  
}  
sayHello("Maxsu");  
sayHello();//passing no value  
sayHello("Vimsu");  
?>
```

> **提示：** 从PHP 5开始，可以使用默认参数值的概念，也可以通过引用调用。

```bash
php /var/www/html/function-defaultparm1.php
```

URL预览:`{host0.http_url}function-defaultparm1.php`

## 实例2 ![./setup.html](./images/env.png)

![./setup.html](./images/env.png)文件名:function-defaultparm2.php

```php
<?php    
function greeting($first="Max",$last="su"){    
    echo "Greeting: $first $last<br/>";    
}    
greeting();  
greeting("Min");  
greeting("Michael","Clark");  
?>
```

```bash
php /var/www/html/function-defaultparm2.php
```

URL预览:`{host0.http_url}function-defaultparm2.php`

## 实例3 ![./setup.html](./images/env.png)

文件名:function-defaultparm3.php

```php
<?php  
function add($n1=10,$n2=10){  
    $n3=$n1+$n2;  
    echo "Addition is: $n3<br/>";  
}  
add();  
add(20);  
add(40,40);  
?>  
```

```bash
php /var/www/html/function-defaultparm3.php
```

URL预览:`{host0.http_url}function-defaultparm3.php`