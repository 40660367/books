# Django 系列篇（四）：路由篇（上）

原创作者： 星安果  微信公众号： [AirPython]   关注AirPython,第一时间关注Python技术干货！

**该转载已获原作者授权**

![img](./images/logo.png)



**系列导读**



[**01. Django 系列篇（一）：Hello World！**](./helloworld.html)

[**02. Django 系列篇（二）：配置篇（上）**](./config-part1.html)

[**03. Django 系列篇（三）：配置篇（下）**](./config-part2.html)

## 1. 补充

由于 Django 3.0+ 非长期支持版本，并且版本兼容性还存在一定的的 Bug，建议重新安装 2.2.11 长期支持版本

```
# 重新安装django
pip3 install django==2.2.11
```

另外，为了方便后期的项目部署，建议安装 virtualenvwrapper 之后，新建一个单独的虚拟环境用于存放项目依赖

```
# 安装virtualenvwrapper
pip3 install virtualenvwrapper

# 配置virtualenvwrapper虚拟环境
pass

# 单独新建一个Django的虚拟环境
mkvirtualenv django
```



然后使用 Pycharm 重新建一个 Django 项目，选择上面的虚拟环境即可

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoytLLr7qcJSbCp7k8rB2u8MtpAiaKFYhLTDdSmBUxncZysBicDNw5Z8SIhN7ZbC0RYSKlsYxzpiaibiaNsg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 2. 路由是什么？

路由即：URL，统一资源定位符，是从互联网上访问资源的一种表示方式，互联网上的每个文件都有其唯一的路由，用于指定网络文件的路径位置，便于我们查找

在 Django 中新增的路由，就是向外暴露出我们接受的的 URL 请求集合

简单地说，路由就是我们常说的网页地址，Web 服务对外暴露的 API

路由由 4 部分组成，分别是：路由地址、视图函数、可选变量、路由命名，其中路由地址和视图函数是必选部分

新建的项目根目录包含一个 urls.py，默认包含一个指向 admin 后台管理的 URL 路径

```
from django.contrib import admin
from django.urls import path, re_path

urlpatterns = [
    # 指向admin后台管理的路由文件site.py
    path('admin/', admin.site.urls),
]
```

另外可以在新建的 App 下创建 urls.py，方便管理和区分每一个 App 的路由地址

## 3. 工作原理

在项目运行时，会从项目根目录的 urls.py 读取所有 App 所定义的路由信息，生成完整的路由列表

当用户通过浏览器访问某个路由地址时，Django 会处理这条请求，从中拿到路由地址，从上面的路由列表中匹配操作

最后，通过匹配结果，执行路由信息所指向的视图函数，从而完成整个请求、响应过程

## 4. 基础使用

使用步骤如下：

首先，编辑项目根目录下 url.py 文件，在路由集合 urlpatterns 中新增一条路由信息，指向 App 的路由文件 urls.py

需要注意的是，路由是由 Django 的 path 函数定义，包含两个参数，分别是：路由地址、路由对应的视图函数

```
# urls.py(项目根目录)
# 导入内置的admin后台管理功能模块
from django.contrib import admin
# 导入路由函数功能模块
from django.urls import path, re_path

# urlpatterns：整个项目的路由集合列表
urlpatterns = [
    # 指向admin后台管理的路由
    # 'admin/'：指向127.0.0.1:8000/admin
    path('admin/', admin.site.urls),

    # 新增一条路由信息，指向某个App的路由文件
    # 路由地址为 \，使用include()函数将路由信息分发给first_app下的urls.py处理
    path('',include('first_app.urls')),
]
```

接着，在 App 目下的视图文件 views.py 中，新增一个视图函数 index，利用 Django 内置的 render() 函数渲染一个网页文件

需要注意的是，视图函数必须至少设置一个参数 request，代表获取的请求对象，包含：请求内容、请求方式、请求头等

```
# views.py(App下的视图文件)
from django.shortcuts import render

# 新建一个视图函数：index
# 处理请求，并返回一个相应
def index(request):
    # 渲染index.html网页文件
    return render(request, 'index.html')
```

最后，编辑 App 下的 urls.py 路由信息文件，如果不存在，就新建一个路由文件

和上面编写项目路由文件类似，只需要加入路由信息，指向上面创建的视图函数即可

```
# urls.py(App)
from django.urls import path

# 导入视图函数
# 视图函数：处理请求并返回响应信息
from . import views

urlpatterns = [
    # 指向视图函数index
    path('', views.index)
]
```

最后运行项目，Django 会从配置文件 settings.py 读取 ROOT_URLCONF 的属性值，生成对应项目的路由列表，从而找到对应 App 路由文件，最后根据 App 的路由集合，匹配到对应的视图函数并渲染界面出来。