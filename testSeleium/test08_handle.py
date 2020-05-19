from selenium import webdriver
from time import sleep # sleep方法是为了初学者能够更好地了解操作的变化，所以休眠一定时间，可以去掉
driver = webdriver.Chrome()

# get() 进入贴吧页面
driver.get("https://tieba.baidu.com/")
sleep(1)

# 点击title为娱乐明星的<a>标签元素
driver.find_element_by_css_selector("a[title = '娱乐明星']").click()
sleep(1)

# 获取全部窗口的handle
all = driver.window_handles
print(all)

# 获取当前窗口的handle（贴吧首页）
now_page = driver.current_window_handle
print(now_page)

# 获取当前页面的title（当前title）
title_first_page = driver.title
print(title_first_page)

# 将页面handle转到娱乐明星页面
driver.switch_to_window(all[1])

# 获取当前页面的title(切换handle后)
title_next_page = driver.title
print(title_next_page)


