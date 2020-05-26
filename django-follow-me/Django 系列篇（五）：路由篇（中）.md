## Django 系列篇（五）：路由篇（中）

原创 星安果 [AirPython](javascript:void(0);) *4月22日*

点击上方“AirPython”，选择“加为星标”

第一时间关注Python技术干货！



![img](https://mmbiz.qpic.cn/mmbiz_jpg/atOH362Boyu4nE1kW84ibibg0D9mhBAwaTjSnqica7oSmMVgGClz7yzYKXrian2O7EQryTgarTgymXjOy0EetbuEJw/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)



**系列导读**



[**01. Django 系列篇（一）：Hello World！**](http://mp.weixin.qq.com/s?__biz=MzU1OTI0NjI1NQ==&mid=2247485051&idx=1&sn=7b8338e999ecd13555c07f526a20e8c7&chksm=fc1b78bbcb6cf1ad328e3da76193498c128e214dbadc86d0eedb5ad7f12166b5dac723db8e08&scene=21#wechat_redirect)

[**02. Django 系列篇（二）：配置篇（上）**](http://mp.weixin.qq.com/s?__biz=MzU1OTI0NjI1NQ==&mid=2247485053&idx=1&sn=f262a08fc023f7187d5b9b1274b78dd6&chksm=fc1b78bdcb6cf1ab9356ddd5137410f6d80f706dd27f517b71ec030d9d85196f6075c06b64ea&scene=21#wechat_redirect)

[**03. Django 系列篇（三）：配置篇（下）**](http://mp.weixin.qq.com/s?__biz=MzU1OTI0NjI1NQ==&mid=2247485106&idx=1&sn=00a63e7cbe661e461c315f7f5ee6d701&chksm=fc1b7872cb6cf16455fd2ccb818f66ad9c529decd216a519e86fb47dda3a873496613802e609&scene=21#wechat_redirect)

[**04. Django 系列篇（四）：路由篇（上）**](http://mp.weixin.qq.com/s?__biz=MzU1OTI0NjI1NQ==&mid=2247485158&idx=1&sn=9f2a1397b087157df1811983eb9549f2&chksm=fc1b7826cb6cf130ba84591e7c7ef71d74fd41f78224595cbb587dc1bf8cc1bd2f98658fc0fd&scene=21#wechat_redirect)

## 1. 路由变量

上面 Django 定义的路由只能代表一个页面，为了使路由指向多个不同的页面，可以在路由中定义变量

变量类型有：整形、字符串、slug、uuid  4 种

其中：

1、字符串：匹配任何非空字符串，但不包含斜杠，默认使用字符串类型

2、整形：匹配任何非负数

3、slug：匹配 ASCII 字符以及连接线和下划线，可理解为注释、后缀或附属等概念

4、uuid：匹配一个 uuid 格式的对象，为了防止路由冲突，所有字母必须小写，然后用 - 连接起来，比如：0755-2323-1111-abcd-3f3g

以匹配年、月、日的视图为列

首先，在 App 的路由集合下新增一条路由信息

```
# urls.py(App)

# 指向日期视图函数
# year:字符串
# month：整形
# day：slug类型
path('<year>/<int:month>/<slug:day>', views.ymd_with_params),
```

其中，使用变量符号 <> 为路由设置变量，: 之前代表变量类型，: 之后代表变量名；如果没有指定变量类型，默认为字符串类型

然后，在 App 下的 view.py 文件中编写路由定义的视图函数

视图函数中包含 4 个参数，其中第 1 个参数为：request，其他 3 个参数为：路由信息包含的 3 个变量

需要注意的是，视图函数的参数必须和路由信息包含的变量一一对应，否则会抛出异常

```
# views.py(App)

def ymd_with_params(request, year, month, day):
    """
    日期视图函数
    :param request:
    :return:
    """
    result = str(year) + '/' + str(month) + "/" + str(day)
    return HttpResponse(result)
```

最后运行项目，在浏览器下输入路由地址，比如：http://127.0.0.1:8000/2020/04/20

![img](https://mmbiz.qpic.cn/mmbiz_png/atOH362BoytLLr7qcJSbCp7k8rB2u8Mt0le2bWDVUgXc7nxibA8aGQzPNY3b0tXtWpicurBUETSBsR2XiaOsAm5Kg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 2. 额外变量

除了在路由地址中设置变量外，还可以为 path 函数追加一个变量

需要注意的是，变量必须以字典的形式表示，参数值不限制数据格式，可以是实体对象，也可以是基本数据类型

```
# urls.py(App)

# 新建一个路由地址airpython
# 指向视图函数with_extra_params
# 并带有参数，参数通过字典定义
path('airpython', views.with_extra_params, {'extra_param': 'AirPython'}),
```

然后，在视图函数 with_extra_params() 中来使用这个参数

```
# views.py(App)

def with_extra_params(request, extra_param):
    """
    带额外的参数
    :param request:
    :param extra_param:
    :return:
    """
    return HttpResponse('Welcome to attention ' + extra_param)
```

## 3. 正则表达式

正则表达式可以限制路由地址中的变量取值范围，对路由变量进行截取与判断，使得路由匹配更加地精确合理

路由正则表达式使用函数 re_path 来定义，以小括号 **( )** 为一个部分单位，每个小括号以 ?P 开头，加入正则表达式，最后通过斜杠 **/** 隔开即可

上面的路由地址可以通过正则表达式改写为：

```
# 路由正则表达式
# 函数：re_path(路由地址,视图函数)
# 路由地址：year、month、day为3个参数
re_path('(?P<year>[0-9]{4})/(?P<month>[0-9]{2})/(?P<day>[0-9]{2}).html',views.ymd_with_params1)
```

其中，用 <> 包住的 year、month、day 为 3 个变量

接着定义视图函数，运行项目，就可以通过地址访问到视图函数渲染的内容。

```
def ymd_with_params1(request,year, month, day):
    """
    日期视图函数(正则表达式)
    :param request:
    :param year:
    :param month:
    :param day:
    :return:
    """
    result = str(year) + '/' + str(month) + "/" + str(day)
    return HttpResponse(result)
```

## 4. 命名空间

随着网页的数目增加，维护会有一定难度，因此，Django 可以为每一条路由设置命名空间，方便我们更好地管理网站

通过查看源码，发现路由函数 include() 有两个参数，分别是：arg、namespace，其中 namespace 代表路由的命名空间，为可选参数；arg 参数类型为字符串或元组（长度为：2 ），作用是指向项目某一个 App 的 urls.py 文件

需要注意的是：

1、如果路由函数不存在命名空间，arg 的数据格式是字符串，比如：first_app.urls，指向 first_app 这个 App 的 urls.py 路由文件

2、如果路由函数命名空间存在，arg 的数据格式一定要设置为长度为 2 的元组，比如：('first_app.urls','first_app')，其中第一个参数为目标 App 的 urls.py 文件，第二个参数一般设置为 App 的名称 

```
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # 指向admin后台系统的路由文件
    path('admin/', admin.site.urls),

    # 指向first_app的路由文件：urls.py
    # namespace:设置路由的命令空间
    path('', include(('first_app.urls', 'first_app'), namespace='first_app')),

    # 指向本App的路由文件：urls.py
    path('second/', include(('second_app.urls', 'second_app'), namespace='second_app')),
]
```

## 5. 路由名称

在 Django 中，路由名称是对一个路由进行命名，作用是在视图、模块里使用路由命名生成路由地址，在后期路由地址发生变更的时候，方便维护和更新

路由定义列表中，可以为函数 path() 和 re_path() 的 name 属性指定一个值，相当于给路由指定了名称

```
urlpatterns = [
    # 指向视图函数index
    # 添加路由name属性
    path('', views.index, name='index'),
]
```

不同 App 中的路由命令可以重复使用，但是在同一个 App 内，最好保证路由名称的唯一性。