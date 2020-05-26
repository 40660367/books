# Flask 文件上传(uploading)

在Flask中处理文件上传非常简单。 它需要一个enctype属性设置为`'multipart/form-data'`的HTML表单，将该文提交到指定URL。 URL处理程序从`request.files[]`对象中提取文件并将其保存到所需的位置。

每个上传的文件首先保存在服务器上的临时位置，然后再保存到最终位置。 目标文件的名称可以是硬编码的，也可以从`request.files [file]`对象的`filename`属性中获取。 但是，建议使用`secure_filename()`函数获取它的安全版本。

可以在Flask对象的配置设置中定义默认上传文件夹的路径和上传文件的最大大小。

| 变量                           | 说明                                      |
| ------------------------------ | ----------------------------------------- |
| app.config[‘UPLOAD_FOLDER’]    | 定义上传文件夹的路径                      |
| app.config[‘MAX_CONTENT_PATH’] | 指定要上传的文件的最大大小 - 以字节为单位 |

以下代码具有URL: `/upload` 规则，该规则显示`templates`文件夹中的`upload.html`文件，以及调用`uploader()`函数处理上传过程的URL => `/upload-file`规则。

示例:templates/upload.html

```html
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>Flask示例</title>
</head>
   <body>

     <form action = "/upload" method = "POST" 
         enctype = "multipart/form-data">
         <input type = "file" name = "file" />
         <input type = "submit" value="提交"/>
      </form>
   </body>
</html>
```

文件名:upload.py

```python
from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        f = request.files['file']
        print(request.files)
        f.save(f.filename)
        return 'file uploaded successfully,<a href=/upload>Upload Again</a>'
    else:
        return render_template('upload.html')


if __name__ == '__main__':
    app.run('0.0.0.0',80,debug = True)
```

运行服务器

```bash
python /share/lesson/flask/upload.py
```

打开网址`{host0.http_url}upload`，选择文件后点击**提交**。

 表单的post方法调用 `/upload_file`。 底层函数`uploader()`执行保存文件操作。

等待页面上看到提示完成。就可以在您的后端的当前目录查看到刚刚上传的文件了。

```bash
ll ~
```



