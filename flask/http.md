# Flask HTTP方法

Http协议是万维网数据通信的基础。 它协议定义了从指定URL中检索不同数据的方法。

| 编号 | 方法   | 描述                                                         |
| ---- | ------ | ------------------------------------------------------------ |
| 1    | GET    | 将数据以未加密的形式发送到服务器，这最常用的方法。           |
| 2    | HEAD   | 与GET相同，但没有响应主体                                    |
| 3    | POST   | 用于将HTML表单数据发送到服务器。通过POST方法接收的数据不会被服务器缓存。 |
| 4    | PUT    | 用上传的内容替换目标资源的所有当前表示。                     |
| 5    | DELETE | 删除由URL给出的所有目标资源的所有表示                        |

默认情况下，Flask路由响应GET请求。 但是，可以通过为`route()`装饰器提供方法参数来更改此首选项。

为了演示在URL路由中使用POST方法，首先创建一个HTML表单并使用POST方法将表单数据发送到URL。

### 示例

文件名:template/get.html

```html
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8"/>
    <title>Flask HTTP请求方法处理GET</title>
</head>
   <body>
      <form action = "/httpaction" method = "get">
         <p>输入姓名:</p>
         <p><input type = "text" name = "name" value=""/></p>
         <p><input type = "submit" value = "提交" /></p>
      </form>
   </body>
</html>
```

文件名:http.py

```python
from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)

@app.route('/success/<name>')
def success(name):
    return 'welcome %s' % name

@app.route('/httpaction',methods = ['POST', 'GET'])
def httpaction():
    if request.method == 'POST':
        user = request.form['name']
        return redirect(url_for('success',name = 'POST method:'+user))
    else:
        user = request.args.get('name')
        return redirect(url_for('success',name = 'GET method:'+user))

@app.route('/get')
def httpget():
    return render_template('get.html')
    
if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

启动服务器

```bash
python /share/lesson/flask/http.py
```

用浏览器打开`{host0.http_url}get`,可以看到模板get.html网页，看`form action`被映射到`/httpaction`路由，并由函数`loginaction（）`函数进行处理。 服务器通过POST方法接收数据，因此从表单数据获得`'name'`参数的值，通过以下方式

```python
user = request.form['name']
```

请您自己试下用POST方式获得数据