# Django 表单

HTML表单是网站交互性的经典方式。 本章将介绍如何用Django对用户提交的表单数据进行处理。

## 使用Django完成Get 请求

HTTP协议以"请求－回复"的方式工作。客户发送请求时，可以在请求中附加数据。服务器通过解析请求，就可以获得客户传来的数据，并根据URL来提供特定的服务。

### 创建项目 	 
```bash
cd ~ && django-admin startproject myproject 
```

### 创建建一个 search.py 文件，用于接收用户的请求：

```bash
cd ~ && vim myproject/myproject/search.py
```

```python
# -*- coding: utf-8 -*-
 
from django.http import HttpResponse
from django.shortcuts import render_to_response
 
# 表单
def search_form(request):
    return render_to_response('search_form.html')
 
# 接收请求数据
def search_get(request):  
    request.encoding='utf-8'
    if 'q' in request.GET and request.GET['q']:
        message = '你搜索的内容为: ' + request.GET['q']
        message = message+"<hr> 点浏览器返回键返回继续尝试"
    else:
        message = '你提交了空表单'
    return HttpResponse(message)
```

创建模板页，用于提取表单，按钮等html组件

```bash
cd ~ && mkdir -p myproject/templates/ && vim myproject/templates/search_form.html
```

```html
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<title>Django Get Test</title>
</head>
<body>
    <form action="/search_get" method="get">
        <h2>GET方式请求:</h2>
        <input type="text" name="q">
        <input type="submit" value="搜索">
    </form>
</body>
</html>
```
### 修改项目配置文件,加入模板目录地址

```bash
cd ~ && vim myproject/myproject/settings.py
```

将该文件中的 TEMPLATES列中的 中的 DIRS对应的空列表[]，改为 **[BASE_DIR+"/templates",]**，如下所示

```python
TEMPLATES = [
    {
        'DIRS': [BASE_DIR+"/templates",],       # 修改位置
    }
```
```python
ALLOWED_HOSTS = ['*']  #在这里请求的host添加了*
```

### 配置URL路径

```bash
cd ~ && vim myproject/myproject/urls.py
```
```python
from . import  search #引入处理文件

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^search_form$', search.search_form),
    url(r'^search_get$', search.search_get),
]
```

### 启动服务并访问

```bash
python3 ~/myproject/manage.py runserver 0.0.0.0:80
```

### 访问项目

使用浏览器打开:`{host0.http_url}`