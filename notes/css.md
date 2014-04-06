## CSS notes
<hr>

### html template

```
<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<title>An HTML Template</title>
<link href="styles.css" rel="stylesheet" type="text/css" />
</head>
<body>
<!-- asdfsdf -->
</body>
</html>
```

### three ways of styling
* inline

```
<p style="font-size: 25pt; font-weight:bold; font-style:
italic; color:red;"> </p>
```
* embeded

```
<head>
<style type="text/css">
h1 {font-size: 16px;}
p {color:blue;}
</style>
</head>
```

* linked styles
```
<link href="my_style_sheet.css" media="screen"
rel="stylesheet" type="text/css" />
```

### pseudo elements
```
example1:
p:first-letter {font-size:300%; fl oat:left;}
example2:
p:fi rst-line{font-variant:small-caps;}
example3:
<h1 class="age">25</h1>
h1.age:before {content:"Age: "}
h1.age:after {content:" years old."}
```

### selectors:
```css
class1,class2 (class1 and class2)
class1.class2  (element with class1 and class2)
class1+class2 (class2 immediately after class1)
class1~class2 (class2 is slibling of class1)
class1>class2 (class2 is child of class1)
```

### display: blocks and inline
```
blocks
<h1>-<h6> 
<p>
<ol>
<li>
<blockquote>
inline
<a>
<span>
<img>
<em>
<strong>
<abbr>
```
#### swap inline or blocks
```css
/*default is block*/
p {display:inline;}
/*default is inline*/
a {display:block;}
```

### position
* static (default value)
* relative (Relative positioning
allows you to use the left and right
properties to move the element with
respect to its normal position in the
document flow.
* Absolute (enables you to remove an element
from the document fl ow and position
it with respect to another element—
here, the default positioning
context, body.)
* fixed (so the element
does not move when the page is scrolled.)



### box model observation
* Box Model Observation 1#: Dimensioned boxes (width is specified) expand to occupy more horizontal space as padding, borders, and margins are added. Effectively, the width property sets the width of the box’s content, not the box itself, when the box’s width is stated.

* Box Model Observation #2:
Undimensioned elements (no width
set) will always expand to fi ll the
width of their containing element.
Because of this, adding horizontal
margins, borders, and padding to an
undimensioned element does cause
the content to change width.

### substring attribute match

```
img[alt*="Figure"] {border: 1px solid gray;} (select alt contains "Figure", but it is case sensitive)
a[href^="http"] (start with http)
a[href$=".pdf"] (end with pdf)
```

### notes
* section * a {font-size:1.3em;} : 任何是section 孙子元素，而非子元素的a 标签都会被选中
* 浮动非图片元素时，必须给它设定宽度，否则后果难以预料。图片无所谓，因为它本身有默认的宽度。


### tips

* how to select the non-first li

``` li+li``` 

* put background img center of div

```
background-position: 50% 50%,
background-repeat: no-repeat，
```

### references
* [styling with css](http://www.amazon.com/Stylin-CSS-Designers-Guide-2nd/dp/0321525566)
* [smashing css](http://www.amazon.com/Smashing-CSS-Professional-Techniques-Modern/dp/047068416X)
