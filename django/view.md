# Django 创建视图 			

视图功能，或简称"view"，是一个简单的Python函数，它接受一个Web请求，并返回一个Web响应。

此响应可以是 Web页的HTML内容，或重定向，或404错误，或XML文档，或图像/片等。

例如：使用视图创建页面，请注意需要将一个视图关联到一个URL，并把它看作一个网页。 在Django中，视图必须在应用程序的views.py文件中创建。 

## 在Django中创建简单的视图并通过URL访问到

我们将在 app1创建一个简单的视图显示： "Index Page of Django" ，让他可以在/这个根URL路径下被访问到。 再创建一个简单的视图显示： "Hello, Django!" ，让他可以在/hello这个URL路径下被访问到。

环境准备

### 创建应用app1的视图文件views.py

```bash
cd ~ && vim ./myproject/app1/views.py
```

文件内容如下:

```python
from django.http import HttpResponse

def hello(request):
   text = """<h2>Hello, Django!</h2>"""
   return HttpResponse(text) 

def index(request):
    text="<h1>Index Page of Django<h1>H"
    return HttpResponse(text)
```

在这个视图中，我们使用 HttpResponse 呈现 HTML(你可能已经注意到了，我们将HTML硬编码在视图中)。 

### 修改程序主程序目录下urls文件,把视图和URL路径进行映射

在这个视图我们只是需要把它(这将在即将到来的章节中讨论)的页面。 

```bash
cd ~ && vim ./myproject/myproject/urls.py
```

```python
from django.conf.urls import url
from django.contrib import admin
from app1 import views as app1views
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hello/', app1views.hello),
    url(r'^$', admin.site.urls),
]
```

##  运行项目

现在，您的项目创建和配置，确保它能工作。

```bash
python3 ./myproject/manage.py runserver 0.0.0.0:80
```

## 访问项目

使用浏览器打开:`{host0.http_url}hello/`