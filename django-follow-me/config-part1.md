# Django 系列篇（二）：配置篇（上）

原创作者： 星安果  微信公众号： [AirPython]   关注AirPython,第一时间关注Python技术干货！

**该转载已获原作者授权**

![img](./images/logo.png)

**系列导读**



[***\*01.\**** **Django 系列篇（一）：Hello World！**](./helloworld.html)



## 1. Django 有哪些配置

创建一个项目之后，会自动在项目根目录下生成一个配置文件，即：settings.py

分为运行环境和基础功能的配置，主要包含：App、中间件、模板、数据库、域名访问权限、项目路径等

## 2. 基本配置

基本配置包含对项目路径、域名访问、密钥、App 列表的配置。

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boyu0tLJ8zXGwHBDR1BSvD2qv2PcndjuBG2S6nFicELhINBsG3DJcNXVG8icwD697kQ3ISLGKYDeCtHJA/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

一般来说，项目路径和密钥配置 是自动生成的，不需要进行修改配置。

其中密钥是随机生成的一个字符串，用于重要数据，包含：密码、CSRF 机制、Session 的加密处理。

调试模式在开发阶段，应设置为 True，部署上线时，应更改为：False

域名访问设置可以访问的域名列表，当 DEBUG 为 True 时，默认只能在本机浏览器访问调试；否则需要填写 ALLOWED_HOSTS，指定容许访问的域名。

```
# 设置可以访问的域名
# 使用 ['*'] 容许所有域名访问
ALLOWED_HOSTS = ['*']
```

内置 App 包含：

- admin 后台管理系统
- auth 用户认证系统
- contenttypes 模型 Model 元数据
- sessions Session 会话，用于记录用户信息
- messages 消息提示功能
- staticfiles 静态资源查找

另外，可以通过 manage.py 命令行工具新建 App，然后在列表中进行配置。

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boyu0tLJ8zXGwHBDR1BSvD2qvOF5ZD5q8Uz2g3ffeWyQTKMiaGtaJZWfKXZSf0gm3M7yW4qH2NFoHQug/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 3. 静态资源配置

静态资源指网站中不会改变的文件，主要包含：CSS 文件、JS 文件、图片等资源，配置属性有 3 种，分别是：STATIC_URL、STATICFILES_DIRS、STATIC_ROOT

STATIC_URL 代表资源路由，Django 对于静态资源，默认配置信息如下：

```
# settings.py
# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.0/howto/static-files/

STATIC_URL = '/static/'
```

如果资源路由保持默认值，在调试模式下，项目只能识别 App 下 static 文件夹下的静态文件。

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boyu0tLJ8zXGwHBDR1BSvD2qvhwOpTMthm8FBFShMpQEzRoYGdSsHyib8pGKeWWicbicVNK37ZcPK96U3w/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

由于资源路由 STATIC_URL 的限制，实际开发过程中，其他目录的资源文件没法访问。

STATICFILES_DIRS，即资源集合

可以在 settings.py 文件内自定义静态资源文件夹列表，这些列表目录下的静态文件都可以访问到。

```
# settings.py
# 静态资源集合
# 加入项目根目录下的static文件夹
# App下自定义的静态资源文件夹
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static'),
                    os.path.join(BASE_DIR, 'secondapp/static1')]

# 三个静态文件目录下的静态文件都可以访问
# http://127.0.0.1:8000/static/1.png
```

STATICFILES_ROOT，即资源部署

STATICFILES_ROOT 主要收集整个项目的静态资源，然后放在一个新的文件夹内。

在项目开发阶段，Django 自动提供静态文件的代理服务，无需指定显式指定 STATICFILES_ROOT。

需要注意的是，在项目上线的时候，必须要配置 STATICFILES_ROOT，然后执行 collectstatic 指令，实现服务器和项目之间的映射

```
# settings.py
## 资源部署
STATIC_ROOT = os.path.join(BASE_DIR, 'static_root')

# 把静态文件收集到 STATIC_ROOT中。
# python3 manage.py collectstatic
```

最后，通过 http://127.0.0.1:8000/static/3.png 即可以访问到媒体文件。

## 4. 媒体资源配置

除了静态资源，还有一些经常变动的资源，通常需要放置到媒体资源文件夹内，比如：用户头像。

媒体资源配置属性有 2 种，分别是：MEDIA_URL 和 MEDIA_ROOT

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boyu0tLJ8zXGwHBDR1BSvD2qvMRiaYQAf2KIvbGu5aPO3oYQ6D1c6rojPmIA5F6OWEF8bgd51q9K5DWQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

其中，MEDIA_URL 作用是配置媒体资源的路由地址，指向项目根目录下的 media 文件夹

MEDIA_ROOT 是获取 media 文件夹在当前系统的完整路径

```
# settings.py
# 媒体资源
# 设置媒体路由地址信息
MEDIA_URL = './media/'
# media文件夹的完整路径
MEDIA_ROOT = os.path.join(BASE_DIR, MEDIA_URL)
```

为了保证 Django 找到媒体文件，即：浏览器能访问 media 文件夹的文件，需要在 url.py 文件中，将 media 文件夹注册到 Django 项目路由设置文件中。

```
# urls.py
from django.conf import settings
from django.contrib import admin
from django.urls import path, re_path
# 将media文件夹添加路由地址
from django.views.static import serve

from secondapp.views import index

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    # 配置媒体文件夹路由地址
    re_path('media/(?P<path>.*)', serve, {'document_root': settings.MEDIA_ROOT}, name='media')
]
```

最后，通过 http://127.0.0.1:8000/media/4.png 即可以访问到媒体文件。

下篇文章将继续聊模板、数据库、中间件等配置的内容。