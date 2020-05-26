# Flask 路由(routing)

现代Web框架使用路由技术来帮助用户记住应用程序URL。 无需从主页导航即可直接访问所需页面。

Flask中的`route()`装饰器用于将URL绑定到函数。 例如

文件名:routing.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return 'Index Page'

@app.route('/hello')
def hello_world():
    return 'hello world'

if __name__ == '__main__':
    app.run('0.0.0.0',80)
```

**启动服务器**

```python
python /share/lesson/flask/routing.py
```

使用浏览器打开`{host0.http_url}`和`{host0.http_url}hello`查看

## 使用app定义路由

应用程序对象的`add_url_rule()`函数也可用于将URL与函数绑定，如上例所示，使用`route()`，URL `/hello`规则绑定到`hello_world()`函数。 因此，如果用户访问URL : `{host0.http_url}hello` ，就会调用`hello_world()`函数。

```python
def hello_world():
    return 'hello world'
app.add_url_rule('/', 'hello', hello_world)
```