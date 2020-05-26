# PHP print语句

类似于PHP `echo`语句，PHP `print`是一个语言结构(因为有返回值，可以认为它是函数)，所以也不需要使用括号和参数列表。 与`echo`不同，它总是返回`1`。

PHP `print`的语法如下：

```php
int print(string $arg)
```

PHP print语句可以用来打印字符串，多行字符串，转义字符，变量，数组等。

### 打印字符串

文件名:print1.php
```php
<?php  
    print "Hello by PHP print ";  
    print ("Hello by PHP print()");  
?>
```

```bash
php /var/www/html/print1.php
```

URL预览:`{host0.http_url}print1.php`

### 打印多行字符串

文件名:print2.php

```php
<?php  
print "Hello by PHP print  
this is multi line  
text printed by   
PHP print statement  
";  
?>
```

```bash
php /var/www/html/print2.php
```

URL预览:`{host0.http_url}print2.php`

### 打印转义字符

文件名:print3.php

```php
<?php  
    print "Hello escape \"sequence\" characters by PHP print";  
?>
```

```bash
php /var/www/html/print3.php
```

URL预览:`{host0.http_url}print3.php`

### 打印变量值

文件名:print4.php

```php
<?php  
    $msg="Hello print() in PHP";  
    print "Message is: $msg";   
?>
```

```bash
php /var/www/html/print4.php
```

URL预览:`{host0.http_url}print4.php`

