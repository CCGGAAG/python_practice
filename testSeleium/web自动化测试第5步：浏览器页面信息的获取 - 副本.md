上一节讲到了如何利用获得的元素来获取元素的信息，这次来说一下如何获取浏览器相关的信息，主要是页面的路径：URL和页面的标题：title比较常用一定要记住
##1.获取页面相关信息的方法
- current_url :当前页面的URL路径
- title：当前页面的title名称
- name：当前浏览器名称
- page_source：当前html页面源码

前两个比较常用，可能会用到，比如说页面跳转后利用url来判断；页面的title也是一个检测的测试点。
接下来以百度贴吧页面来演示这几个常用方法
##2.代码演示实现
代码如下：
```python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/")

# 获取当前页面的URL
url_page = driver.current_url

# 获取当前页面的title
title_page = driver.title

# 获取当前浏览器的名称
name_browser = driver.name

# 获取当前页面的html源码
source_html = driver.page_source

print(url_page)
print(title_page)
print(name_browser)
print(source_html)
```
##3.结果：
```text
https://tieba.baidu.com/
百度贴吧——全球最大的中文社区
chrome
页面源码(此处不展示页面源码)
```