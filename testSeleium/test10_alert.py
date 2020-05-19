from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
driver.get("http://www.w3school.com.cn/tiy/t.asp?f=jseg_prompt")

# 通过frame的name值来定位
driver.switch_to_frame("i")

# 点击按钮触发弹窗
ele = driver.find_element_by_css_selector("body > input[type='button']")
ele.click()
sleep(2)

# 定位到到弹窗
a = driver.switch_to_alert()
print(driver)
# 获取弹窗的内容
print(a.text)

# 触发取消按钮
a.dismiss()
sleep(2)

# 再次点击按钮触发弹窗
ele.click()

# 在弹窗中的输入框输入数据
a.send_keys("许西城")
sleep(2)

# 触发确认按钮
a.accept()

# # 百度登录框
# from selenium import webdriver
# from time import sleep
# # 打开谷歌浏览器
# driver = webdriver.Chrome()
#
# # 输入网址并访问
# driver.get("https://www.baidu.com/")
#
# # 点击登录按钮
# driver.find_element_by_css_selector("#u1 > a.lb").click()
# sleep(2)
#
# # 定位登录弹窗的输入框，并输入数据
# name_box = driver.find_element_by_css_selector("#TANGRAM__PSP_10__userName")
# name_box.send_keys("name")


