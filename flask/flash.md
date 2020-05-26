# Flask 闪现消息(flash message)
一个基于GUI好的应用程序需要向用户提供交互的反馈信息。 例如，桌面应用程序使用对话框或消息框，JavaScript使用`alert()`函数用于类似的目的。

在Flask Web应用程序中生成这样的信息消息很容易。 Flask框架的闪现系统使得可以在一个视图中创建一个消息并将其呈现在名为`next`的视图函数中。

Flask模块包含`flash()`方法。 它将消息传递给下一个请求，该请求通常是一个模板。

```python
flash(message, category)
```

在这里

- *message* - 参数是要刷新的实际消息。
- *category* - 参数是可选的。 它可以是’错误’，’信息’或’警告’。

要从会话中删除消息，模板调用`get_flashed_messages()`函数。

```python
get_flashed_messages(with_categories, category_filter)
```

两个参数都是可选的。 如果收到的消息具有类别，则第一个参数是元组。 第二个参数对于仅显示特定消息很有用。

以下闪现模板中收到消息。

```html
{% with messages = get_flashed_messages() %}
   {% if messages %}
      {% for message in messages %}
         {{ message }}
      {% endfor %}
   {% endif %}
{% endwith %}
```

现在我们来看一个简单的例子，演示Flask中的闪现机制。 在下面的代码中，URL => “/”显示了到登录页面的链接，没有指定要发送的消息。

```python
@app.route('/')
def index():
    return render_template('index.html')
```

该链接引导用户显示登录表单的URL => “/login”。 提交时，login()函数验证用户名和密码，并相应地闪现“成功”或“错误”变量消息。

```python
@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('login.html', error = error)
```

如有错误，登录模板将重新显示并显示错误消息。

### 示例：

文件名:templates/flashlogin.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask示例</title>
</head>
   <body>

     <h1>登录</h1>
      {% if error %}
      <p><strong>Error:</strong> {{ error }}
      {% endif %}
      <form action = "/login" method ="POST">
         <dl>
            <dt>用户名:</dt>
            <dd>
               <input type = text name = "username" 
                  value = "{{request.form.username }}">
            </dd>
            <dt>密码:</dt>
            <dd><input type ="password" name ="password"></dd>
         </dl>
         <p><input type = submit value ="登录"></p>
      </form>

   </body>
</html>
```

如果登录成功，则在索引模板上闪现成功消息。

文件名:flashindex.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask消息闪现</title>
</head>
   <body>


         {% with messages = get_flashed_messages() %}
          {% if messages %}
            <ul class=flashes>
            {% for message in messages %}
              <li>{{ message }}</li>
            {% endfor %}
            </ul>
          {% endif %}
        {% endwith %}

      <h1>Flask Message Flashing Example</h1>
      <p>您想要<a href = "{{ url_for('login') }}">
         <b>登录?</b></a></p>

   </body>
</html>
```

文件名:flash.py

```python
from flask import Flask, flash, redirect, render_template, request, url_for
app = Flask(__name__)
app.secret_key = 'random string'

@app.route('/')
def index():
   return render_template('flashindex.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    print(request.method)
    if request.method == 'POST':
        if request.form['username'] != 'admin' or \
            request.form['password'] != 'admin':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('This is a Flash Message:You were successfully logged in')
            return redirect(url_for('index'))
    return render_template('flashlogin.html', error = error)
if __name__ == "__main__":
    app.run('0.0.0.0',80,debug = True)
```

启动服务器

```bash
python /share/lesson/flask/flash.py
```

用浏览器打开:`{host0.http_url}`,点击登陆会跳转到登录页面。输入用户名和密码均为admin后点击**登录**按钮。 将显示一条消息`This is a Flash Message：You were successfully logged in'`。