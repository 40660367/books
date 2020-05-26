# Django 模板		

Django能够单独分开 Python 和 HTML，Python代码/变量进入视图和HTML模板。 

连接这两个，Django依赖于渲染函数和Django模板语言。 

## 		 		渲染函数

这个函数有三个参数：

- 		请求− 初始化请求 		
- 		模板路径 − 这是相对于在项目 settings.py 文件的变量到 TEMPLATE_DIRS 选项的路径。 		
- 		参数字典 − 字典包含所需的模板中的所有变量。这个变量可以创建或者可以使用 locals() 通过在视图中声明的所有局部变量。 		

## 在Django中使用模板

环境准备

### 在项目中的主目录中创建一个templates目录

```bash
cd ~ && mkdir -p myproject/templates
```

### 在该目录下创建一个模板文件:

```bash
cd ~ && vim myproject/templates/temp.html 
```

模板文件内容为,其中{{ hello }}为标签，可动态显示内容

```html
<h1>{{ hello }}</h1>
```

### 修改项目配置文件

```bash
cd ~ && vim myproject/myproject/settings.py
```

将该文件中的 TEMPLATES列中的 中的 DIRS对应的空列表[]，改为 **[BASE_DIR+"/templates",]**，如下所示

```python
TEMPLATES = [
    {
        ...
        'DIRS': [BASE_DIR+"/templates",],       # 修改位置
        'APP_DIRS': True,
        ...
    }
```

### 创建视图文件

```bash
cd ~ && vim myproject/views.py
```

将`views.py`内容修改为:
```python
from django.shortcuts import render
 
def temp(request):
    context          = {}
    context['hello'] = 'Hello Django Templates!'
    return render(request, 'temp.html', context)
```

### 修改路径映射

```bash
cd ~ && vim ./myproject/myproject/urls.py
```

```python
from django.conf.urls import url
from django.contrib import admin
import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^temp/', views.temp),
]
```

##  运行项目

现在，您的项目创建和配置，确保它能工作。

```bash
python3 ./myproject/manage.py runserver 0.0.0.0:80
```

## 访问项目

打开浏览器`{host0.http_url}temp`，即可进行访问。
