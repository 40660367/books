# HTML 表单(form)

表单是一个包含表单元素的区域。

HTML 表单用于收集不同类型的用户输入。

表单元素是允许用户在表单中输入内容,比如：文本域(textarea)、下拉列表、单选框(radio-buttons)、复选框(checkboxes)等等。

表单使用表单标签`<form>`来设置:

```html
<form>

input 元素
    
</form>
```

## HTML 表单 - 输入元素(input)

多数情况下被用到的表单标签是输入标签（`<input>`）。

输入类型是由类型属性（type）定义的。大多数经常被用到的输入类型如下：

### 文本域（text fields）

`<input type="text"> `标签定义了文本域。

当用户要在表单中键入字母、数字等内容时，就会用到文本域。

```html
<form>
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>
```
#### 在浏览器中显示
<form>
First name: <input type="text" name="firstname"><br>
Last name: <input type="text" name="lastname">
</form>

**注意:**表单本身并不可见。同时，在大多数浏览器中，文本域的默认宽度是 20 个字符。

### 密码字段(password fileds)

`<input type="password">` 标签定义了密码字段:

```html
<form>
Password: <input type="password" name="pwd">
</form>
```
#### 在浏览器中显示

<form>
Password: <input type="password" name="pwd">
</form>

**注意:**密码字段字符不会明文显示，而是以星号或圆点替代。

### 单选按钮（radio buttons）

`<input type="radio">` 标签定义了表单单选框选项

```
<form>
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>
```

#### 在浏览器中显示

<form>
<input type="radio" name="sex" value="male">Male<br>
<input type="radio" name="sex" value="female">Female
</form>

## 复选框（checkboxes）

`<input type="checkbox">` 定义了复选框. 用户需要从若干给定的选择中选取一个或若干选项。

```html
<form>
<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
<input type="checkbox" name="vehicle" value="Car">I have a car
</form>
```
#### 在浏览器中显示

<form>
<input type="checkbox" name="vehicle" value="Bike">I have a bike<br>
<input type="checkbox" name="vehicle" value="Car">I have a car
</form>

## 提交按钮(submit button)

`<input type="submit">` 定义了提交按钮.

当用户单击确认按钮时，表单的内容会被传送到另一个文件。表单的动作属性定义了目的文件的文件名。由动作属性定义的这个文件通常会对接收到的输入数据进行相关的处理。:
```
<form name="input" action="/form-action" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>
```
#### 在浏览器中显示

<form name="input" action="/form-action" method="get">
Username: <input type="text" name="user">
<input type="submit" value="Submit">
</form>

假如您在上面的文本框内键入几个字母，然后点击确认按钮，那么输入数据会传送到 "form-action"这个路由页面。由该页面进行处理