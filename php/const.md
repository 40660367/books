# PHP 常量

PHP常量是在执行脚本期间无法更改的名称或标识符。 PHP常量可以通过两种方式定义：

1. 使用 `define()` 函数定义
2. 使用 `const` 关键字定义

PHP常量遵循相同的PHP变量规则。 例如，它可以只用字母或下划线开始。通常，PHP常量应以大写字母定义。

## PHP常量：define()

下面来看看看PHP中的`define()`函数的语法。

```php
define(name, value, case-insensitive)
```

1. `name`：指定常量名称。
2. `value`：指定常量值。
3. `case-insensitive`：默认值为`false`。默认情况下区分大小写。

下面来看看看使用`define()`函数来定义PHP常量的例子。

文件名: constant1.php

```php
<?php  
    define("MESSAGE","Hello PHPer!");  
    echo MESSAGE;  
?>
```

```bash
php /var/www/html/constant1.php
```

URL预览:`{host0.http_url}constant1.php`

文件名: constant2.php

```php
<?php  
    define("MESSAGE","Hello PHPer",true);//not case sensitive  
    echo MESSAGE;  
    echo message;  
?>
```

```bash
php /var/www/html/constant2.php
```

URL预览:`{host0.http_url}constant2.php`

文件名: constant3.php

```php
<?php  
    define("MESSAGE","Hello PHPer",false);//case sensitive  
    echo MESSAGE;  
    echo message;  
?>
```

```bash
php /var/www/html/constant3.php
```

URL预览:`{host0.http_url}constant3.php`

## PHP常量：const关键字

`const`关键字在编译时定义常量。 它是一个语言构造不是一个函数。

它比`define()`快一点，因为它没有返回值。

它总是区分大小写的。

文件名: constan4.php

```php
<?php  
    const MESSAGE="Hello const by PHPer";  
    echo MESSAGE;  
?>
```

```bash
php /var/www/html/constant4.php
```

URL预览:`{host0.http_url}constant4.php`