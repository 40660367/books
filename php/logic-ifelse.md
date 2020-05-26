# PHP if/else语句

PHP `if else`语句用于测试条件。在PHP中有多种方法来使用`if`语句。

- if
- if-else
- if-else-if
- 嵌套if

## PHP if语句

如果条件(condition)为`true`，则执行PHP if语句块。

**语法**

```php
if(condition){  
    //code to be executed  
}
```

**示例** 

文件名:logic-if.php

```php
<?php  
    $num=12;  
    if($num<100){  
        echo "$num is less than 100";  
    }  
?>
```

```bash
php /var/www/html/logic-if.php
```

URL预览:`{host0.http_url}logic-if.php`

## PHP if-else语句

PHP if-else语句被执行时可同时条件是真或假。

**语法** 

```php
if(condition){  
    //code to be executed if true  
}else{  
    //code to be executed if false  
}
```

**示例**

文件名:logic-ifelse.php

```php
<?php  
    $num=12;  
    if($num%2==0){  
        echo "$num is even number";  
    }else{  
        echo "$num is odd number";  
    }  
?>
```

```bash
php /var/www/html/logic-ifelse.php
```

URL预览:`{host0.http_url}logic-ifelse.php`