from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()

# 进入163邮箱首页
driver.get("http://mail.163.com/")
sleep(2)

# 切换到包含登录框的frame下
driver.switch_to.frame(1)

# 通过定位输当前焦点元素，并再次输入数据
ele_box = driver.switch_to.active_element
ele_box.send_keys("123")



