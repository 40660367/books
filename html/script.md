# HTML 脚本(script)

JavaScript 使 HTML 页面具有更强的动态和交互性。

## HTML`<script>`标签

`<script>` 标签用于定义客户端脚本，比如 JavaScript。
`<script>` 元素既可包含脚本语句，也可通过 src 属性指向外部脚本文件。

JavaScript 最常用于图片操作、表单验证以及内容动态更新。

下面的脚本会向浏览器输出"Hello World!"：
```html
<script> document.write("Hello World!"); </script>
```

<script> document.write("Hello World!"); </script>

## HTML`<noscript>`标签

`<noscript>` 标签提供无法使用脚本时的替代内容，比方在浏览器禁用脚本时，或浏览器不支持客户端脚本时。

`<noscript>`元素可包含普通 HTML 页面的 body 元素中能够找到的所有元素。

只有在浏览器不支持脚本或者禁用脚本时，才会显示` <noscript> `元素中的内容：

```html
<script> document.write("Hello World!") </script> 
<noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>
```



<script> document.write("Hello World!") </script> <noscript>抱歉，你的浏览器不支持 JavaScript!</noscript>