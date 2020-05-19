'''
Created on 2017年5月24日

@author: test
'''
from selenium import webdriver
import time
driver =webdriver.Chrome()
i = 0
while i<50:
     url ="http://jandan.net/pic/page-%s#comments"%i
     print(url)
     driver.get(url)
     time.sleep(5)
     i=i+1
   