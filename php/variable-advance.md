# PHP $和$$变量

$var(一个美元)是一个正常变量，名称为：`var`，存储任何值，如：string，integer，float等。

$$var(两个美元)是一个引用变量，用于存储`$var`的值。

为了更好地理解`$`和`$$`之间的区别，下面来看看一些例子。

## 示例1

文件名: example1.php

```php
<?php  
    $x = "abc";  
    $$x = 200;  
    echo $x."<br/>";  
    echo $$x."<br/>";  
    echo $abc;  
?>
```

在上面的例子中，我们为变量`x`赋值为：”`abc`“。引用变量`$$x`的值分配为`200`。
现在我们打印出变量：`$x`，`$$x`和`$abc`。由此可以看出：`$$x`和`$abc`的值是相同的，即：因为 `$x`的值为”`abc`“，所以 `$$x`(`${$x｝`)计算后为`$abc`。

```bash
php /var/www/html/example1.php
```

URL预览:`{host0.http_url}example1.php`

## 示例2

文件名: example2.php

```php
<?php  
    $x="U.P";  
    $$x="Lucknow";  
    echo $x. "<br>";  
    echo $$x. "<br>";  
    echo "Capital of $x is " . $$x;  
?>
```

在上面的例子中，我们为变量`x`赋值一个值：”`U.P`“ ， 引用变量`$$x`的值被指定为`Lucknow`。

现在我们打印了：`$x`，`$$x`值和一个字符串。

```bash
php /var/www/html/example2.php
```

URL预览:`{host0.http_url}example2.php`

## 示例3

文件名: example3.php

```php
<?php  
    $name="Cat";  
    ${$name}="Dog";  // => $Cat = "Dog"
    ${${$name}}="Monkey";  // => $Cat = "Monkey"
    echo $name. "<br>";  
    echo ${$name}. "<br>";  
    echo $Cat. "<br>";  
    echo ${${$name}}. "<br>";  
    echo $Dog. "<br>";  
?>
```

在上面的例子中，我们为变量：`Cat`指定了一个值。 引用变量`${$name}`分配一个值：”`Dog`“， `${${$name}}`分配一个值：”`Monkey`“ 。

现在我们将打印 `$name`，`${$name}`，`$Cat`，`${${$name}}`和`$Dog`的值。

```bash
php /var/www/html/example3.php
```

URL预览:`{host0.http_url}example3.php`