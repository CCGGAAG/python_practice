# from selenium import webdriver
#
# driver = webdriver.Chrome()
# driver.get("https://tieba.baidu.com/")
#
# # send_keys 文本框输入值：123
# driver.find_element_by_xpath("//*[@id='wd1']").send_keys("123")
#
# # clear 清除文本框内的文本
# driver.find_element_by_xpath("//*[@id='wd1']").clear()
#
# # send_keys 文本框输入值：自动化测试
# driver.find_element_by_xpath("//*[@id='wd1']").send_keys("自动化测试")
#
# # click 点击进入贴吧按钮
# driver.find_element_by_xpath("//*[@id='tb_header_search_form']/span[1]/a").click()
#
# # submit 提交表单(效果等同于click点击)
# # driver.find_element_by_xpath("//*[@id='tb_header_search_form']/span[1]/a").submit()

# ------------------------------------------------------------------------------------------



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
driver.find_element_by_css_selector("").is_selected()




