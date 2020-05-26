# PHP 环境安装及配置
## 本课程在线环境的安装

### 安装PHP解析器,Apache2服务器

```bash
#更新源并安装php解释器，以及apache服务器
apt update && apt-get install php apache2 -y


#启动apache服务
service apache2 start
```
```shell
#apache2服务相关说明
查看状态： service apache2 status/start/stop/restart
Web目录： /var/www/html/
安装目录： /etc/apache2/
全局配置： /etc/apache2/apache2.conf
监听端口： /etc/apache2/ports.conf
虚拟主机： /etc/apache2/sites-enabled/000-default.conf
```

### 解析测试

**制作php探针文件**

```bash
cat > /var/www/html/env.php <<EOF
<?php echo phpinfo();?>
EOF
```

***PHP解析测试***

```bash
#使用php解释器解析该探针文件
php /var/www/html/env.php
```

***apache2服务器解析测试***

点击`{host0.http_url}env.php`查看由apache2解析的php探针文件。

### 复制课程案例至目录

```bash
cp -r /share/lesson/php/* /var/www/html/
```

### 配置成功

到此我们已经成功安装了php解释器，apache web服务器并启动了服务，还导入了课程学习所需要的示例文件，您就可以开始进行本课程下一步的学习了。

**注：当云环境的生命周期失效后，需要重新进行安装。**