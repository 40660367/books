# PHP 参数化函数

PHP参数化函数是带有参数的函数。 您可以在函数中传递任意数量的参数。 这些传递的参数作为函数中的变量。

它们在函数名称之后，在括号内指定。输出取决于作为参数传递到函数中的动态值。

## PHP参数化示例1

**加减法**

在这个例子中，我们在两个函数`add()`和`sub()`中传递了两个参数`$x`和`$y`。
文件名:para1.php

```php
<!DOCTYPE html>
<html lang="zh">
<head>
    <meta charset="utf-8" />
    <title>参数加法和减法示例</title>  
</head>  
<body>  
<?php  
        //Adding two numbers  
         function add($x, $y) {  
            $sum = $x + $y;  
            echo "Sum of two numbers is = $sum <br><br>";  
         }   
         add(300, 700);  

         //Subtracting two numbers  
         function sub($x, $y) {  
            $diff = $x - $y;  
            echo "Difference between two numbers is = $diff";  
         }   
         sub(1000, 500);  
      ?>  
</body>  
</html>
```

```bash
php /var/www/html/para1.php
```

URL预览:`{host0.http_url}para1.php`

## PHP参数化示例2

**动态数字的加法和减法**

在这个例子中，我们在两个函数`add()`和`sub()`中传递了两个参数`$x`和`$y`。
*文件：para2.php*

```php
<?php  
//add() function with two parameter  
function add($x,$y)    
{  
    $sum=$x+$y;  
    echo "Sum = $sum <br><br>";  
}  
//sub() function with two parameter  
function sub($x,$y)    
{  
    $sub=$x-$y;  
    echo "Diff = $sub <br><br>";  
}  
//call function, get  two argument through input box and click on add or sub button  
if(isset($_POST['add']))  
{  
    //call add() function  
     add($_POST['first'],$_POST['second']);  
}     
if(isset($_POST['sub']))  
{  
    //call add() function  
    sub($_POST['first'],$_POST['second']);  
}  
?>  
<form method="post">  
Enter first number: <input type="number" name="first"/><br><br>  
Enter second number: <input type="number" name="second"/><br><br>  
<input type="submit" name="add" value="ADDITION"/>  
<input type="submit" name="sub" value="SUBTRACTION"/>  
</form>
```

```bash
php /var/www/html/para2.php
```

URL预览:`{host0.http_url}para2.php`