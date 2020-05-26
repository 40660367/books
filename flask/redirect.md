# Flask 重定向(redirect)

Flask类有重定向`redirect()`函数。调用时，它会返回一个响应对象，并将用户重定向到具有指定状态码的另一个目标位置。

`redirect()`函数的原型如下 -

```python
Flask.redirect(location, statuscode, response)
```

在上述函数中 -

- *location* 参数是响应应该被重定向的URL。
- *statuscode* 参数发送到浏览器的头标，默认为`302`。
- *response* 参数用于实例化响应。

以下状态代码是标准化的 -

- HTTP_300_MULTIPLE_CHOICES
- HTTP_301_MOVED_PERMANENTLY
- HTTP_302_FOUND
- HTTP_303_SEE_OTHER
- HTTP_304_NOT_MODIFIED
- HTTP_305_USE_PROXY
- HTTP_306_RESERVED
- HTTP_307_TEMPORARY_REDIRECT

默认状态码是`302`，这是表示’找到’页面。

在以下示例中，`redirect()`函数用于在登录尝试失败时再次显示登录页面。

### 示例:

文件名:templates/login.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask Redirect示例</title>
</head>
   <body>

      <form action = "/login" method = "post">
         <p><h3>Post Method To Login</h3></p>
            <h4>Enter userID</h4></p>
         <p><input type = 'text' name = 'name'/></p>
         <p><input type = 'submit' value = '登录'/></p>
      </form>


      <form action = "/login" method = "get">
        <p><h3>Get Method To Login</h3></p>
           <h4>Enter userID</h4></p>
        <p><input type = 'text' name = 'name'/></p>
        <p><input type = 'submit' value = '登录'/></p>
     </form>

   </body>
</html>
```

文件名:redirect.py

```python
from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST' and \
        request.form['username'] == 'admin' :
        return redirect(url_for('success'))
    return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run('0.0.0.0',80,True)
```

**启动服务器**

```bash
python /share/lesson/flask/redirect.py
```

使用浏览器打开`{host0.http_url}login`来进行验证