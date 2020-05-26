# HTML 标题(heading)

标题（Heading）是通过 `<h1>` - `<h6>` 标签进行定义的。浏览器会自动地在标题的前后添加空行。

文件名:heading.html


```html
<h6>定义最小的标题。</h6>
<h5>定义五级标题。</h5>
<h4>定义四级标题。</h4>
<h3>定义三级标题。</h3>
<h2>定义二级标题。</h2>
<h1>定义一级标题。</h1>

```
#### 在浏览器中显示
<h6>定义最小的标题。</h6>
<h5>定义五级标题。</h5>
<h4>定义四级标题。</h4>
<h3>定义三级标题。</h3>
<h2>定义二级标题。</h2>
<h1>定义一级标题。</h1>





### 标题使用规范

请确保将 HTML 标题 标签只用于标题。不要仅仅是为了生成**粗体**或**大号**的文本而使用标题。

搜索引擎使用标题为您的网页的结构和内容编制索引。

因为用户可以通过标题来快速浏览您的网页，所以用标题来呈现文档结构是很重要的。

应该将 h1 用作主标题（最重要的），其后是 h2（次重要的），再其次是 h3，以此类推。

## HTML 水平线

`<hr>` 标签在 HTML 页面中创建水平线。

hr 元素可用于分隔内容。

文件名:hr.html

```html
<p>hr 标签定义水平线：</p>
<hr />
<p>这是段落1。</p>
<hr />
<p>这是段落2。</p>
<hr />
<p>这是段落3。</p>
```

#### 在浏览器中显示

<p>hr 标签定义水平线：</p>
<hr />
<p>这是段落1。</p>
<hr />
<p>这是段落2。</p>
<hr />
<p>这是段落3。</p>
## HTML 注释

可以将注释插入 HTML 代码中，这样可以提高其可读性，使代码更易被人理解。浏览器会忽略注释，也不会显示它们。

文件名:comment.html

```html
<!-- 这是一个注释 -->
```

**注释:** 开始括号之后（左边的括号）需要紧跟一个叹号，结束括号之前（右边的括号）不需要，合理地使用注释可以对未来的代码编辑工作产生帮助。