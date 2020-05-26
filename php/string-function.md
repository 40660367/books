# PHP 字符串函数

PHP提供了各种字符串函数来访问和操作字符串。 下面给出了重要的PHP字符串函数的列表。

## PHP strtolower()函数

`strtolower()`函数以小写字母返回字符串。

**语法**

```php
string strtolower ( string $string )
```

**示例**

文件名:string-function-strtolower.php

```php
<?php  
$str="I am a PHPer";  
$str=strtolower($str);  
echo $str;  
?>
```

```bash
php /var/www/html/string-function-strtolower.php
```

URL预览:`{host0.http_url}string-function-strtolower.php`

## PHP strtoupper()函数

`strtoupper()`函数以大写字母返回字符串。

**语法**

```php
string strtoupper ( string $string )
PHP
```

**示例**

文件名:string-function-strtoupper.php

```php
<?php  
$str="I am a PHPer"; 
$str=strtolower($str);  
echo $str;  
?>
```

```bash
php /var/www/html/string-function-strtoupper.php
```

URL预览:`{host0.http_url}string-function-strtoupper.php`

## PHP ucfirst()函数

`ucfirst()`函数返回将字符串的第一个字符转换为大写。 它不改变其他字符的大小写。

**示例**

文件名:string-function-ucfirst.php

```php
<?php  
$str="I am a PHPer"; 
$str=ucfirst($str);  
echo $str;  
?>
```

```bash
php /var/www/html/string-function-ucfirst.php
```

URL预览:`{host0.http_url}string-function-ucfirst.php`

## PHP lcfirst()函数

`lcfirst()`函数返回将第一个字符转换为小写的字符串。 它不改变其他字符的情况。

**语法**

```php
string lcfirst ( string $str )
```

**示例**

文件名:string-function-lcfirst.php

```php
<?php  
$str="I am a PHPer"; 
$str=lcfirst($str);  
echo $str;  
?>
```

```bash
php /var/www/html/string-function-lcfirst.php
```

URL预览:`{host0.http_url}string-function-lcfirst.php`

## PHP ucwords()函数

`ucwords()`函数返回将字符串每个单词的第一个字符转换为大写。

**语法**

```php
string ucwords ( string $str )
```

**示例**

文件名:string-function-ucwords.php

```php
<?php  
$str="my name is Allen Zhou";  
$str=ucwords($str);  
echo $str;  
?>
```

```bash
php /var/www/html/string-function-ucwords.php
```

URL预览:`{host0.http_url}string-function-ucwords.php`

## PHP strrev()函数

`strrev()`函数返回字符串反转的形式。

**语法**

```
string strrev ( string $string )
```

**示例**

文件名:string-function-strrev.php

```php
<?php  
$str="my name is Maxsu jaiswal";  
$str=strrev($str);  
echo $str;  
?>
```

```bash
php /var/www/html/string-function-strrev.php
```

URL预览:`{host0.http_url}string-function-strrev.php`

## PHP strlen()函数

`strlen()`函数返回字符串的长度。

**语法**

```
int strlen ( string $string )
```

**示例**

文件名:string-function-strlen.php

```php
<?php  
$str="my name is Max su";  
$len=strlen($str);  
echo $len;  
?>
```

```bash
php /var/www/html/string-function-strlen.php
```

URL预览:`{host0.http_url}string-function-strlen.php`