from selenium import webdriver
from time import sleep

driver = webdriver.Chrome()
driver.get("http://www.runoob.com/js/js-tutorial.html")

# 高亮显示所定位的元素
light_element = driver.find_element_by_id("s")
js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
js_sentence_args = "color: yellow; border: 5px solid yellow;"
driver.execute_script(js_sentence_light, light_element, js_sentence_args)
sleep(3)

# 更改页面输入框中的默认文字
js_sentence_style = "document.getElementById('s').placeholder='我改变了搜索输入框默认文字';"
driver.execute_script(js_sentence_style)
sleep(3)

# 改变滚动条位置
js_sentence_position = "document.documentElement.scrollTop=9999"
driver.execute_script(js_sentence_position)
sleep(3)

