from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

# 打开Chrome浏览器
driver = webdriver.Chrome()

# 进入百度高级搜索页
driver.get("http://tieba.baidu.com/f/search/adv")

# 获取select下拉框的元素
ele_select = driver.find_element_by_css_selector("select[name='sm']")

# 获取下拉框中所有选项元素（element）
options = Select(ele_select).options
print("所有选项元素的列表：%s" % options)
for i in options:
    print("元素对应的选项：%s"% i.text)

# 获取下拉框当前显示(选中)的元素(element)
options_selected = Select(ele_select).all_selected_options
print("-----------------------分隔符---------------------------")
print(options_selected)
for j in options_selected:
    print("当前选中的选项(默认项)：%s" % j.text)

# 选择value值为2的选项
Select(ele_select).select_by_value("2")
sleep(1)

# 输出默认项(当前选中项）
now = Select(ele_select).first_selected_option
print(now.text)

from selenium import webdriver
from selenium.webdriver.support.ui import Select
from time import sleep

# 打开浏览器，进入演示页面
driver = webdriver.Chrome()
driver.get("http://www.w3school.com.cn/tiy/t.asp?f=html_dropdownbox")

# 定位输入框文本域
ele_textarea = driver.find_element_by_css_selector("#TestCode")

# 清空文本域
ele_textarea.clear()

# 输入多选下拉框的演示源码 (multiple="multiple\")
texts = "<html> " \
        "<body><form><select multiple=\"multiple\" name=\"cars\"><option value=\"volvo\">Volvo</option>" \
        "<option value=\"saab\">Saab</option><option value=\"fiat\">Fiat</option>\" \
        \"<option value=\"audi\">Audi</option></select></form></body></html>"
ele_textarea.send_keys(texts)

# 点击提交代码
submit_button = driver.find_element_by_css_selector("#butt > input[type='button']")
submit_button.click()
sleep(2)

# 定位frame和select元素
driver.switch_to.frame("i")
ele_select = driver.find_element_by_css_selector("body > form > select")
# 选择全部的选项（多选）
Select(ele_select).select_by_index(0)
Select(ele_select).select_by_index(1)
Select(ele_select).select_by_index(2)
Select(ele_select).select_by_index(3)

# 取消选择第一项选项（页面上可以观察到变化）
Select(ele_select).deselect_by_index(0)

# 输出当前选择的第一项
now = Select(ele_select).first_selected_option
print(now.text)


