上一节讲到对于元素的操作和浏览器的常用操作如何通过代码实现，这次来学习如何通过定位元素，来获取元素的信息（元素属性、信息等）
##1.获取元素相关的信息
- size：元素的大小
- text：元素内文本
- is_displayed( )  ：元素是否可见
- is_enabled()： 元素是否可用（一般用于判断按钮是否置灰）
- is_selected( ) ： 元素是否被选中（一般用于表单中的单选框和复选框）
- get_attribute ( ) ： 元素的属性（可以获取到所选标签内的属性信息）

接下来以百度新闻首页为例：
![百度贴吧首页](http://img.blog.csdn.net/20170720165302676?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQ0NHR0FBRw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

我们通过如图所示选中的元素来演示如何获取元素的属性
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://news.baidu.com/")

# 新闻标题
element1 = driver.find_element_by_css_selector("label[class='not-checked']")
# 新闻标题选择框
element2 = driver.find_element_by_css_selector("#newstitle")

# 新闻标题的大小（{'height', 'width'}）
print(element1.size)

# 新闻标题的文本
print(element1.text)

# 新闻标题是否可见
print(element1.is_displayed())

# 新闻标题标签内的for属性
print(element1.get_attribute("for"))

# 新闻标题选择框是否被选中
print(element2.is_selected())

```
**结果:**
``` text
{'height': 18, 'width': 48}
新闻标题
True
newstitle
False
```