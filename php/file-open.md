# PHP 文件处理

PHP文件系统允许我们创建文件，逐行读取文件，逐个字符读取文件，写入文件，附加文件，删除文件和关闭文件。

## PHP打开文件 - fopen()函数

PHP `fopen()`函数用于打开文件。

**语法**

```php
resource fopen ( string $filename , string $mode [, bool $use_include_path = false [, resource $context ]] )
```

**示例**

文件名:file-fopen.php

```php
<?php  
$handle2 = fopen("/var/www/html/file-test.txt", "r");  
?>
```

## PHP关闭文件 - fclose()函数

PHP `fclose()`函数用于关闭打开的文件指针。

**语法**

```php
boolean fclose ( resource $handle )
```

**示例代码**

文件名:file-fclose.php

```php
<?php  
fclose($handle);  
?>
```

## PHP读取文件 - fread()函数

PHP `fread()`函数用于读取文件的内容。 它接受两个参数：资源和文件大小。

**语法**

```php
string fread ( resource $handle , int $length )
```

示例

文件名:file-read.php

```php
<?php    
$filename = "/var/www/html/file-test.txt";    
$handle = fopen($filename, "r");//open file in read mode    

$contents = fread($handle, filesize($filename));//read file    

echo $contents;//printing data of file  
fclose($handle);//close file    
?>
```

URL预览:`{host0.http_url}file-read.php`

## PHP写文件 - fwrite()函数

PHP `fwrite()`函数用于将字符串的内容写入文件。

**语法**

```php
int fwrite ( resource $handle , string $string [, int $length ] )
```

**示例**

文件名:file-write.php

```php
<?php  
$fp = fopen('data.txt', 'w');//open file in write mode  
fwrite($fp, 'hello ');  
fwrite($fp, 'php file');  
fclose($fp);  

echo "File written successfully";  
?>
```

URL预览:`{host0.http_url}file-write.php`

## PHP删除文件 - unlink()函数

PHP `unlink()`函数用于删除文件。

**语法**

```php
bool unlink ( string $filename [, resource $context ] )
```

**示例**

文件名:file-unlink.php

```php
<?php    
unlink('data.txt');  

echo "File deleted successfully";  
?>
```

```bash
php /var/www/html/file-uploader.php
```

