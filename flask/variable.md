# Flask 变量(variable)

可以通过将可变部分添加到规则参数来动态构建URL。 这个变量部分被标记为``。 它作为关键字参数传递给规则所关联的函数。

### 示例1

文件名:variable1.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/hello/<name>')
def hello_name(name):
    return 'Hello %s!' % name

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

运行服务器

```bash
python /share/lesson/flask/variable1.py
```

`route()`装饰器的规则参数包含附加到`{host0.http_url}/hello`的变量部分。

因此，如果在浏览器中输入 ``{host0.http_url}hello/jerry`，那么 jerry 将作为参数提供给`hello()`函数。

除了默认的字符串变量部分之外，还可以使用以下转换器构造规则

| 编号 | 转换器 | 描述                            |
| ---- | ------ | ------------------------------- |
| 1    | int    | 接受整数                        |
| 2    | float  | 对于浮点值                      |
| 3    | path   | 接受用作目录分隔符的斜杠符(`/`) |

### 示例2

在下面的代码中，使用了所有这些构造函数。

文件名:variable2.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/blog/<int:postID>')
def show_blog(postID):
    return 'Blog Number %d' % postID

@app.route('/rev/<float:revNo>')
def revision(revNo):
    return 'Revision Number %f' % revNo

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

运行服务器

```bash
python /share/lesson/flask/variable2.py
```

在浏览器中输入 `{host0.http_url}rev/1.1`，后端`revision()`函数将浮点数作为参数。

会返回：Revision Number 1.100000

在浏览器中输入 `{host0.http_url}blog/1123`

会返回：Blog Number 1123

## Werkzeug的路由模块

Flask的URL规则基于Werkzeug的路由模块。 这确保了形成的URL是唯一的，并且基于Apache制定的先例。

### 示例3：

文件名:variable3.py

```python
from flask import Flask
app = Flask(__name__)

@app.route('/flask')
def hello_flask():
    return 'Hello Flask'

@app.route('/python/')
def hello_python():
    return 'Hello Python'

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

两条规则看起来都很相似，但在第二条规则中，使用了尾部斜线(`/`)。 因此，它变成了一个规范的URL。 因此，使用`/python`或`/python/`返回相同的输出。 但是，在第一条规则的情况下， URL:`/flask/`会导致`404 Not Found`页面。

运行服务器

```bash
python /share/lesson/flask/variable3.py
```

在浏览器中打开看看，`{host0.http_url}flask`是否如描述所说？