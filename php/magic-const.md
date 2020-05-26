# PHP 魔术常量

魔术常数是PHP中的预定义常量，根据它们的使用而改变。 它们以双下划线(`__`)开头，以双下划线结尾。

它们类似于其他预定义的常量，但是它们随着上下文的改变而改变它们的值，它们被称为魔术常量。

下表中定义了八个魔法常量。 它们**不区分大小写**。

| 常量名称        | 描述                                                         |
| --------------- | ------------------------------------------------------------ |
| `__LINE__`      | 表示使用当前行号。                                           |
| `__FILE__`      | 表示文件的完整路径和文件名。 如果它在`include`中使用，则返回包含文件的名称。 |
| `__DIR__`       | 表示文件的完整目录路径。 等同于`dirname(__file__)`。 除非它是根目录，否则它没有尾部斜杠。 它还解析符号链接。 |
| `__FUNCTION__`  | 表示使用它的函数名称。如果它在任何函数之外使用，则它将返回空白。 |
| `__CLASS__`     | 表示使用它的函数名称。如果它在任何函数之外使用，则它将返回空白。 |
| `__TRAIT__`     | 表示使用它的特征名称。 如果它在任何函数之外使用，则它将返回空白。 它包括它被声明的命名空间。 |
| `__METHOD__`    | 表示使用它的类方法的名称。方法名称在有声明时返回。           |
| `__NAMESPACE__` | 表示当前命名空间的名称。                                     |

## 实例

下面来看看一个上面的每个魔法常量的例子。

文件名:magic.php

```php
<?php

    echo "<h1>Example for __LINE__</h1>";  
    echo "You are at line number " . __LINE__ . "<br><br>";// print Your current line number i.e;3  
    echo "<h3>Example for __FILE__</h3>";  
    echo __FILE__ . "<br><br>";//print full path of file with .php extension  
    echo "<h3>Example for __DIR__</h3>";  
    echo __DIR__ . "<br><br>";//print full path of directory where script will be placed  
    echo dirname(__FILE__) . "<br><br>"; //its output is equivalent to above one.  
    echo "<h3>Example for __FUNCTION__</h3>";  
    //Using magic constant inside function.  
    function cash(){  
        echo 'the function name is '. __FUNCTION__ . "<br><br>";//the function name is cash.  
    }  

    cash();  

    //Using magic constant outside function gives the blank output.  
    function test_function(){  
        echo 'HYIIII';  
    }  

    test_function();  
    echo  __FUNCTION__ . "<br><br>";//gives the blank output.  

    echo "<h3>Example for __CLASS__</h3>";  
    class abc  
    {  
        public function __construct() {  
            ;  
        }  

        function abc_method(){  
        echo __CLASS__ . "<br><br>";//print name of the class abc.  
        }  
    }  
    $t = new abc;  
    $t->abc_method(); 

    class first{  
        function test_first(){  
            echo __CLASS__;//will always print parent class which is first here.  
        }  
    }  

    class second extends first  
    {  
        public function __construct() {  
            ;  
        }  
    }  
    $t = new second;  
    $t->test_first();  

    echo "<h3>Example for __TRAIT__</h3>";  
    trait created_trait{  
        function abc(){  
            echo __TRAIT__;//will print name of the trait created_trait  
        }  
    }  

    class anew{  
        use created_trait;  
    }  
    $a = new anew;  
    $a->abc();  
    echo "<h3>Example for __METHOD__</h3>";  

    class meth{  
        public function __construct() {  
            echo __METHOD__ . "<br><br>";//print meth::__construct  
        }  
        public function meth_fun(){  
            echo __METHOD__;//print meth::meth_fun  
        }  
    }  
    $a = new meth;  
    $a->meth_fun();  

    echo "<h3>Example for __NAMESPACE__</h3>";  
    class name{  
        public function __construct() {  
            echo 'This line will be printed on calling namespace';  
        }  
    }  
    $clas_name= __NAMESPACE__ .'\name';  
    $a = new $clas_name;  

?>
```

```bash
php /var/www/html/magic.php
```

URL预览:`{host0.http_url}magic.php`