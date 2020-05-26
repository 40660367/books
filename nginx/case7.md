# Nginx 示例7:设置FastCGI代理

nginx可用于将请求路由到运行使用各种框架和编程语言构建的应用程序的FastCGI服务器。
使用FastCGI服务器的最基本nginx配置包括使用`fastcgi_pass`指令(而不是`proxy_pass`指令)，以及`fastcgi_param`指令来设置传递给`FastCGI`服务器的参数。 

假设`FastCGI`服务器可以在`localhost:9000`上访问。 以上节的代理配置为基础，用`fastcgi_pass`指令替换`proxy_pass`指令，并将参数更改为`localhost:9000`。 在PHP中，`SCRIPT_FILENAME`参数用于确定脚本名称，`QUERY_STRING`参数用于传递请求参数。 最终的配置将是：

```
server {
    location / {
        fastcgi_pass  localhost:9000;
        fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
        fastcgi_param QUERY_STRING    $query_string;
    }
}
```

这将设置一个服务器，将除静态图像请求之外的所有请求路由到通过FastCGI协议在`localhost:9000`上运行的代理服务器。

**示例：**

```
location ~ \.php$ {
 fastcgi_pass unix:/var/run/php5-fpm.sock;
 fastcgi_index index.php;
 fastcgi_param SCRIPT_FILENAME $document_root$fastcgi_script_name;
 include fastcgi_params;
}
```





