# Django 创建工程

现在我们已经安装了Django，让我们开始使用它。

 在Django中，每个要创建Web应用程序称为项目; 一个项目是应用程序的总和。应用程序是一组依托于MVC模式的代码文件。 作为例子，让我们要建立一个网站，该网站是我们的项目，论坛，新闻，联系方式的应用程序。 这种结构使得移动的项目之间的应用更容易，因为每一个应用程序都是独立的。 

## Django中创建工程，配置并访问

[Django环境安装](/setup.html)

### 创建项目 	 

无论您是在Windows或Linux，还在课程的在线环境。只是得到一个终端或一个命令提示符并导航至要创建项目的位置，然后执行下面的代码。

```bash
cd ~ && django-admin startproject myproject 
```

### 项目的目录结构

我们来查看这个文件夹

“myproject”文件夹是你的项目的容器，它实际上包含了两个元素：

- 		`manage.py` − 文件是一种项目本地`django-admin`通过命令行与项目交互(启动开发服务器，同步数据库...)。通过`manage.py`可以了解可使用的代码 

```bash
python3 ~/myproject/manage.py help
```

- 		 “myproject” 子目录中 − 此文件夹是项目的实际Python包。它包含四个文件:	
  - 				`__init__.py` − 只对于Python，处理这个文件夹的包。 				
  - 				`settings.py` − 正如名称所示，用于项目设置。 				
  - 				`urls.py` − 项目创建的各个环节和要调用的函数。项目的所有Toc。 				
  - 				`wsgi.py` − 如果需要部署项目在 WSGI 上。 				

###  设置项目

您的项目配置文件在`~/myproject/settings.py`。以下是可能需要设置一些重要的选项 

```bash
vim ~/myproject/myproject/settings.py
```

在我们创建的项目里修改`setting.py`文件

ALLOWED_HOSTS = ['\*']  ＃在`[]`里添加了`'*'`,代表接受任何外部主机的请求。

###  运行项目

现在，您的项目创建和配置，确保它能工作。

```bash
python3 ~/myproject/manage.py runserver 0.0.0.0:80
```

### 访问项目

使用浏览器打开:`{host0.http_url}`

![image-20200521170613588](./images/project.png)