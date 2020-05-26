# Django 模型

Django 对各种数据库提供了很好的支持，包括：PostgreSQL、MySQL、SQLite、Oracle。

Django 为这些数据库提供了统一的调用API。 我们可以根据自己业务需求选择不同的数据库。

MySQL 是 Web 应用中最常用的数据库。本章节我们将以sqlite作为实例进行介绍。你可以通过[ sqlite 教程](/sqlite/) 了解更多SQL的基础知识。

## 使用Django 插入数据

### 查看数据库配置文件

```bash
cd ~ && cat myproject/myproject/settings.py
```
查看在项目的 settings.py 文件中找到 DATABASES 配置项，sqlite3默认已经写好。
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### 创建APP

Django规定，如果要使用模型，必须要创建一个app。我们使用以下命令创建一个名为sqlapp的 app:

```bash
cd ~/myproject && django-admin startapp sqlapp
tree sqlapp #查看sqlapp的目录结构
```

### 定义模型

```bash
cd ~ && vim myproject/sqlapp/models.py #修改
```

`models.py`代码如下：

```python
from django.db import models

# Create your models here.
class Test(models.Model):
    name = models.CharField(max_length=20)
```

以上的类名代表了数据库表名，且继承了models.Model，类里面的字段代表数据表中的字段(name)，数据类型则由CharField（相当于varchar）、DateField（相当于datetime）， max_length 参数限定长度。

### 将应用sqltest加入至项目

接下来在settings.py中找到INSTALLED_APPS这一项，如下：

```bash
cd ~ && vim myproject/myproject/settings.py #修改
```

```python
INSTALLED_APPS = (
    'sqlapp',               # 添加此项
)
```

在命令行中运行：

```bash
cd ~ 
python3 myproject/manage.py migrate   # 创建表结构
python3 myproject/manage.py makemigrations sqlapp  # 让 Django 知道我们在我们的模型有一些变更
python3 myproject/manage.py migrate 
```

看到几行 "Applying sqlapp." 的字样，你的数据表就创建好了。

表名组成结构为：应用名_类名（如：sqlapp_test）。

**注意：**尽管我们没有在models给表设置主键，但是Django会自动添加一个id作为主键。

### 创建数据库操作文件

添加数据需要先创建对象，然后再执行 save 函数，相当于SQL中的INSERT：

```bash
cd ~ && vim myproject/myproject/sqlops.py
```

```python
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
 
from sqlapp.models import Test
 
# 数据库操作
def insert(request):
    test1 = Test(name='Django Models')
    test1.save()
    return HttpResponse("<p>数据添加成功！</p>")
```

### 配置URL访问路由

```bash
cd ~ && vim myproject/myproject/urls.py #修改
```


urls.py: 文件代码：

```python
from django.conf.urls import *
from . import sqlops
 
urlpatterns = [
    url(r'^insert$', sqlops.insert),
]
```

###  运行项目

现在，您的项目创建和配置，确保它能工作。

```bash
python3 ./myproject/manage.py runserver 0.0.0.0:80
```

### 访问项目

使用`{host0.http_url}insert`，进行访问

### 使用sqlite进行验证

sqlite3数据库文件默认在`~/myproject/`下，您可以一边不断刷新web页面，一边观察数据文件的变化。

```bash
watch stat ~/myproject/db.sqlite3
```
