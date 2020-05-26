# Nginx 示例6:重写URI请求(rewrite)

可以通过使用`rewrite`指令在请求处理期间多次修改请求URI，该指令具有一个可选参数和两个必需参数。 第一个(必需)参数是请求URI必须匹配的正则表达式。 第二个参数是用于替换匹配URI的URI。 可选的第三个参数是可以停止进一步重写指令的处理或发送重定向(代码`301`或`302`)的标志。例如：

```conf
location /users/ {
    rewrite ^/users/(.*)$ /show?user=$1 break;
}
```

如该示例所示，用户通过匹配正则表达式捕获第二个参数。

您可以在`location` 和 `server`上下文中包含多个`rewrite`指令。 NGINX按照它们发生的顺序逐个执行指令。 当选择该上下文时，`server`上下文中的`rewrite`指令将被执行一次。
在NGINX处理一组`rewrite`指令之后，它根据新的URI选择一个`location`上下文。 如果所选`location`块包含`rewrite`指令，则依次执行它们。 如果URI与其中任何一个匹配，则在处理所有定义的`rewrite`指令之后，将搜索新`location`块。

以下示例显示了与返回指令相结合的`rewrite`指令。

```conf
server {
    ...
    rewrite ^(/download/.*)/media/(.*)\..*$ $1/mp3/$2.mp3 last;
    rewrite ^(/download/.*)/audio/(.*)\..*$ $1/mp3/$2.ra  last;
    return  403;
    ...
}
```

此示例配置区分两组URI。 诸如`/download/some/media/file`之类的URI更改为`/download/some/mp3/file.mp3`。由于最后一个标志，所以跳过后续指令(第二次`rewrite`和`return`指令)，但NGINX继续处理该请求，该请求现在具有不同的URI。类似地，诸如`/download/some/audio/file`的URI被替换为`/download/some/mp3/file.ra`。 如果URI与`rewrite`指令不匹配，则NGINX将`403`错误代码返回给客户端。

有两个中断处理重写指令的参数：

- `last` - 停止执行当前服务器或位置上下文中的重写指令，但是NGINX会搜索与重写的URI匹配的位置，并且应用新位置中的任何重写指令(URI可以再次更改，往下继续匹配)。
- `break` - 像`break`指令一样，在当前上下文中停止处理重写指令，并取消搜索与新URI匹配的位置。新位置(`location`)块中的`rewrite`指令不执行。

## 示例：将多级路径的文件映射为一个文件，以增强seo效果

实现效果：将访问URL：news-2020-04-13-123.html  映射为   /news/2020/04/13/123.html

```bash
#创建测试文件
mkdir -p /var/www/html/news/2020/04/13/
echo 123news.html > /var/www/html/news/2020/04/13/123.html
```

**修改配置文件`/etc/nginx/sites-enabled/default `**

```bash
vim /etc/nginx/sites-enabled/default
```
在location块内添加
```conf
rewrite ^/news-([0-9]+)-([0-9]+)-([0-9]+)-([0-9]+)\.html$ /news/$1/$2/$3/$4.html last;
```

**重载nginx**

```bash
nginx -s reload
```

**验证:**

打开`{host0.http_url}news-2020-04-13-123.html `

## 示例：目录对换

实现效果：/news/2020 => /2020/news

```bash
#创建测试文件
mkdir -p /var/www/html/2020/news
echo index.html > /var/www/html/2020/news/index.html
```

**修改配置文件`/etc/nginx/sites-enabled/default `**

```bash
vim /etc/nginx/sites-enabled/default
```

在location块内添加

```
rewrite ^/(.+)/(\d+) /$2/$1 last;
```

**重载nginx**

```bash
nginx -s reload
```

**验证:**

打开`{host0.http_url}news/2020`



## 以下案例请自行配置练习：

**二级域名和目录转成参数**

abc.domian.com/sort/2 => abc.domian.com/abc/2.html

```
if ($host ~* (.*)\.freeaihub\.cn) {
set $sub_name $1;
rewrite ^/sort\/(\d+)\/?$ /$sub_name/$1.html last;
}
```

**三级域名跳转**

```
if ($http_host ~* “^(.*)\.i\.c1gstudio\.com$”) {

rewrite ^(.*) http://top.88dgw.com$1/;

break;
}
```

**目录自动加“/”**

```
if` `(-d ``$request_filename``){``rewrite ^/(.*)([^/])$ http:``//$host/$1$2/ permanent;``}
```

