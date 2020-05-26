# Flask 表单处理(form)

我们已经看到，可以在URL规则中指定http方法。URL映射的函数接收到的表单数据可以以字典对象的形式收集，并将其转发给模板以在相应的网页上呈现它。

在以下示例中，URL => `/` 呈现具有表单的网页(*student.html*)。填充的数据会提交到触发`result()`函数的URL => `/result` 中。

`results()`函数收集字典对象中`request.form`中存在的表单数据，并将其发送给*result.html* 并显示出来。

该模板动态呈现表单数据的HTML表格。

下面给出的是Python的应用程序代码 -

文件名:student.py

```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html",result = result)

if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

文件名:templates/student.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask示例</title>
</head>
   <body>

      <form action = "/result" method = "POST">
         <p>姓名 <input type = "text" name = "Name" /></p>
         <p>物理分数: <input type = "text" name = "Physics" /></p>
         <p>化学分数: <input type = "text" name = "Chemistry" /></p>
         <p>数学分数: <input type ="text" name = "Mathematics" /></p>
         <p><input type = "submit" value = "提交" /></p>
      </form>

   </body>
</html>
```

文件名:templates/result.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask示例</title>
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

**启动服务器**

```bash
python /share/lesson/flask/student.py
```

在浏览器中`{host0.http_url}student`，当点击**提交**按钮时，表单数据以HTML表格的形式呈现在*result.html* 中

