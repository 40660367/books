# Django 系列篇（一）：Hello World！

原创作者： 星安果  微信公众号： [AirPython]   关注AirPython,第一时间关注Python技术干货！

**该转载已获原作者授权**

![img](./images/logo.png)

## 1. 为什么是 Django

Python 常用的 Web 框架包含：Django、Flask、Tornado 等。

Django 框架的功能和文档更完善，并提供一站式解决方案，自带后台管理系统、强大的数据库功能，能开箱即用，相比其他 Web 框架，使用更便捷。

## 2. 安装

在安装 Django 之前，需要在本机安装、配置 Python 开发环境

接着，使用 pip3 命令行在线安装 Django 依赖库

```bash
# 安装django依赖库
pip3 install Django -i https://pypi.tuna.tsinghua.edu.cn/simple/
#默认为3.0.6
#安装需要一段时间，请耐心等待
```

## 3. 创建项目 - 命令行

安装完 Django 依赖库之后，就可以使用 django-admin 命令创建一个项目。

```bash
# 使用 django-admin 创建一个项目
# 命令：django-admin startproject 项目名称
cd ~
django-admin startproject firstProject
```

项目文件包含：命令行工具 manage.py、项目配置文件 settings.py、项目路由设置文件 urls.py、服务器网关接口 wsgi.py、Django3.0 新增的 asgi 服务入口

```bash
tree firstProject
```

```reponsetext
firstProject
├── firstProject
│   ├── asgi.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
└── manage.py

1 directory, 6 files
```

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoysicZZPUENx28ECic8X2d5jx4wREVJU5xJyYqbIburLzKopdLIsOMkxoTkK5ZImAt2r4sIIYXEiajOvA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

创建完项目之后，利用命令行工具 manage.py 创建应用 App，一个 Django 项目可以包含多个 App。

```bash
# 使用 manage.py 为项目创建一个App
# 命令：python3 startapp App名称
cd ~/firstProject/
python3 manage.py startapp firstapp
```

每一个 App 包含：后台管理功能 admin.py、数据库映射库 models.py、视图文件 views.py、数据迁移文件夹 migrations 等。

![img](https://mmbiz.qpic.cn/mmbiz_jpg/atOH362BoysicZZPUENx28ECic8X2d5jx4G6cWm1uQsGa5anW3V7Xjw1sH9mloltUDjzDbIZ5LwVOIe8nIibyEAXA/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



您的项目配置文件在`~/firstProject/settings.py`。以下是可能需要设置一些重要的选项

```bash
vim ~/firstProject/firstProject/settings.py
```

在我们创建的项目里修改`setting.py`文件

在`[]`里添加了`'*'`,代表接受任何外部主机的请求。

```conf
ALLOWED_HOSTS = ['*'] 
```

创建完项目和 App 之后，接着利用 manage.py 命令行工具，指定端口号为：80，启动当前项目。

```
# 启动项目
# 端口号指定为：80
cd ~/firstProject/
python3 manage.py runserver 0.0.0.0:80
```

最后，在浏览器中输入：`{host0.http_url}`，即可以查看项目的运行情况了。

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoysicZZPUENx28ECic8X2d5jx4ABGCiaKSECplzibTIQe53AG0eI7Kia5Q21WGJEX15knu8DAxI79t6ACuA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 4. 创建项目 - Pycharm

使用 Pycharm 创建、管理项目更加方便，只需要指定项目类型为 Django，选择一个 Python 虚拟环境，设置第一个 App 的名称，即能快速创建一个项目，并内置一个 App

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoysicZZPUENx28ECic8X2d5jx4IqdNfRVMWbAGaKlQ49wAoPwW2EicX3icn8lw0PCb1s99MJNjEn6icGibDQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

使用 Pycharm 创建的项目会包含 templates 文件夹，用于存放 HTML 视图模板文件。

另外需要注意的是，这里默认选择的模板是 Django，可以手动切换到 Jinja2

最后，只需要点击右上角的运行，就可以启动项目。

## 5. Hello World

下面我们看看 Django 怎么实现 Hello World 的。

第 1 步，在 templates 文件夹下新建一个 index.html，内容如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoysicZZPUENx28ECic8X2d5jx462tz80HZj1P8s962nlRRdcWfrrPicib6RxbUa2dFF0ohEbGYAN8QODeg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

第 2 步，在 App 的视图文件 view.py 中自定义一个方法用来 渲染 上面的页面。

```python
# App view.py
from django.shortcuts import render

# App定义一个方法 index()，用来渲染页面
def index(request):
    return render(request, 'index.html')
```

第 3 步，在项目 urls.py 路由配置中配置路由信息，指向 App 的视图即可。

项目的路由可以自动匹配到对应的路由信息。

```python
from django.contrib import admin
from django.urls import path

# 导入App的视图
from secondapp.views import index

# 路由配置
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index)
]
```

通过上面 3 步操作，启动项目，即可以利用浏览器访问 Hello World 页面了

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoysicZZPUENx28ECic8X2d5jx4V8ic3ZfPnvg0TIJQePt560hA0GEeoR0lM1WmCWKqHBr5rfbBp3Fl3Gw/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)
