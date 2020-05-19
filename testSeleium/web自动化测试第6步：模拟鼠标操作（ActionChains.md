在日常的测试中，经常会遇到需要鼠标去操作的一些事情，比如说悬浮菜单、拖动验证码等，这一节我们来学习如何使用webdriver模拟鼠标的操作

首先模拟鼠标的操作要首先引入ActionChains的包
```python
from selenium.webdriver.common.action_chains import ActionChains
```
而对于ActionChains包，一般的写法是：
![导入actionchains包](http://img.blog.csdn.net/20170722155650066?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQ0NHR0FBRw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)
这是这个方法一般的书写格式，下面我们来看一如何使用模拟鼠标操作的具体案例
##1.鼠标拖动操作（滑动验证码问题）
**方法：** 
- drag_and_drop(self, source, target)   
拖动source元素到target元素的位置
  - source：鼠标拖动的原始元素
  - target：鼠标拖动到的另外一个元素（的位置）

- drag_and_drop_by_offset(self, source, xoffset, yoffset)   
拖动source元素到指定的坐标
  - source：鼠标拖动的原始元素
  - xoffset：鼠标把元素拖动到另外一个位置的x坐标
  - yoffset：鼠标把元素拖动到另外一个位置的y坐标
### **演示案例:**  
我们用淘宝的注册页面案例来说明鼠标拖动操作：把滑块从左端移到右端。
![鼠标操作演示图片](http://img.blog.csdn.net/20170722161457608?watermark/2/text/aHR0cDovL2Jsb2cuY3Nkbi5uZXQvQ0NHR0FBRw==/font/5a6L5L2T/fontsize/400/fill/I0JBQkFCMA==/dissolve/70/gravity/Center)  

代码如下  
```python
from selenium import webdriver  
from selenium.webdriver.common.action_chains import ActionChains  
from time import sleep  
  
  
# 模拟鼠标操作-鼠标拖动-滑动验证码  
driver = webdriver.Chrome()  
driver.get("https://reg.taobao.com/member/reg/fill_mobile.htm")  
driver.maximize_window()  
  
# 点击确定按钮  
element1 = driver.find_element_by_css_selector("#J_AgreementBtn")  
element1.click()  
sleep(1)  
  
# 获取滑动条的size  
span_background = driver.find_element_by_css_selector("#nc_1__scale_text > span")  
span_background_size = span_background.size  
print(span_background_size)  
  
# 获取滑块的位置  
button = driver.find_element_by_css_selector("#nc_1_n1z")  
button_location = button.location  
print(button_location)  
  
# 拖动操作：drag_and_drop_by_offset  
# 将滑块的位置由初始位置，右移一个滑动条长度（即为x坐标在滑块位置基础上，加上滑动条的长度，y坐标保持滑块的坐标位置）  
x_location = button_location["x"] + span_background_size["width"]  
y_location = button_location["y"]  
ActionChains(driver).drag_and_drop_by_offset(button, x_location, y_location).perform()  
```
##2.鼠标悬浮操作
**方法：**  
- move_to_element (element) ：鼠标移动（悬浮）到某个元素之上
  - element，要悬浮的元素  

接下来主要对淘宝网首页的地址悬浮菜单来进行演示：  
**淘宝网悬浮菜单**
代码如下所示：通过悬浮菜单选择其他地区
```python
from selenium import webdriver  
from selenium.webdriver.common.action_chains import ActionChains  
from time import sleep  
  
  
# 模拟鼠标操作-鼠标悬浮菜单-淘宝网首页地区选择  
driver = webdriver.Chrome()  
driver.get("https://www.taobao.com/")  
sleep(1)  
  
# 获取要悬浮的元素，并使用move_to_element()方法  
element_list = driver.find_element_by_xpath("//*[@id='J_SiteNavBdL']/li[1]/div[1]/span[1]")  
ActionChains(driver).move_to_element(element_list).perform()  
  
# 悬浮元素出现菜单后，可以点击悬浮菜单里的元素了  
driver.find_element_by_css_selector("#J_SiteNavRegionList > li:nth-child(4)").click()  

3.ActionChains的其他操作：移动鼠标、右击、双击、结合键盘按键的操作等。。。
context_click(element) :   
右击element元素

double_click(element)： 
 双击element元素

move_by_offset(xoffset，yoffset)：   
移动鼠标到指定的x，y位置（相对于浏览器的绝对位置）

move_to_element_with_offset(element, xoffset, yoffset):
相对element元素,移动鼠标到指定的x，y位置(相对于element元素的相对位置)

click_and_hold(element1=None)：   
在element1元素上按下鼠标左键，并保持按下动作（元素默认为空）

release(element2=None):    
 在element2元素上松开鼠标左键（元素默认为空）

key_down(key , element1=None)：    
在element1元素上，按下指定的键盘key（ctrl、shift等）键，并保持按下动作（元素默认为空）

key_up(key , element2=None)：  
   在element2元素上，松开指定的键盘key（元素默认为空）

send_keys(key):  
向当前定位元素发送某个key键

send_keys_to_element(element ，key)：
向element元素发送某个key键
```
