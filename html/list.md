# HTML 列表(list)

HTML 支持有序、无序和定义列表:

## HTML有序列表

```html
<ol>
<li>Coffee</li>
<li>Milk</li>
</ol>
```

#### 在浏览器中显示

1. Coffee
2. Milk

## HTML无序列表

无序列表是一个项目的列表，此列项目使用粗体圆点（典型的小黑圆圈）进行标记。

无序列表使用`<ul>`标签

```html
<ul>
<li>Coffee</li>
<li>Milk</li>
</ul>
```

#### 在浏览器中显示

- Coffee
- Milk

## HTML 自定义列表

自定义列表不仅仅是一列项目，而是项目及其注释的组合。

自定义列表以`<dl>`标签开始。每个自定义列表项以`<dt>`开始。每个自定义列表项的定义以`<dd>`开始。

```html
<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>
```

#### 在浏览器中显示
<dl>
<dt>Coffee</dt>
<dd>- black hot drink</dd>
<dt>Milk</dt>
<dd>- white cold drink</dd>
</dl>

