"""
1.满足条件后继续执行，否则在设置时间过后抛出异常
WebDriverWait(driver, timeout, poll_frequency=POLL_FREQUENCY, ignored_exceptions=None)
driver 所创建的浏览器driver
timeout 最长时间长度（默认单位：秒）
poll_frequency 间隔检测时长（每）默认0.5秒
ignored_exceptions  方法调用中忽略的异常，默认只抛出：找不到元素的异常
2.
until(method, message='')
直到调用的方法返回值为True
until_not(method, message='')
直到调用的方法返回值为False
3.
expected_conditions

title_is(title)判断当前页面标题是否为title
title_contains(title)判断当前页面标题是否包含title
presence_of_element_located(locator) 判断此定位的元素是否存在
url_contains(url)判断页面网址中是否包含url
url_to_be(url)判断页面网址是否为url
url_changes(url)判断页面网址不是url
visibility_of_element_located(locator) 判断此定位的元素是否可见
visibility_of(element)判断此元素是否可见
presence_of_all_elements_located(locator) 判断此定位的一组元素是否至少存在一个
visibility_of_any_elements_located(locator)判断此定位的一组元素至少有一个可见
visibility_of_all_elements_located(locator) 判断此定位的一组元素全部可见
text_to_be_present_in_element(locator, text_) 判断此定位中是否包含text_的内容
text_to_be_present_in_element_value(locator, text_) 判断此定位中的value属性中是否包含text_的内容
frame_to_be_available_and_switch_to_it(locator) 判断定位的元素是否为frame，并直接切换到这个frame中
invisibility_of_element_located(locator) 判断定位的元素是否不可见
invisibility_of_element(element) 判断此元素是否不可见
element_to_be_clickable(locator) 判断所定位的元素是否可见且可点击
staleness_of(element) 判断此元素是否不可用
element_to_be_selected(element) 判断该元素是否被选中
element_located_to_be_selected(locator) 判断定位的元素是否被选中
element_selection_state_to_be(element,Boolean) 判断该元素被选中状态是否和期望状态相同
element_located_selection_state_to_be(locator,Boolean) 判断定位的元素被选中状态是否和期望状态相同
number_of_windows_to_be(num) 判断当前浏览器页签数量是否为num
new_window_is_opened(handles) 判断此handles页签不是唯一打开的页签
alert_is_present() 判断是否会出现alert窗口警报

4.
implicitly_wait(time_to_wait) 在time_to_wait的时间内，如果一直循环无法定位到元素，则抛出异常（全局设置）
time_to_wait 最长的等待时间



"""

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Expect
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.get("http://www.baidu.com/")

# 返回结果
driverWait_assert = WebDriverWait(driver, 15, 0.5).until(Expect.title_contains("百度一下"))
print(driverWait_assert)

# 返回元素
driverWait_ele = WebDriverWait(driver, 15, 0.5).until(Expect.presence_of_element_located(("id", "kw")))
print(driverWait_ele)

driver.get("https://tieba.baidu.com/")
driver.find_element_by_css_selector("a[title = '娱乐明星']").click()
handle = driver.current_window_handle
driverWait_window = WebDriverWait(driver, 15, 0.5).until(Expect.new_window_is_opened(handle))
print(driverWait_window)

# 判断条件失败
driverWait_assert = WebDriverWait(driver, 5, 0.5).until(Expect.title_contains("网易云"), "自定义信息：页面标题错误")