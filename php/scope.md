# PHP 变量作用域

变量的作用域是脚本中变量可被引用/使用的部分。

PHP 有四种不同的变量作用域：

- local
- global
- static
- parameter

## 局部和全局作用域

在所有函数外部定义的变量，拥有全局作用域。除了函数外，全局变量可以被脚本中的任何部分访问，要在一个函数中访问一个全局变量，需要使用 global 关键字。

在 PHP 函数内部声明的变量是局部变量，仅能在函数内部访问：

## 实例

文件名:scope.php

```php
<?php
$x=5; // 全局变量

function myTest()
{
  $y=10; // 局部变量
  echo "<p>测试函数内变量:<p>";
  echo "变量 x 为: $x";
  echo "<br>";
  echo "变量 y 为: $y";
} 

myTest();

echo "<p>测试函数外变量:<p>";
echo "变量 x 为: $x";
echo "<br>";
echo "变量 y 为: $y";
?>
```

```bash
php /var/www/html/scope.php
```

URL预览:`{host0.http_url}scope.php`

在以上实例中 myTest() 函数定义了 `$x` 和`$y`变量。 `$x` 变量在函数外声明，所以它是全局变量 ， `$y` 变量在函数内声明所以它是局部变量。

当我们调用myTest()函数并输出两个变量的值, 函数将会输出局部变量 `$y` 的值，但是不能输出 `$x` 的值，因为 `$x` 变量在函数外定义，无法在函数内使用，如果要在一个函数中访问一个全局变量，需要使用 global 关键字。

然后我们在myTest()函数外输出两个变量的值，函数将会输出全局变量 `$x` 的值，但是不能输出 `$y` 的值，因为 `$y` 变量在函数中定义，属于局部变量。

你可以在不同函数中使用相同的变量名称，因为这些函数内定义的变量名是局部变量，只作用于该函数内。


## PHP global 关键字

global 关键字用于函数内访问全局变量。

在函数内调用函数外定义的全局变量，我们需要在函数中的变量前加上 global 关键字：

## 实例

文件名:global.php

```php
<?php
$x=5;
$y=10;
 
function myTest()
{
    global $x,$y;
    $y=$x+$y;
}
 
myTest();
echo $y; // 输出 15
?>
```

```bash
php /var/www/html/global.php
```

URL预览:`{host0.http_url}global.php`

PHP 将所有全局变量存储在一个名为 $GLOBALS[*index*] 的数组中。 *index* 保存变量的名称。这个数组可以在函数内部访问，也可以直接用来更新全局变量。

## Static 作用域

当一个函数完成时，它的所有变量通常都会被删除。然而，有时候您希望某个局部变量不要被删除。

要做到这一点，请在您第一次声明变量时使用 **static** 关键字：

## 实例

文件名:static.php

```php
<?php
function myTest()
{
    static $x=0;
    echo $x;
    $x++;
    echo PHP_EOL;    // 换行符
}
 
myTest();
myTest();
myTest();
?>
```

```bash
php /var/www/html/static.php
```

URL预览:`{host0.http_url}static.php`

然后，每次调用该函数时，该变量将会保留着函数前一次被调用时的值。

**注释：**该变量仍然是函数的局部变量。

## 参数作用域

参数是通过调用代码将值传递给函数的局部变量。

参数是在参数列表中声明的，作为函数声明的一部分：

## 实例

文件名:parm-scope.php

```php
<?php
function myTest($x)
{
    echo $x;
}
myTest(5);
?>
```

```bash
php /var/www/html/parm-scope.php
```

URL预览:`{host0.http_url}parm-scope.php`