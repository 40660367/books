# Django 应用程序app		

一个项目是许多应用的总和。每个应用程序有一个客观并可重复使用到另一个项目，像在网站上的联系表单可以是一个应用程序，并且可以重复使用到其它应用。看到它作为项目的一个模块。 

## 创建并使用Django应用程序

[环境准备](./setup.html)及[项目初始化准备](./project.html)

### 创建应用程序app1

我们假设在项目文件夹。在我们有主项目“myproject”文件夹，并在一级文件夹有一个文件：manage.py ，执行以下命令

```bash
cd ~/myproject && python3 ~/myproject/manage.py startapp app1 
```

### 浏览应用程序目录

刚刚创建的 app1应用程序类似于项目，Django创建 “app1” 文件夹中的应用程序结构如下

```bash
tree ~/myproject/app1/
```

 - **__init__.py** − 只是为了确保 python 作为包处理此文件夹。 		
 - **admin.py** − 此文件帮助您在管理界面中修改应用程序。 		
 - **models.py** − 这是存储所有的应用程序的模型。 		
 - **tests.py** − 这是单元测试。 		
 - **views.py** − 这是应用程序视图。 		

### 注册应用程序到项目中 	 

在这个阶段，我们有“myapp”这个应用程序，现在我们需要注册它到 Django项目“myproject”。

要做到这一点，在你的项目中(添加应用程序名称)到 settings.py 文件更新 INSTALLED_APPS 元组

```bash
vim ~/myproject/myproject/settings.py
```


```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]
```

对这个列表上添加上我们刚刚创建的myapp。使其变为:

```python
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'app1',
]
```

### 启动项目

现在，您的项目创建和配置，确保它能工作。
```bash
python3 ~/myproject/manage.py runserver 0.0.0.0:80
```

## 访问项目

使用浏览器打开:`{host0.http_url}`