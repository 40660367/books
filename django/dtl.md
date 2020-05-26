# Django模板语言(DTL) 	 

Django模板引擎提供了一个小型的语言来定义应用程序面向用户的层。 

## 显示变量 	 

变量显示如下：{{variable}}. 模板由视图在渲染(render)函数的第三个参数发送的变量来替换变量。让我们改变 hello.html 显示当天的日期 ： 

hello.html 

```html
<html>   
   <body>
      Hello World!!!<p>Today is {{today}}</p>
   </body>   
</html>
```

然后，我们的视图将改变为 - 

```python
def hello(request):
   today = datetime.datetime.now().date()
   return render(request, "hello.html", {"today" : today}) 
```

现在，我们将得到下面的输出在访问URL:/myapp/hello 之后

```html
Hello World!!!
Today is Sept. 11, 2015 
```

正如你可能已经注意到，如果变量不是一个字符串，Django会使用__str__方法来显示它;并以同样的原则，你可以访问对象的属性，就像在Python中使用的一样。例如：如果我们想显示日期的年份，这里的变量是： {{today.year}}. 

## 过滤器 

它们可以帮助您显示修改的变量。过滤器的结构如下所示： {{var|filters}}. 

一个简单的实例 − 

- 		{{string|truncatewords:80}} − 过滤器将截断字符串，所以只看到前80个字符。 		
- 		{{string|lower}} − 转换字符为小写 		
- 		{{string|escape|linebreaks}} − 转义字符串内容，然后换行转换为标签。 		

还可以设置默认的变量。 

## 标签 

标签可以执行以下操作：if 条件，for循环，模板继承以及更多。 

### if标签 

就像在Python中，你可以使用if，else和elif在模板中 − 

```html
<html>
   <body>
   
      Hello World!!!<p>Today is {{today}}</p>
      We are
      {% if today.day == 1 %}
      
      the first day of month.
      {% elif today == 30 %}
      
      the last day of month.
      {% else %}
      
      I don't know.
      {%endif%}
      
   </body>
</html>
```

在这个新的模板，根据当天的日期，该模板将呈现这个值。 

### for标签 

就像'if'，我们有 'for' 标签，这些完全像在Python中一样使用它们。让我们改变 hello视图列表发送到我们的模板 

```python
def hello(request):
   today = datetime.datetime.now().date()
   
   daysOfWeek = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
   return render(request, "hello.html", {"today" : today, "days_of_week" : daysOfWeek}) 
```

该模板用来显示列表 {{ for }}

```html
<html>
   <body>
      
      Hello World!!!<p>Today is {{today}}</p>
      We are
      {% if today.day == 1 %}
      
      the first day of month.
      {% elif today == 30 %}
      
      the last day of month.
      {% else %}
      
      I don't know.
      {%endif%}
      
      <p>
         {% for day in days_of_week %}
         {{day}}
      </p>
		
      {% endfor %}
      
   </body>
</html> 
```

我们应该得到输出的内容如下

```html
Hello World!!!
Today is Sept. 11, 2015
We are I don't know.
Mon
Tue
Wed
Thu
Fri
Sat
Sun
```

###  块和扩展标签 	 

模板系统是不完整模板继承。当您设计模板的含义，子模板会根据自己的需要填写一个主模板，就像一个页面中所选选项卡可能需要一个特殊的CSS。 

让我们修改 hello.html 模板来从 main_template.html 继承。 

main_template.html 

```html
<html>
   <head>      
      <title>
         {% block title %}Page Title{% endblock %}
      </title>      
   </head>
	
   <body>   
      {% block content %}
         Body content
      {% endblock %}      
   </body>
</html>
```

hello.html 

```html
{% extends "main_template.html" %}
{% block title %}My Hello Page{% endblock %}
{% block content %}

Hello World!!!<p>Today is {{today}}</p>
We are
{% if today.day == 1 %}

the first day of month.
{% elif today == 30 %}

the last day of month.
{% else %}

I don't know.
{%endif%}

<p>
   {% for day in days_of_week %}
   {{day}}
</p>

{% endfor %}
{% endblock %}
```

在上面的示例, 在调用 /myapp/hello，我们仍然会得到相同的结果和以前一样，但现在我们靠的是扩展，并不用重构代码

在 main_template.html 我们定义使用标签块。标题栏块将包含页面标题，以及内容块将在页面主内容。在Home.html中使用扩展继承来自main_template.html，那么我们使用上面块定义(内容和标题)。 

### 注释标签 

注释标签用来模板定义注释，不是HTML注释，它们将不会出现在HTML页面。它可以是一个文件或只是注释一行代码。