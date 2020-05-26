# PHP 语法

PHP 脚本在服务器上执行，然后将纯 HTML 结果发送回浏览器。

## 基本的 PHP 语法

PHP 脚本可以放在文档中的任何位置。

PHP 脚本以`<?php`开始，以`?>` 结束，例如

```php
<?php
// PHP 代码
?>
```

PHP 文件的默认文件扩展名是 ".php"。

PHP 文件通常包含 HTML 标签和一些 PHP 脚本代码。

## 实例:不含html的php脚本

文件名:echo.php

```php
<?php
echo "Hello World!";
?>
```

```bash
php /var/www/html/echo.php
```

URL预览:`{host0.http_url}echo.php`

## 实例:含html的php脚本

下面，我们提供了一个简单的 PHP 文件实例，它可以向浏览器输出文本 "Hello World!"：

文件名:helloworld.php

```php
<!DOCTYPE html>
<html>
<body>

<h1>My PHP page</h1>

<?php
echo "Hello World!";
?>

</body>
</html>
```

```bash
php /var/www/html/helloworld.php
```

URL预览:`{host0.http_url}helloworld.php`

PHP 中的每个代码行都必须以分号结束。分号是一种分隔符，用于把指令集区分开来。

通过 PHP，有两种在浏览器输出文本的基础指令：**echo** 和 **print**。

## PHP 中的注释

文件名:comment.php

```php
<!DOCTYPE html>
<html>
<body>

<?php
// 这是 PHP 单行注释

/*
这是
PHP 多行
注释
*/
?>

</body>
</html>
```

```bash
php /var/www/html/comment.php
```

URL预览:`{host0.http_url}comment.php`