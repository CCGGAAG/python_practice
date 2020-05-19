# from selenium import  webdriver
#
# # 打开Chrome 进入示例页面
# driver = webdriver.Chrome()
# driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_frame_cols")
#
# # 定位父类层级iframe
# ele_framest = driver.find_element_by_css_selector("#result > iframe")
#
# # 切换到父类层级iframe-通过元素切换
# driver.switch_to_frame(ele_framest)
# print(driver.page_source)
# print("----------------------------------------------------------------------------")
#
# # 切换到第二个子类frame-通过索引切换
# driver.switch_to_frame(1)
# print(driver.page_source)
# print("----------------------------------------------------------------------------")
#
# # 切换到最上层层级-等同于driver.switch_to_frame(None)
# driver.switch_to_default_content()
# print(driver.page_source)

# 163邮箱登陆
from selenium import webdriver
from time import sleep
driver=webdriver.Chrome()

# 进入163邮箱首页
driver.get("http://mail.163.com/")
sleep(2)

# 切换到包含登录框的frame下
driver.switch_to_frame(0)

# 通过name定位输入框，并输入数据
driver.find_element_by_xpath("//input[@name='email']").send_keys("4444")


