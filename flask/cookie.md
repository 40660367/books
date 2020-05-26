# Flask Cookies

Cookie以文本文件的形式存储在客户端计算机上。 其目的是记住和跟踪与客户使用有关的数据，以获得更好的访问体验和网站统计。

Request对象包含一个`cookie`的属性。 它是所有cookie变量及其对应值的字典对象，客户端已发送。 除此之外，cookie还会存储其到期时间，路径和站点的域名。

在Flask中，cookies设置在响应对象上。 使用`make_response()`函数从视图函数的返回值中获取响应对象。 之后，使用响应对象的`set_cookie()`函数来存储cookie。

重读cookie很容易。 可以使用`request.cookies`属性的`get()`方法来读取cookie。

在下面的Flask应用程序中，当访问`{host0.http_url}cookies` 时，会打开一个简单的表单。

```python
@app.route('/cookies')
def index():
    return render_template('cookie.html')
```

文件名:template/cookie.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask Cookies示例</title>
</head>
   <body>

      <form action = "/setcookie" method = "POST">
         <p><h3>Enter userID</h3></p>
         <p><input type = 'text' name = 'name'/></p>
         <p><input type = 'submit' value = '登录'/></p>
      </form>

   </body>
</html>
```

文件名:template/readcookie.html

```html
<html>
<a href='/getcookie'>设置成功，去试下读取cookie吧</a>
</html>
```

表单提交到`{host0.http_url}setcookie`  关联的视图函数设置一个Cookie名称为:`userID`，并的另一个页面中呈现。

```python
@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
   if request.method == 'POST':
        user = request.form['name']
        resp.set_cookie('userID', user)
        return resp
```

readcookie.html该文件包含超链接到另一个函数`getcookie()`的视图，该函数读回并在浏览器中显示cookie值。

```python
@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'
```

文件名:cookie.py

```python
from flask import Flask
from flask import render_template
from flask import request
from flask import make_response


app = Flask(__name__)


@app.route('/cookie')
def index():
    return render_template('cookie.html')

@app.route('/setcookie', methods = ['POST', 'GET'])
def setcookie():
    if request.method == 'POST':
        user = request.form['name']
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)
        return resp

@app.route('/getcookie')
def getcookie():
    name = request.cookies.get('userID')
    print (name)
    return '<h1>welcome, '+name+'</h1>'

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

**启动服务器:**

```bash
python3 /share/lesson/flask/cookie.py
```

**测试cookie:**

首先打开`{host0.http_url}cookie`随便输入一些字符点击提交，然后点击页面的链接即可看到刚刚设置的cookie值