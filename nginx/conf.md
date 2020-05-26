# Nginx 配置文件

## 配置文件的结构

nginx由配置文件中指定的指令控制的模块组成。 指令分为简单指令和块指令。 一个简单的指令由空格分隔的名称和参数组成，并以分号(`;`)结尾。 块指令具有与简单指令相同的结构，但不是以分号结尾，而是以大括号(`{`和`}`)包围的一组附加指令结束。 如果块指令可以在大括号内部有其他指令，则称为上下文(例如：`events`，`http`，`server`和`location`)。

配置文件中放置在任何上下文之外的伪指令都被认为是**主上下文**。 `events` 和`http`指令驻留在**主上下文**中，`server`在`http`中的，而`location`在`http`块中。

`#`号之后的一行的部分被视为注释。

## 配置文件组成：

main（全局设置）:main部分设置的指令将影响其它所有部分的设置；

server（主机设置）:server部分的指令主要用于指定虚拟主机域名、IP和端口；

upstream（上游服务器设置，主要为反向代理、负载均衡相关配置）:upstream的指令用于设置一系列的后端服务器，设置反向代理及后端服务器的负载均衡；

location（URL匹配特定位置后的设置），每部分包含若干个指令。:location部分用于匹配网页位置（比如，根目录“/”,“/images”,等等）。

他们之间的关系式：server继承main，location继承server；upstream既不会继承指令也不会被继承。它有自己的特殊指令，不需要在其他地方的应用。

## 配置文件位置：

```bash
cat /etc/nginx/sites-enabled/default
```

NGINX与其他服务类似，因为它具有以特定格式编写的基于文本的配置文件。 默认情况下，文件名为`nginx.conf`并放在`/etc/nginx`目录中(对于开源NGINX产品，位置取决于用于安装NGINX和操作系统的软件包系统，它通常位于`/usr/local/nginx/conf/etc/nginx`或`/usr/local/etc/nginx`。)

配置文件由指令及其参数组成。 简单(单行)指令各自以分号结尾。 其他指令作为“容器”，将相关指令组合在一起，将其包围在花括号(`{}`)中。 以下是简单指令的一些示例。

```conf
user             nobody;
error_log        logs/error.log notice;
worker_processes 1;
```

为了使配置更易于维护，建议您将其拆分为存储在`/etc/nginx/conf.d`目录中的一组功能特定文件，并在主`nginx.conf`文件中使用`include`指令引用(包函)指定文件的内容。如下所示 -

```conf
include conf.d/http;
include conf.d/stream;
include conf.d/exchange-enhanced;
```

几个顶级指令(称为上下文)将适用于不同流量类型的指令组合在一起：

- [events](http://nginx.org/en/docs/ngx_core_module.html?&_ga=1.10035445.1509956953.1490042234#events) – 一般连接处理
- [http](http://nginx.org/en/docs/http/ngx_http_core_module.html?&_ga=1.10035445.1509956953.1490042234#http) – HTTP协议流量
- [mail](http://nginx.org/en/docs/mail/ngx_mail_core_module.html?&_ga=1.85614937.1509956953.1490042234#mail) – Mail协议流量
- [stream](http://nginx.org/en/docs/stream/ngx_stream_core_module.html?&_ga=1.85614937.1509956953.1490042234#stream) – TCP协议流量

指定在这些上下文之外的指令是在主上下文中。
在每个流量处理上下文中，可包括一个或多个服务器上下文来定义控制请求处理的虚拟服务器。 您可以在服务器环境中包含的指令根据流量类型而有所不同。

对于HTTP流量(http上下文)，每个服务器指令控制对特定域或IP地址上的资源请求的处理。 服务器上下文中的一个或多个位置上下文定义了如何处理特定的URI集合。

对于邮件和TCP流量(`mail` 和 `stream` 上下文)，服务器指令各自控制到达特定TCP端口或UNIX套接字的流量处理。

以下配置说明了上下文的使用情况。

```conf
user nobody; # a directive in the 'main' context

events {
    # configuration of connection processing
}

http {

    # Configuration specific to HTTP and affecting all virtual servers

    server {
        # configuration of HTTP virtual server 1

        location /one {
            # configuration for processing URIs with '/one'
        }

        location /two {
            # configuration for processing URIs with '/two'
        }
    }

    server {
        # configuration of HTTP virtual server 2
    }
}

stream {
    # Configuration specific to TCP and affecting all virtual servers

    server {
        # configuration of TCP virtual server 1 
    }
}
```

对于大多数指令，在另一个上下文(子上下文)中定义的上下文将继承父级中包含的伪指令的值。 要覆盖从父进程继承的值，请在子上下文中包含该指令。 有关上下文遗留的更多信息，请参阅[proxy_set_header](http://nginx.org/en/docs/http/ngx_http_proxy_module.html?&_ga=1.110839877.1509956953.1490042234#proxy_set_header)伪指令的文档。

要更改配置文件才能生效，NGINX必须重新加载该文件。可以重新启动nginx进程或发送`reload`信号来升级配置，而不会中断当前请求的处理。