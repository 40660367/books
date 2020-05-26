# PHP 函数

PHP函数是一段可以重复使用多次的代码。 它可以接受输入作为参数列表和返回值。 PHP中有成千上万的内置函数。

在PHP中，我们可以定义条件函数，函数内的函数和递归函数。

## PHP函数的优点

**代码重用性：**PHP函数只定义一次，可以多次调用，就像其他编程语言一样。

**使用更少的代码：** 它节省了大量代码，因为我们不需要多次重写逻辑。 通过使用函数，可以只写一次逻辑并重用它。

**易于理解：** PHP函数分离了编程逻辑。 因此，更容易理解应用程序的流程，因为每个逻辑都被划分为函数的形式。

## PHP用户定义函数

我们可以很容易地声明和调用用户定义的函数。下面来看看看声明用户定义函数的语法。

```php
function functionname(){  
    //code to be executed  
}
```

> **注意：**函数名必须以字母和下划线开头，与PHP中的其他标签(如：变量)一样。 它不能以数字或特殊符号开头。

执行上面代码结果如下

**PHP函数示例1**

![./setup.html](./images/env.png)文件名: function1.php

```php
<?php  
function sayHello(){  
echo "Hello PHP Function";  
}  
sayHello();//calling function  
?>
```

```bash
php /var/www/html/function1.php
```

URL预览:`{host0.http_url}function1.php`

## 函数参数

我们可以通过用逗号分隔的参数传递PHP函数中的信息。
PHP支持按值调用(默认)，通过引用调用，默认参数值和可变长度参数列表。

下面来看看看在PHP函数中传递单个参数的例子。
文件名:functionarg.php

```php
<?php  
function sayHello($name){  
    echo "Hello $name<br/>";  
}  
sayHello("MaxSu");  
sayHello("MinSu");  
sayHello("John");  
?>
```

```bash
php /var/www/html/functionarg.php
```

URL预览:`{host0.http_url}functionarg.php`

下面来看看看在PHP函数中传递两个参数的例子。

文件名:functionarg2.php

```php
<?php  
function sayHello($name,$age){  
echo "Hello $name, you are $age years old<br/>";  
}  
sayHello("Maxsu",27);  
sayHello("Minsu",26);  
sayHello("John",23);  
?>
```

```bash
php /var/www/html/functionarg2.php
```

URL预览:`{host0.http_url}functionarg2.php`

## PHP引用调用

传递给函数的值默认情况下不会修改实际值(通过值调用)。 但我们可以通过传递值作为参考(引用)。

默认情况下，传递给函数的值是通过值调用。 要传递值作为参考(引用)，您需要在参数名称前使用＆符号(&)。

下面来看看一个在PHP中通过引用调用的简单示例。

文件名:functionref.php

```php
<?php  
function adder(&$str2)  
{  
    $str2 .= 'Call By Reference';  
}  
$str = 'Hello ';  
adder($str);  
echo $str;  
?>
```

```bash
php /var/www/html/functionref.php
```

URL预览:`{host0.http_url}functionref.php`

## PHP函数：默认参数值

我们可以在函数中指定默认参数值。 在调用PHP函数时，如果不指定任何参数，它将采用默认参数。 下面来看看一个在PHP函数中使用默认参数值的简单示例。

文件名:functiondefaultarg.php

```php
<?php  
function sayHello($name="default_name"){  
    echo "Hello $name<br/>";  
}  
sayHello("maxsu");  
sayHello();//passing no value  
sayHello("John");  
?>
```

```bash
php /var/www/html/functiondefaultarg.php
```

URL预览:`{host0.http_url}functiondefaultarg.php`

## PHP函数：返回值

下面来看看一个有返回值的PHP函数的例子。

文件名:functionreturn.php

```php
<?php  
function cube($n){  
return $n*$n*$n;  
}  
echo "Cube of 3 is: ".cube(3);  
?>
```

```bash
php /var/www/html/functionreturn.php
```

URL预览:`{host0.http_url}functionreturn.php`