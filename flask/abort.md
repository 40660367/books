# Flask 错误(abort)

Flask类具有带有错误代码的`abort()`函数。

```python
Flask.abort(code)
```

`code`参数使用以下值之一 -

- 400 - 对于错误的请求
- 401 - 用于未经身份验证
- 403 - 禁止
- 404 - 未找到
- 406 - 不可接受
- 415 - 用于不支持的媒体类型
- 429 - 请求过多

这里对上面的代码中的`login()`函数进行一些细微的修改。 如果要显示“Unauthourized”页面，而不是重新显示登录页面，请将其替换为中止(401)的调用。

### 示例

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

文件名:abort.py

```python
from flask import Flask, redirect, url_for, render_template, request, abort
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        if request.form['username'] == 'admin' :
            return redirect(url_for('success'))
        else:
            abort(401)
    else:
        return redirect(url_for('index'))

@app.route('/success')
def success():
    return 'logged in successfully'

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

**启动服务器**

```bash
python /share/lesson/flask/abort.py
```

使用浏览器打开`{host0.http_url}login`来进行验证