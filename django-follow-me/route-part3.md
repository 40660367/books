# Django 系列篇（六）：路由篇（下）

原创作者： 星安果  微信公众号： [AirPython]   关注AirPython,第一时间关注Python技术干货！

**该转载已获原作者授权**

![img](./images/logo.png)



**系列导读**



[**01. Django 系列篇（一）：Hello World！**](./helloworld.html)

[**02. Django 系列篇（二）：配置篇（上）**](./config-part1.html)

[**03. Django 系列篇（三）：配置篇（下）**](./config-part2.html)

[**04. Django 系列篇（四）：路由篇（上）**](./route-part2.html)

**05.** [**Django 系列篇（五）：路由篇（中）**](./route-part2.html)

## 1. 前言

上两篇讲了路由的定义、变量、命名空间等，都是将路由看成一个网址，通过浏览器去访问。

实际上，在视图、模型、后台管理等功能模块，也会使用到路由。

## 2. 模板使用路由

Django 中，可以在模板 HTML 文件中使用 url 语法生成路由地址

首先，在 App 内定义一个路由，编写对应的视图函数，以之前的日期路由函数为例

```
# urls.py(App)
# App下的日期路由
urlpatterns = [
    # 指向日期视图函数
    path('<year>/<int:month>/<slug:day>', views.ymd_with_params, name='ymd_with_params'),
]

# views.py(App)
# App编写视图函数
def ymd_with_params(request, year, month, day):
    """
    日期视图函数
    :param request:
    :return:
    """
    result = str(year) + '/' + str(month) + "/" + str(day)
    return HttpResponse(result)
```

然后，编辑 templates 文件夹下的 HTML 文件，使用 url 语法为 a 标签指定一个路由地址

```
# index.html(项目templates文件夹下)
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <title>第一个页面</title>
</head>

<body>
<h1>Hello World！</h1>

<a href="{% url 'ymd_with_params' '2020' '04' '23' %}">跳转到日期路由页面</a>
</body>
</html>
```

其中，url 语法包含 4 个参数，分别代表：路由的 name 值，路由和视图函数中定义的 3 个参数

模板语法 url 中使用的变量参数之间使用空格隔开，与路由地址定义的参数保证一一对应关系

需要注意的是，如果 App 有设置 namespace，模板语法 url 使用路由的时候，需要通过 namespace:路由名称的形式作为第一个参数

```
# App指定了namespace
urlpatterns = [
   path('', include(('first_app.urls', 'first_app'), namespace='first_app')),
]

# 模板中使用
<a href="{% url 'first_app:ymd_with_params' '2020' '04' '23' %}">跳转到日期路由页面</a>
```

最后，运行项目，点击 a 标签，即可以通过模板中定义的路由跳转到对应的页面

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362Boys7k1ISZzeCDfwLALH1bYuYfn5ejA9XJu9XMTpmDXg7YoeFtqHuurPUPadj3sdoAYSkSiaf6MZoZ2g/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 3. 视图反向解析路由 

在视图里也可以使用路由，这一操作称为反向解析，通过路由命名或路由地址来获取路由信息。

反向解析主要使用 reverse()、resolve() 两个函数，其中

reverse() ：通过路由命名和视图对象生成路由地址

resolve()：通过路由地址获取路由对象信息

比如：定义了 namespace 为 temp_nam_space，路由 name 为 temp_name

那么，可以使用 reverse() 函数生成路由地址，然后通过 resolve() 函数将路由地址转换为路由对象

```
def ymd_with_params2(request, year, month, day):
    """
    日期视图函数
    :param request:
    :return:
    """
    # 参数
    args = ['2020', '04', '23']
    result = resolve(reversed('temp_nam_space:temp_name',args=args))

    # 查看路由信息
    print(result.kwargs)
    print(result.url_name)
    print(result.namespace)
    print(result.view_name)
    print(result.app_name)

    result = str(year) + '/' + str(month) + "/" + str(day)
    return HttpResponse(result)
```

同样，直接使用 reverse() 函数生成一个路由地址，放到响应中进行返回

```
def ymd_with_params3(request):
    """
    日期视图函数
    :param request:
    :return:
    """
    # 参数
    args = ['2020', '04', '23']

    # 使用reversed()函数生成路由地址
    return HttpResponse(reversed('temp_nam_space:temp_name', args=args))
```

## 4. 重定向

路由重定向，即：网页跳转到其他网页，对应的状态码为：301、302、303、307、308

Django 中重定向有 2 种方式，分别是：路由重定向、视图的重定向

路由重定向使用 RedirectView 类的 as_view() 方法类定义，默认支持 GET 请求

```
# urls.py(App)
# 路由重定向
# 参数url：设置网页跳转的路由地址，/ 代表首页
path('redirect_path', RedirectView.as_view(url='/'), name='redirect_path')
```

运行项目后，访问 redirect_path 路由，将会自动重定向到首页界面

对于视图重定向，相对使用更灵活，利用 Django 内置的 redirect() 函数能实现多方面的开发需求

```
# views.py(App)
def index_redirect(request):
    """
    首页重定向到日期页面
    :param request:
    :return:
    """
    # redirect() 函数，重定向到其他网页
    return redirect(reverse('ymd_with_params', args=[2020, 4, 23]))
```