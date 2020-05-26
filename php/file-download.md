# PHP 下载文件

在PHP中，可使用内置的`readfile()`函数来实现文件下载。 `readfile()`函数读取一个文件并将其写入输出缓冲区。

## PHP readfile()函数

**语法**

```php
int readfile ( string $filename [, bool $use_include_path = false [, resource $context ]] )
```

- `$filename`：表示文件名
- `$use_include_path`：它是可选参数。它默认为`false`。可以将其设置为`true`以搜索`included_path`中的文件。
- `$context`：表示上下文流资源。
- `int`：它返回从文件读取的字节数。

## PHP下载文件示例：文本文件

使用示例提供的文本文件:`file-test.txt`

文件名: file-download.php

```php
<?php  
$file_url = 'http://yourdynamicenv.url/file-test.txt';  
header('Content-Type: application/octet-stream');  
header("Content-Transfer-Encoding: utf-8");   
header("Content-disposition: attachment; filename=\"" . basename($file_url) . "\"");   
readfile($file_url);  
?>
```

```bash
php /var/www/html/file-download.php
```

URL预览:`{host0.http_url}file-download.php`