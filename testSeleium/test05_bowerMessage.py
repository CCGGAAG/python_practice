from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://tieba.baidu.com/")

# 获取当前页面的URL
url_page = driver.current_url

# 获取当前页面的title
title_page = driver.title

# 获取当前浏览器的名称
name_browser = driver.name

# 获取当前页面的html源码
source_html = driver.page_source

print(url_page)
print(title_page)
print(name_browser)
print(source_html)
