# Flask 静态文件(static)

Web应用程序通常需要一个静态文件，例如支持显示网页的JavaScript文件或CSS文件。 通常，可以通过配置Web服务器提供这些服务，但在开发过程中，这些文件将从包中的静态文件夹或模块旁边提供，它将在应用程序的`/static`上提供。

使用特殊的端点“静态”来为静态文件生成URL。

在以下示例中，`index.html`中的HTML按钮的`OnClick`事件调用`hello.js`中定义的javascript函数，该函数在Flask应用程序的 `/` 中呈现。

### 示例

文件名:static.py

```python
from flask import Flask, render_template
app = Flask(__name__)

@app.route("/static")
def index():
    return render_template("static.html")

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

文件名:templates/static.html

```html
<html>
   <head>
      <script type = "text/javascript" 
         src = "{{ url_for('static', filename = 'hello.js') }}" ></script>
   </head>
   <body>
      <input type = "button" onclick = "sayHello()" value = "Say Hello" />
   </body>
</html>
```

文件名:static/hello.js

```js
function sayHello() {
   alert("Hello World")
}
```

**运行服务器:**

```bash
python /share/lesson/flask/static.py
```

URL访问：{host0.http_url}