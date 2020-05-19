from selenium import webdriver

driver = webdriver.Chrome()
driver.get("http://news.baidu.com/")

# 新闻标题
element1 = driver.find_element_by_css_selector("label[class='not-checked']")
# 新闻标题选择框
element2 = driver.find_element_by_css_selector("#newstitle")

# 新闻标题的大小（{'height', 'width'}）
print(element1.size)

# 新闻标题的文本
print(element1.text)

# 新闻标题是否可见
print(element1.is_displayed())

# 新闻标题标签内的for属性
print(element1.get_attribute("for"))

# 新闻标题选择框是否被选中
print(element2.is_selected())


