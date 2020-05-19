'''
Created on 2017年4月5日

@author: test
'''
from   selenium     import webdriver
from selenium.webdriver.android.webdriver import WebDriver
test01=webdriver.Chrome()
test01.get("http://222.209.88.121:9999/zlgxwl/index.html")
test01.maximize_window()
test01.find_element_by_xpath("/html/body/div[3]/div/div[2]/ul/li[6]/a").click()

test01.find_element_by_xpath("//*[@id=\"searchResult\"]/ul/li[2]/div/div[2]/h3/a").click()
text = test01.find_element_by_id("copyright").text   
print(text)
assert text!="null"
print("233")
 #页面底部cp信息
      
            