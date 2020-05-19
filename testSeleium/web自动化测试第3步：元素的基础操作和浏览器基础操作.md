上一节，我们了解了如何定位元素，其实也有涉及对于元素的操作，这一节我们就详细的介绍一下对于元素的操作和对于浏览器的一些操作
##1.对于元素的基础操作：
- clear（）：清除输入框内的文本
- send_keys（）：输入特定的字符 （需要传参）
- click（）：点击元素
- submit（）：提交表单（一般这个方法可以替代click）
``` python
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/")

# send_keys 文本框输入值：123
driver.find_element_by_xpath("//*[@id='wd1']").send_keys("123")

# clear 清除文本框内的文本
driver.find_element_by_xpath("//*[@id='wd1']").clear()

# send_keys 文本框输入值：自动化测试
driver.find_element_by_xpath("//*[@id='wd1']").send_keys("自动化测试")

# click 点击进入贴吧按钮
driver.find_element_by_xpath("//*[@id='tb_header_search_form']/span[1]/a").click()

# submit 提交表单(效果等同于click点击)
# driver.find_element_by_xpath("//*[@id='tb_header_search_form']/span[1]/a").submit()
```

##2.对于浏览器的基本操作：   
我们可以通过代码来实现直接控制浏览器，比如访问某个网址，前进后退、跳转浏览器大小、关闭等我们常用的功能，简单介绍一下

- get（）直接访问某个网址（传参输入网址）
- back（） 返回上一个页面
- forward（）进入下一个页面
- close（）关闭当前标签页
- quit（）关闭浏览器
- set_window_size() 设置浏览器大小（传参输入浏览器长、宽）
- maximize_window()  最大化浏览器
- refresh()  刷新页面

我们可以用一幅图来解释一下浏览器操作的方法在实际浏览器中对应的位置
![浏览器中对应的操作](http://img.blog.csdn.net/20170719124942900?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQ0NHR0FBRw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)

下面是代码演示示例：（为了更好地体现操作，我加入了sleep方法，不至于页面变化太快）
```python
from selenium import webdriver
from time import sleep # sleep方法是为了初学者能够更好地了解操作的变化，所以休眠一定时间，可以去掉
driver = webdriver.Chrome()

# get() 进入百度页面
driver.get("https://www.baidu.com/")
sleep(1)

# get() 进入贴吧页面
driver.get("https://tieba.baidu.com/")
sleep(1)

# back() 返回上一页：百度页面
driver.back()
sleep(1)

# forward() 返回下一页：贴吧页面
driver.forward()
sleep(1)

# set_window_size() 设置浏览器大小
driver.set_window_size(500, 1000)
sleep(1)

# maximize_window() 最大化浏览器
driver.maximize_window()
sleep(1)

# 点击title为娱乐明星的<a>标签元素
driver.find_element_by_css_selector("a[title = '娱乐明星']").click()
sleep(1)

# 关闭当前页面
driver.close()
sleep(2)

# 关闭浏览器
driver.quit()
```

##3.其他问题：
对于浏览器的基本操作演示中，有除了sleep（）方法第一次见以外，细心地同学会发现close（）方法执行时并不是关闭的当前现实的“娱乐明星”页面，而是关闭的百度贴吧首页，这两个知识点大家可以研究一下，一个是等待一个是窗口切换。