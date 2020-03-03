# HTML基础

## 标题与段落

HTML标签一般包括开和闭两部分，如`<h1>Hello</h1>`

标题标签分为`h1 h2 h3 h4 h5 h6`6个级别，`h1`一般作为页面标题/文章标题。文章段落则使用段落标签，如 `<p>I'm a p tag!</p>`。在网页设计时，不确定文本时可以先用占位符，如`<p>lorem ipsum text</p>`。

HTML中的注释：

```html
​```
<!--
<p>lorem ipsum text</p>
-->
```

HTML5中还引入了一些包含一定语义的标签，如`main header footer nav video article section`等。

## 图片与链接

图片标签，如`<img src="https://www.your-image-source.com/your-image.jpg" alt="Author standing on a beach with two thumbs up.">` 必须包含`src alt`两个属性，注意这是一个自关闭标签。

链接标签，如`<a href="https://freecodecamp.org">this links to freecodecamp.org</a>`，必须包含属性`href`。除外链外，`href`也可以指向内部元素，如

```html
<a href="#contacts-header">Contacts</a>
...
<h2 id="contacts-header">Contacts</h2>
```

链接可以嵌入到文本中，如

```html
<p>
  Here's a <a target="_blank" href="http://freecodecamp.org"> link to freecodecamp.org</a> for you to follow.
</p>
```

注意`target`属性设为`_blank`时链接打开新窗口。

此外，还可以使用 `href="#"`作为占位符，便于JavaScript进一步处理。

 图片可以作为链接的内容，比如：

```html
<a href="#"><img src="https://bit.ly/fcc-running-cats" alt="Three kittens running towards the camera."></a>
```

## 列表

无序列表使用`ul`和`li` 标签

```html
<ul>
  <li>milk</li>
  <li>cheese</li>
</ul>
```

有序列表使用`ol`和`li` 标签

```html
<ol>
  <li>Garfield</li>
  <li>Sylvester</li>
</ol>
```

## 表单

`input`标签是获取用户输入的表单的主要标签，它的`type`属性决定了它的形态

```html
<input type="text" placeholder="this is placeholder text" required>
```

这是文本输入框，比如表单中的用户名，其中的`placeholder`属性是默认的提示文字，`required`属性表示这个元素用户必须输入

`form`标签则代表了整个表单，其它表单元素都嵌入这个标签

```html
<form action="/url-where-you-want-to-submit-form-data"></form>
```

表单提交使用按钮元素`button`来触发，型如

```html
<button type="submit">this button submits the form</button>
```

使用`type`为`radio`可以创建单选项目，型如

```html
    <label for="indoor"> 
<input id="indoor" type="radio" name="indoor-outdoor">Indoor 
</label>
<label for="outdoor"> 
  <input id="outdoor" type="radio" name="indoor-outdoor">Outdoor 
</label>
```

一般嵌入`label`标签使用，注意`label`标签使用`for`属性对应`input`标签的`id`，同一单选列表使用相同的`name`属性

类似的，`input`标签的`type`为`checkbox`时，可以创建多选项目

```html
<label for="loving"><input id="loving" type="checkbox" name="personality"> Loving</label>
```

`ratio` 和`checkbox`的值默认为`on`,如上述`indoor`选中，则`indoor-outdoor=on`,意义不大，所以一般需要设定`value`属性，如

```html
<form action="/submit-cat-photo">
    <label><input type="radio" name="indoor-outdoor" value="indoor"> Indoor</label>
    <label><input type="radio" name="indoor-outdoor" value="outdoor"> Outdoor</label><br>
    <label><input type="checkbox" name="personality" value="loving"> Loving</label>
    <label><input type="checkbox" name="personality" value="lazy"> Lazy</label>
    <label><input type="checkbox" name="personality" value="energetic"> Energetic</label><br>
    <input type="text" placeholder="cat photo URL" required>
    <button type="submit">Submit</button>
</form>
```

`ratio` 和`checkbox`可以标记`checked`属性表示默认选中。

## 基本布局

`div`可能是使用最广泛的标签，用于布局及组织内容的逻辑。

HTML文件需要文件头，现代的HTML5文档，文件头如下：

```html
<!DOCTYPE html>
<html>
  <!-- Your HTML code goes here -->
</html>
```

一个典型的HTML5文档基本结构如下：

```html
<!DOCTYPE html>
<html>
  <head>
    <!-- metadata elements -->
  </head>
  <body>
    <!-- page contents -->
  </body>
</html>
```

类似 `link`, `meta`, `title`,  `style`等元信息都放在 `head` 标签内。



