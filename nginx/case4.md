# Nginx 示例4:压缩和解压gzip 

在这篇文章中，涉及内容如下 -

1. 压缩和解压缩介绍
2. 启用压缩
3. 启用解压缩
4. 发送压缩文件

## 压缩和解压缩介绍

压缩响应通常会显着减少传输数据的大小。 然而，由于压缩在运行时发生，它还可以增加相当大的处理开销，这会对性能产生负面影响 在向客户端发送响应之前，NGINX会执行压缩，但不会“压缩”已压缩的响应(例如，由代理的服务器)。

## 启用压缩

要启用压缩，请使用包含[gzip](http://nginx.org/en/docs/http/ngx_http_gzip_module.html?&_ga=1.107694530.1509956953.1490042234#gzip)指令并指定`on`值。

```conf
gzip on;
```

默认情况下，NGINX仅使用MIME类型`text/html`压缩响应。要使用其他MIME类型压缩响应，请包含`gzip_types`指令并列出其他类型。

```conf
gzip_types text/plain application/xml;
```

要指定要压缩的响应的最小长度，请使用[gzip_min_length](http://nginx.org/en/docs/http/ngx_http_gzip_module.html?&_ga=1.257108299.1509956953.1490042234#gzip_min_length)指令。 默认值为`20`字节(可将此处调整为`1000`)：

```conf
gzip_min_length 1000;
```

默认情况下，NGINX不会压缩对代理请求的响应(来自代理服务器的请求)。 请求来自代理服务器的事实由请求中Via头字段的存在确定。 要配置这些响应的压缩，请使用[gzip_proxied](http://nginx.org/en/docs/http/ngx_http_gzip_module.html?&_ga=1.10560372.1509956953.1490042234#gzip_proxied)指令。 该指令具有多个参数，指定NGINX应压缩哪种代理请求。例如，仅对不会在代理服务器上缓存的请求压缩响应是合理的。 为此，`gzip_proxied`指令具有指示NGINX在响应中检查`Cache-Control`头字段的参数，如果值为`no-cache`, `no-store` 或 `private`，则压缩响应。 另外，您必须包括 `Expires` 参数以用来检查`Expires`头域的值。 这些参数在以下示例中与`auth`参数一起设置，该参数检查`Authorization`头字段的存在(授权响应特定于最终用户，并且通常不被缓存)：

```conf
gzip_proxied no-cache no-store private expired auth;
```

与大多数其他指令一样，配置压缩的指令可以包含在`http`上下文中，也可以包含在 `server` 或 `location` 配置块中。

`gzip`压缩的整体配置可能如下所示。

```conf
server {
    gzip on;
    gzip_types      text/plain application/xml;
    gzip_proxied    no-cache no-store private expired auth;
    gzip_min_length 1000;
    ...
}
```

## 启用解压缩

某些客户端不支持使用`gzip`编码方法的响应。 同时，可能需要存储压缩数据，或者即时压缩响应并将它们存储在缓存中。 为了成功地服务于不接受压缩数据的客户端，NGINX可以在将数据发送到后一种类型的客户端时即时解压缩数据。

要启用运行时解压缩，请使用`gunzip`指令。

```conf
location /storage/ {
    gunzip on;
    ...
}
```

`gunzip`指令可以在与`gzip`指令相同的上下文中指定：

```conf
server {
    gzip on;
    gzip_min_length 1000;
    gunzip on;
    ...
}
```

请注意，此指令在单独的模块中定义，默认情况下可能不包含在开源NGINX构建中。

## 发送压缩文件

要将文件的压缩版本发送到客户端而不是常规文件，请在适当的上下文中将`gzip_static`指令设置为`on`。

```conf
location / {
    gzip_static on;
}
```

在这种情况下，为了服务`/path/to/file`的请求，NGINX尝试查找并发送文件`/path/to/file.gz`。 如果文件不存在，或客户端不支持`gzip`，则NGINX将发送未压缩版本的文件。

请注意，`gzip_static`指令不启用即时压缩。它只是使用压缩工具预先压缩的文件。要在运行时即时压缩内容(而不仅仅是静态内容)，请使用`gzip`指令。

该指令在单独的模块中定义，默认情况下可能不包含在开源NGINX构建中。