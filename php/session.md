# PHP 会话Session

PHP会话(Session)用于临时存储和从一个页面传递信息到另一个页面(直到用户关闭网站)。

PHP会话技术广泛应用于购物网站，我们需要存储和传递购物车信息。 用户名，产品代码，产品名称，产品价格等信息从一个页面传递到另一个页面。

PHP会话为每个浏览器创建唯一的用户ID，以识别用户，并避免多个浏览器之间的冲突。

## PHP session_start()函数

PHP `session_start()`函数用于启动会话。 它启动一个新的或恢复现有会话。 如果已创建会话，则返回现有会话。 如果会话不可用，它将创建并返回新会话。

**语法**

```php
bool session_start ( void )
```

使用示例代码：

```php
session_start();
```

## PHP $_SESSION

PHP `$_SESSION`是一个包含所有会话变量的关联数组。 它用于设置和获取会话变量值。

**示例：存储信息**

```php
$_SESSION["user"] = "Minsu";
```

**示例：获取信息**

```php
$user = $_SESSION["user"];  
echo $user;
```

## PHP会话示例

文件名:session1.php

```php
<?php  
session_start();  
?>  
<html>  
<body>  
<?php  
$_SESSION["user"] = "Allen";  
echo "Session information are set successfully.<br/>";  
?>  
<a href="session2.php">Visit next page</a>  
</body>  
</html>
```

文件名:session2.php

```php
<?php  
session_start();  
?>  
<html>  
<body>  
<?php  
echo "User is: ".$_SESSION["user"];  
?>  
</body>  
</html>
```

URL预览:`{host0.http_url}session1.php`

## PHP会话计数器示例

文件名:sessioncounter.php

```php
<?php  
   session_start();  

   if (!isset($_SESSION['counter'])) {  
      $_SESSION['counter'] = 1;  
   } else {  
      $_SESSION['counter']++;  
   }  
   echo ("Page Views: ".$_SESSION['counter']);  
?>
```

URL预览:`{host0.http_url}sessioncounter.php`

## PHP销毁会话

PHP `session_destroy()`函数用于完全销毁所有会话变量。

文件名:session-destory.php

```php
<?php  
session_start();  
session_destroy();  
?>
```

URL预览:`{host0.http_url}session-destory.php`