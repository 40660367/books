# PHP echo语句

PHP `echo`是一个语言结构(也可以叫作语句)，不是一个函数，所以不需要使用括号。 但是如果要使用多个参数，则需要使用括号。

PHP `echo`的语法如下：

```php
void echo ( string $arg1 [, string $... ] )
```

PHP的`echo`语句可以用来打印字符串，多行字符串，转义字符，变量，数组等。

### 打印字符串

文件名：echo1.php

```php
<?php  
    echo "Hello by PHP echo";  
?>
```

```bash
php /var/www/html/echo1.php
```

URL预览:`{host0.http_url}echo1.php`

### 打印多行字符串

文件名: echo2.php

```php
<?php  
echo "Hello by PHP echo  
this is multi line  
text printed by   
PHP echo statement  
";  
?>
```

```bash
php /var/www/html/echo2.php
```

URL预览:`{host0.http_url}echo2.php`

### 打印转义字符

文件名: echo3.php

```php
<?php  
    echo "Hello escape \"sequence\" characters";  
?>
```

```bash
php /var/www/html/echo3.php
```

URL预览:`{host0.http_url}echo3.php`

### 打印变量值

文件名:echo4.php

```php
<?php  
    $msg="Hello PHPer!";  
    echo "Message is: $msg";    
?>
```

```bash
php /var/www/html/echo4.php
```

URL预览:`{host0.http_url}echo4.php`