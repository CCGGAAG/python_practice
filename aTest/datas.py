'''
Created on 2017年4月17日

@author: test
'''
import time
from selenium import webdriver
import csv

#driver = webdriver.Chrome()

#读取csv文件(使用字典存储)
with open('name.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if row['number']=='2':
            print(row)
#driver.get("http://www.baidu.com")
#try:
#    driver.find_element_by_xpath("123")
#   
#except:
#    #窗口截图
#     driver.get_screenshot_as_file("D:\\baidu_error.jpg")
#driver.quit()