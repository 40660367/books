# PHP 变量

PHP中的变量是保存数据的内存位置的名称。 变量是用于保存临时数据的临时存储。

在PHP中，使用`$`符号和变量名来声明变量。

在PHP中声明变量的语法如下：

```php
$variablename = value;
```

变量可以是很短的名称（如 x 和 y）或者更具描述性的名称（如 age、carname、totalvolume）。

PHP 变量规则：

- 变量以 $ 符号开始，后面跟着变量的名称
- 变量名必须以字母或者下划线字符开始
- 变量名只能包含字母数字字符以及下划线（A-z、0-9 和 _ ）
- 变量名不能包含空格
- 变量名是区分大小写的（`$y` 和 `$Y` 是两个不同的变量）
PHP 语句和 PHP 变量都是区分大小写的。


## 创建（声明）PHP 变量

PHP 没有声明变量的命令。

变量在您第一次赋值给它的时候被创建：

## PHP 是一门弱类型语言

在上面的实例中，我们注意到，不必向 PHP 声明该变量的数据类型。

PHP 会根据变量的值，自动把变量转换为正确的数据类型。

在强类型的编程语言中，我们必须在使用变量前先声明（定义）变量的类型和名称。

## PHP变量：声明字符串，整数和浮点数变量

下面来看看看如何在PHP变量中声明字符串，整数和浮点值的例子。

文件名:variable1.php

```php
<?php  
    $str="hello string";  
    $x=200;  
    $y=44.6;  
    echo "string is: $str <br/>";  
    echo "integer is: $x <br/>";  
    echo "float is: $y <br/>";  
?>
```

```bash
php /var/www/html/variable1.php
```

URL预览:`{host0.http_url}variable1.php`

## PHP变量：两个变量的总和

文件名:variable2.php

```php
<?php  
    $x=5;  
    $y=6;  
    $z=$x+$y;  
    echo $z;  
?>
```

```bash
php /var/www/html/variable2.php
```

URL预览:`{host0.http_url}variable2.php`

## PHP变量：区分大小写

在PHP中，变量名称是区分大小写的。 因此，变量名称“`color`”不同于”`Color`“，”`COLOR`“等。

文件名:variable3.php

```php
<?php  
    $color="red";  
    echo "My car is " . $color . "<br>";  
    echo "My house is " . $COLOR . "<br>";  
    echo "My boat is " . $coLOR . "<br>";  
?>
```

```bash
php /var/www/html/variable3.php
```

URL预览:`{host0.http_url}variable3.php`



## PHP变量：规则

PHP变量必须以字母或下划线开头。PHP变量不能以数字和特殊符号开头。

文件名:variablevalid.php

```php
<?php  
    $a="hello";//letter (valid)  
    $_b="hello";//underscore (valid)  

    echo "$a <br/> $_b";  
?>
```

```bash
php /var/www/html/variablevalid.php
```

URL预览:`{host0.http_url}variablevalid.php`



文件名:variableinvalid.php

```php
<?php  
    $2a="hello";// (invalid)  
    echo "$a <br/>;
?>
```

```bash
php /var/www/html/variableinvalid.php
```

URL预览:`{host0.http_url}variableinvalid.php