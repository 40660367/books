# Nginx 示例3:传递请求标头proxy_set_header

默认情况下，NGINX在代理请求`“Host”` 和 `“Connection”`中重新定义了两个头字段，并消除了其值为空字符串的头字段。 “Host”设置为`$proxy_host`变量，`“Connection”`设置为关闭(`close`)。

要更改这些设置，以及修改其他`header`字段，请使用`proxy_set_header`指令。 该指令可以在一个或多个位置(`location`)指定。 它也可以在特定的`server`上下文或`http`块中指定。 例如：

```conf
location /path/ {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_pass http://localhost:8000;
}
```

在此配置中，`“Host”`字段设置为 [$host](http://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=1.51463017.1509956953.1490042234#variables) 变量。
为了防止头域被传递给代理服务器，可以将其设置为空字符串，如下所示：

```conf
location /path/ {
    proxy_set_header Accept-Encoding "";
    proxy_pass http://localhost:8000;
}
```

## 示例

```bash
vim /etc/nginx/sites-enabled/default 
```

在server段下添加一个新的location如下后保存退出

```conf
location /with-header {
    proxy_set_header Host $host;
    proxy_set_header X-Real-IP $remote_addr;
    proxy_pass http://localhost:8000;
}
location /with-noheader {
    proxy_set_header Accept-Encoding "";
    proxy_pass http://localhost:8000;
}
```

```bash
#重载nginx
nginx -s reload
```

```bash
cd ~ && mkdir -p with-header with-noheader
#制作首页
echo 'This is Python3 Web Server' > ~/pythonproxy/index.html
#启动Python Web服务器
python3 -m http.server
```

访问网址`{host0.http_url}with-header` 与 `{host0.http_url}with-noheader`比较区别
