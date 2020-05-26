# PHP 上传文件

在PHP中，只需要通过几行代码，就能完成上传单个和多个文件的处理。

PHP文件上传功能允许上传二进制和文本文件。 此外，您可以通过PHP身份验证和文件操作功能完全控制要上传的文件。

## PHP $_FILES

PHP全局`$_FILES`包含文件的所有信息。 在`$_FILES`全局变量的帮助下，我们可以得到文件名，文件类型，文件大小，临时文件名和与文件相关的错误。

这里，我们假设文件名是`filename`。请参考下表 -

| 变量名称                          | 描述                                   |
| --------------------------------- | -------------------------------------- |
| `$_FILES['filename']['name']`     | 返回文件名称                           |
| `$_FILES['filename']['type']`     | 返回文件的MIME类型                     |
| `$_FILES['filename']['size']`     | 返回文件的大小(以字节为单位)           |
| `$_FILES['filename']['tmp_name']` | 返回存储在服务器上的文件的临时文件名。 |
| `$_FILES['filename']['error']`    | 返回与此文件相关联的错误代码。         |

## move_uploaded_file()函数

`move_uploaded_file()`函数将上传的文件移动到新位置。 `move_uploaded_file()`函数在内部检查文件是否通过`POST`请求上传。 如果文件是通过`POST`请求上传的，它将移动文件。

**语法**

```php
bool move_uploaded_file ( string $filename , string $destination )
```

## PHP文件上传示例

文件名：file-uploadform.html

```php
<form action="file-uploader.php" method="post" enctype="multipart/form-data">  
    选择上传的文件:  
    <input type="file" name="fileToUpload"/>  
    <input type="submit" value="Upload Image" name="submit"/>  
</form>
```

> 注意：上面代码中，一定要在 `` 标签中添加 `enctype="multipart/form-data"`属性，否则PHP代码无法获取上传的文件内容。

文件名:file-uploader.php

```php
<?php  
$target_path = "/var/www/html/";  
$target_path = $target_path.basename( $_FILES['fileToUpload']['name']);   

if(move_uploaded_file($_FILES['fileToUpload']['tmp_name'], $target_path)) {  
    echo "File uploaded successfully!";  
} else{  
    echo "Sorry, file not uploaded, please try again!";  
}  
```

```bash
php /var/www/html/file-uploader.php
```

URL预览:`{host0.http_url}file-uploader.php`