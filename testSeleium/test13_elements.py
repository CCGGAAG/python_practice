from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()

# 打开百度贴吧首页
driver.get("https://tieba.baidu.com/")

# 贴吧首页搜索栏输入信息（使用两种不同方式）
driver.find_element(By.NAME, "kw1").send_keys("使用By.NAME------")
driver.find_element("name", "kw1").send_keys("使用字符串：name")

"""
By.ID = "id"
By.XPATH = "xpath"
By.LINK_TEXT = "link text"
By.PARTIAL_LINK_TEXT = "partial link text"
By.NAME = "name"
By.TAG_NAME = "tag name"
By.CLASS_NAME = "class name"
By.CSS_SELECTOR= "css selector"
"""
# 获取一组元素
# 获取所有a标签元素
a_tag_list = driver.find_elements(By.TAG_NAME, "a")
for tags in a_tag_list:
    # 打印出来满足条件的webdriver定位
    print(tags)
    # 打印出所有a标签的href属性
    print(tags.get_attribute("href"))

