# CSS基础

虽然不是最佳实践，但可以在元素标签内添加`style`属性，例如

```html
<h2 style="color: blue;">CatPhotoApp</h2>
```

使用CSS选择器是更好的做法

```css
<style>
  h2 {
    color: red;
  }
</style>
```

除了直接选择元素类型，还可以选择元素的`class`，这可以控制多个元素

```css
<style>
  .blue-text {
    color: blue;
  }
</style>
```

字体可设的属性主要包括`font-size` `font-family`

```css
h1 {
  font-size: 30px;
  font-family: sans-serif;
}
```

除了系统字体，还可以引用网络字体，例如

```html
<link href="https://fonts.googleapis.com/CSS?family=Lobster" rel="stylesheet" type="text/CSS">
```

然后`Lobster`字体就可以使用了，注意类似`"Open Sans"`的字体要加引号。

可以指定多个字体，这样当首选字体无法使用时，会依序降级使用。例如：

```css
p {
  font-family: Helvetica, sans-serif;
}
```

CSS使用width属性控制元素的宽度，例如

```css
<style>
  .larger-image {
    width: 500px;
  }
</style>
```

CSS可以元素加边框，边框的属性包括`style`, `color` , `width`,`radius`等，例如：

```css
<style>
  .thin-red-border {
    border-color: red;
    border-width: 5px;
    border-style: solid;
    border-radius:10px;
  }
</style>
```

其中圆角属性`border-radius`还可以设为百分数，特别的`50%`会生成圆形。

元素可以设置背景颜色，例如：

```css
.green-background {
  background-color: green;
}
```

除了`class`，HTML元素还可以设定`id`属性，例如

```html
<h2 id="cat-photo-app">
```

相应的CSS选择器可以选择`id`，例如：

```css
#cat-photo-element {
  background-color: green;
}
```

所有的HTML元素都可以看成一个盒子

![](https://www.runoob.com/images/box-model.gif)

内边距、外边距设定例子

```css
<style>
.blue-box {
    background-color: blue;
    color: #fff;
    padding: 20px;
    margin: 20px;
  }
</style>
```

注意`margin`可以设为负值（出现重叠）

内外边距可以四个方向分别设定，型如 `margin/padding-left/right/top/bottom`

也可以按顺时针方向指定4个值，如：

```css
  .yellow-box {
    background-color: yellow;
    padding: 20px 40px 20px 40px;
  }
```

除了元素类型、`class` `id` ，CSS还可以选择属性，例如

```css
[type='radio'] {
  margin: 20px 0px 20px 0px;
}
```

CSS中有两类长度单位，绝对长度和相对长度，绝对长度单位包括 `px` `mm` `in`等，相对长度包括`em`、`rem`等，例如`em`代表相对父元素的尺寸。

CSS可以设定`body`的样式，例如

```css
body {
  background-color: black;
}
```

CSS属性默认会按标签树逐级继承，注意最高层是`body`元素。

CSS存在多种覆盖关系，其优先级如下：

inline>id>class>element type>parent

还有个不常用的最高优先级，加上 `!important`，例如下述表达会覆盖 inline的设定

```css
<style>
  .pink-text {
    color: pink !important;
  }
</style>
```

CSS中颜色的表示方式一：

```css
body {
  color: #000000;
}
```

简写形式

```css
body {
  color: #F00;
}
```

表示方式二：

```css
body {
  background-color: rgb(255, 165, 0);
}
```

声明一个自定义属性：

```css
element {
  --main-bg-color: brown;
}
```

使用一个局部变量：

```css
element {
  background-color: var(--main-bg-color);
}
```

定义一个默认值

```css
background: var(--penguin-skin, black);
```

 为了增强兼容性，可以用两行CSS代码指定一个默认值：

```css
background: red;
background: var(--red-color);
```

注意CSS变量一样是可以继承的，作为全局变量，可以定义到伪元素 `:root` 。

CSS变量也可在不同的级别中重复定义，则较低级别的会覆盖较高级别。

也可以在响应式中定义

```css
@media (max-width: 350px) {
    :root {
      background: var(--red-color);
    }
  }
```

