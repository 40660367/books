# PHP 注释

PHP注释可以用来描述任何代码行，以便其他开发人员可以很容易地理解代码。 它也可以用来隐藏任何代码。

PHP支持单行和多行注释。 这些注释类似于C/C++和Perl样式(Unix shell样式)注释。

## PHP单行注释

在PHP中使用单行注释有两种方式。

- `//`(C/C++ 风格单行注释)
- `＃`(Unix Shell风格单行注释)


文件名:comment1.php

```php
<?php  
// this is C++ style single line comment  
# this is Unix Shell style single line comment  
echo "Welcome to PHP single line comments";  
?>
```

## PHP多行注释

在PHP中，我们也可以注释多行。 为此，我们需要将所有行包含在`/*` 和 `*/`中。 下面来看看一个简单的PHP多行注释的例子。

文件名:comment2.php

```php
<?php  
/* 
Anything placed 
within comment 
will not be displayed 
on the browser; 
*/  
echo "Welcome to PHP multi line comment";  
?>
```

```bash
php /var/www/html/comment2.php
```

URL预览:`{host0.http_url}comment2.php`