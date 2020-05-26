# PHP 字符串

PHP字符串是一系列字符，即用于存储和处理文本。 在PHP中有`4`种方法可用于指定字符串。

1. 单引号
2. 双引号
3. heredoc语法
4. newdoc语法(自PHP 5.3起)

## 单引号PHP字符串

我们可以通过在单引号中包含文本在PHP中创建一个字符串。 这是在PHP中指定字符串的最简单的方法。如下一个示例 -

文件名:string-single.php

```php
<?php  
$str='Hello text within single quote';  
echo $str;  
?>
```

```bash
php /var/www/html/string-single.php
```

URL预览:`{host0.http_url}string-single.php`

我们可以在单个引用的PHP字符串中存储多行文本，特殊字符和转义序列。

文件名:string-multiple.php

```php
<?php  
$str1='Hello text   
multiple line  
text within single quoted string';  
$str2='Using double "quote" directly inside single quoted string';  
$str3='Using escape sequences \n in single quoted string';  
echo "$str1 <br/> $str2 <br/> $str3";  
?>
```

```bash
php /var/www/html/string-multiple.php
```

URL预览:`{host0.http_url}string-multiple.php`

输出结果如下 -

> **注意：**在单引号PHP字符串中，大多数转义序列和变量不会被解释。 可以使用单引号`\'`反斜杠和通过`\\`在单引号引用PHP字符串。

文件名:string-escape1.php

```php
<?php  
$num1=10;   
$str1='trying variable $num1';  
$str2='trying backslash n and backslash t inside single quoted string \n \t';  
$str3='Using single quote \'my quote\' and \\backslash';  
echo "$str1 <br/> $str2 <br/> $str3";  
?>
```

```bash
php /var/www/html/string-escape1.php
```

URL预览:`{host0.http_url}string-multiple.php`

## 双引号PHP字符串

在PHP中，我们可以通过在双引号中包含文本来指定字符串。 但转义序列和变量将使用双引号PHP字符串进行解释。

文件名:string-doublequote1.php

```php
<?php  
$str="Hello text within double quote";  
echo $str;  
?>
```

```bash
php /var/www/html/string-doublequote1.php
```

URL预览:`{host0.http_url}string-doublequote1.php`



现在，不能使用双引号直接在双引号字符串内。

文件名:string-doublequote2.php

```php
<?php  
$str1="Using double "quote" directly inside double quoted string";  
echo $str1;  
?>
```

```bash
#注意看报错信息
php /var/www/html/string-doublequote2.php
```



我们可以在双引号的PHP字符串中存储多行文本，特殊字符和转义序列。参考如下代码 -

文件名:string-doublequote3.php

```php
<?php  
$str1="Hello text   
multiple line  
text within double quoted string";  
$str2="Using double \"quote\" with backslash inside double quoted string";  
$str3="Using escape sequences \n in double quoted string";  
echo "$str1 <br/> $str2 <br/> $str3";  
?>
```

```bash
php /var/www/html/string-doublequote3.php
```

URL预览:`{host0.http_url}string-doublequote3.php`



在双引号字符串中，变量将会被解释，这是因为我们对特殊字符进行了转义。

文件名:string-escape2.php

```php
<?php  
$num1=10;   
echo "Number is: $num1";  
?>
```

```bash
php /var/www/html/string-escape2.php
```

URL预览:`{host0.http_url}string-escape2.php`