from selenium import  webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

# 模拟键盘操作-百度登录页面
driver = webdriver.Chrome()
driver.get("https://passport.baidu.com/v2/?reg")

# 用户名元素定位和手机号元素定位
name_element = driver.find_element_by_css_selector("#TANGRAM__PSP_3__userName")
phone_element = driver.find_element_by_css_selector("#TANGRAM__PSP_3__phone")

# 在手机号输入框输入数据：test
phone_element.send_keys("test")

# 在手机号输入框进行组合键Ctrl+a 、 Ctrl+x
phone_element.send_keys(Keys.CONTROL, "a")
sleep(2)
phone_element.send_keys(Keys.CONTROL, "x")

# 在名字输入框输入组合键Ctrl+v
name_element.send_keys(Keys.CONTROL, "v")

# 在名字输入框输入数字键3
name_element.send_keys(Keys.NUMPAD3)


