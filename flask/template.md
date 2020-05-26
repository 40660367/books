# Flask 模板(template)

Flask可以以HTML形式返回绑定到某个URL的函数的输出。 例如，在以下脚本中，`hello()`函数将使用附加的``标记呈现*‘Hello World’* 。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return '<html><body><h1>'Hello World'</h1></body></html>'

if __name__ == '__main__':
    app.run(debug = True)
```

但是，从Python代码生成HTML内容非常麻烦，尤其是在需要放置可变数据和Python语言元素(如条件或循环)时。经常需要转义HTML代码。

它可以利用Jinja2模板引擎技术，而不需要从函数返回硬编码HTML。如下代码所示，可以通过`render_template()`函数渲染HTML文件。

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('hello.html')

if __name__ == '__main__':
   app.run(debug = True)
```

Flask将尝试在该脚本所在的同一文件夹中查找`templates`文件夹中的HTML文件。

**示例1：**

文件名:templates/temp.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask HTTP请求方法处理</title>
</head>
   <body>
      <h1>Hello {{ name }}!</h1>
   </body>
</html>
```

文件名:templates.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello/<user>')
def hello_name(user):
    return render_template('temp.html', name = user)

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

运行服务器

```bash
python /share/lesson/flask/templates.py
```

打开浏览器分别打开URL` {host0.http_url}hello/flask`与`{host0.http_url}hello/jerry`，可以看到其中URL的可变部分插入`{{name}}`占位符处。

Jinja2模板引擎使用以下分隔符来从HTML转义。

- `{% ... %}` 用于多行语句
- `{{ ... }}` 用于将表达式打印输出到模板
- `{# ... #}` 用于未包含在模板输出中的注释
- `# ... ##` 用于单行语句

**示例2:**

在以下示例中，演示了在模板中使用条件语句。 `hello()`函数的URL规则接受整数参数。 它传递给`hello.html`模板。 在它里面，收到的数字(标记)的值被比较(大于或小于50)，因此在HTML执行了有条件渲染输出。

文件名:score.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask模板示例</title>
</head>
   <body>

      {% if marks>50 %}
      <h1> You Pass it</h1>
      {% else %}
      <h1>Sorry, You Didn't Pass the test</h1>
      {% endif %}
       
   </body>
</html>
```

请注意，条件语句`if-else`和`endif`包含在分隔符`{%..。%}`中。

文件名:score.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/score/<int:score>')
def score(score):
    return render_template('score.html', marks = score)

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

运行服务器

```bash
python /share/lesson/flask/score.py
```

打开浏览器分别访问`{host0.http_url}score/50`与`{host0.http_url}score/49`查看以有条件地查看HTML输出。

**示例3：**

Python循环结构也可以在模板内部使用。 在以下脚本中，当在浏览器中打开`{host0.http_url}result`时，`result()`函数将字典对象发送到模板文件:*results.html* 。

*result.html* 的模板部分采用for循环将字典对象`result{}`的键和值对呈现为HTML表格的单元格。

文件名:templates/result.thml

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask模板示例</title>
</head>
   <body>
      <table border = 1>
         {% for key, value in result.items() %}
            <tr>
               <th> {{ key }} </th>
               <td> {{ value }} </td>
            </tr>
         {% endfor %}
      </table>
   </body>
</html>
```
在这里，与For循环相对应的Python语句包含在`{%...%}`中，而表达式键和值放在`{{}}`中。

文件名:result.py

```bash
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'phy':59,'che':60,'maths':90}
    return render_template('result.html', result = dict)

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

启动服务器

```bash
python /share/lesson/flask/result.py
```

在浏览器中打开`{host0.http_url}result`以检查输出。
