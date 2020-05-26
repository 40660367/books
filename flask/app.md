# Flask 应用程序(app)

### 测试Flask安装是否成功

文件名:apptest.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/')
def apptest():
    return 'Hello World Test!'

if __name__ == '__main__':
    app.run('0.0.0.0',80)
```

在项目中导入`Flask`模块是强制性的。 Flask类的一个对象是WSGI应用程序。

Flask构造函数将当前模块的名称(`__name__`)作为参数。

Flask类的`route()`函数是一个装饰器，它告诉应用程序哪个URL应该调用相关的函数。

```python
app.route(rule, options)
```

- *rule* 参数表示与该函数绑定的URL。
- *options* 是要转发给底层Rule对象的参数列表。

在上面的例子中，`'/'` URL与`hello_world()`方法绑定。 因此，在浏览器中打开Web服务器的主页时，将呈现此函数的输出。

最后，Flask类的`run()`方法在本地开发服务器上运行应用程序。

```python
app.run(host, port, debug, options)
```

上面方法中的所有参数都是可选的，作用如下表描述说明 - 

| 编号 | 参数    | 描述                                                         |
| ---- | ------- | ------------------------------------------------------------ |
| 1    | host    | 监听的主机名。默认为`127.0.0.1`(localhost)。 设置为`'0.0.0.0'`使服务器在外部可用 |
| 2    | port    | 监听端口号，默认为:`5000`                                    |
| 3    | debug   | 默认为:`false`。 如果设置为:`true`，则提供调试信息           |
| 4    | options | 被转发到底层的Werkzeug服务器。                               |

上面的*apptest.py*脚本保存，就可以从Python shell执行的。使用如下命令 - 

```bash
python /share/lesson/flask/apptest.py
```

在浏览器中打开上面的URL:`{host0.http_url}`。将会看到有 ‘Hello World Test!’ 消息显示在浏览器中。

## 启用调试模式

Flask应用程序通过调用`run()`方法来启动。 但是，当应用程序正在开发中时，应该为代码中的每个更改手动重新启动它。 为了避免这种不便，可以启用调试支持。 如果代码改变，服务器将自动重新加载。 它还将提供一个有用的调试器来跟踪应用程序中的错误(如果有的话)。

在运行或将调试参数传递给`run()`方法之前，通过将应用程序对象的调试属性设置为`True`来启用调试模式。

```python
app.run(debug = True)
```