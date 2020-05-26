## Django 系列篇（三）：配置篇（下）

原创作者： 星安果  微信公众号： [AirPython]   第一时间关注Python技术干货！

该转载已获原作者授权

![img](D:/freeaihub/books/django-follow-me/images/logo.png)



**系列导读**



[**01. Django 系列篇（一）：Hello World！**](./helloworld.html)

[**02. Django 系列篇（二）：配置篇（上）**](./config-step1.html)



## 1. 模板

Django 中的模板引擎在创建项目的时候可以选择，包含：Django Templats 和 Jinja2

模板是一种特殊的 HTML，里面会包含一些变量和指令，配置模板引擎解析，生成一个完整的 HTML 页面，返回给浏览器展示出来。

创建一个新项目时，在 settings.py 文件中，Django 初始化的模板配置信息如下：

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoyuyBw4k9LoSic07Jw8PjFhPxn1fgwOdO20emTktibSLaX57QNPibiaMtu06Ces1KGrG2T2oBl5Gk3N5dQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

需要注意的是，实际项目开发中，只需要配置 DIRS 路径即可，根目录下的 templates 文件夹用于存放通用的模板文件。

```
# settings.py
# 配置模板的路径
# 包含：根目录的 templates 目录和 App 下的 templates 目录
# 注意：每一个 App 下都可以新建一个 templates 目录，然后配置进去
'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'secondapp/templates')
                 ]
```

另外，每一个 App 下也可以新建一个 templates 目录，用于保存当前 App 所需要模板文件。

## 2. 数据库

数据库配置是用于实现项目和数据库的连接，实现数据的增删查改。

Django 提供了 4 种数据库引擎，分别是：

```
# settings.py
# 4 种数据库引擎
# 数据库postgresql
'django.db.backends.postgresql'

# mysql数据库
'django.db.backends.mysql'

# sqlite数据库
'django.db.backends.sqlite3'

# oracle数据库
'django.db.backends.oracle'
```

Django 新建一个项目的时候，默认使用 Sqlite3 数据库，常用于移动端，配置信息如下：

```
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

以连接 Mysql 为例

要实现项目和数据库的连接，首先需要安装 mysqlclient 依赖库

```
# 安装依赖库：mysqlclient
pip3 install mysqlclient
```

接着，在配置文件 setttings.py 中配置 Mysql 的数据库基本信息，包含：用户名、密码、数据库名、HOST 及端口号

```
DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.sqlite3',
    #     'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    # },

    'default': {
        'ENGINE': 'django.db.backends.mysql',   
        'NAME': 'django',    # 数据库名
        'USER': 'root',      # 登录用户名
        'PASSWORD': '123456',    # 登录密码
        'HOST': '139.199.**.**',  # 服务器地址
        'PORT': '3306',   # 数据库端口号，一般为：3306
    },
}
```

最后，使用 python3 manage.py migrate 命令将内置的迁移文件在 Mysql 数据库中生成对应的数据表

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boysmz0KpXDMnv8e1zMOf7OpFvrzWm9a6fRUQu1zMVayp71h9Os23VSHDq7uIN4SxHWiavMumsuxEwpA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

如果执行上面的命令没法连接 Mysql Server，可以通过修改 user 表的 host 项来解决这个问题。

```
# 登录数据库，修改mysql数据库内，user表的host字段
use mysql;
update user set host = '%' where user = 'root';
FLUSH PRIVILEGES;
```

使用 Navicat 客户端可以查看到默认生成的数据表。

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boysmz0KpXDMnv8e1zMOf7OpFGulf1eczJ4ekglNx8I7jjsmNUcib0hac6r12X3biaoRiay7ZpQCS1YibSA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

对于一些数据量很大的系统，单个数据库存储可能没法满足服务器负载要求，需要将数据存储到多数据库服务器

在配置文件 settings.py 中，Django 可以配置多个数据库，使用 default 关键字指定一个默认的数据库

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boysmz0KpXDMnv8e1zMOf7OpF9yNqEscqOj3ng1cKM4Q1KJSgarOSez99Ctm7mAAMmhibA2Hd7uxziaQA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 3. 中间件

中间件在 Django 中，是一个轻量级别的插件系统，用来处理 Django 中的请求和响应的框架级别的钩子

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boysmz0KpXDMnv8e1zMOf7OpFiatPcZ6gGERj0W65F98TBebpNSb29iaWOWwQe3IUtgahn0WGKRMBMJvQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

中间件的作用是处理用户 Request 请求和 Response 响应内容，对 Django 的输入、输出做整体的修改。

可以在中间件列表下添加 LocaleMiddleware 中间件，可以让内置的功能支持中文显示。

```
# 中间件列表
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # 新增中间件，支持中文显示
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]
```

一些复杂的功能可以通过自定义中间件类，然后在 settings.py 进行配置，激活中间件即可。

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boysmz0KpXDMnv8e1zMOf7OpFOxdNs1EEAOictlTXicDiaXEAbdaHFFBk7JbZ4ib1HablydZMJj5DNoQMDg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

需要注意的是，中间件的加入顺序是固定的，不能随意更改顺序，否则会导致程序异常。

Django 项目默认的中间件配置可以满足大部分开发需求，一般不需要进行更改。