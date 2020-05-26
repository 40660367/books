# Nginx  示例1:修改默认服务目录及首页

 **示例1:**

```bash
cat /etc/nginx/sites-enabled/default 
```

在server段下看到

```
root /var/www/html;
```

这一行，就代表nginx安装后默认的web服务目录。

这里先不进行修改目录所在位置，先把默认首页进行替换。

Ningx默认首页是这样:

![image-20200415135139795](./images/nginx-welcome.png)

```bash
#制作自己的首页
echo 'My New Index Page' > /var/www/html/index.html
```

访问网址`{host0.http_url}`,就可以看到nginx的默认首页已经变成我们刚刚自定义的首页了。

