from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get("http://bxw2359310172.my3w.com/")
driver.find_element_by_xpath(".//*[@id='ls_username']").send_keys("东方不败")
driver.find_element_by_xpath(".//*[@id='ls_password']").send_keys("123456")
driver.find_element_by_xpath(".//*[@id='lsform']/div[1]/div/p[2]/button").click()
time.sleep(3)
driver.find_element_by_xpath(".//*[@id='forum2']/tr/th/h2/a").click()
time.sleep(1)

driver.find_element_by_xpath(".//*[@id='quickposttopictitle']").send_keys("第三波！！！我们一起来盖楼吧")
driver.find_element_by_xpath(".//*[@id='quickposttopicmessage']").send_keys("我是一楼我先来：1")
driver.find_element_by_xpath(".//*[@id='quickposttopicsubmit']").click()
time.sleep(1)
i=1
while i <1000:
    try:
        driver.find_element_by_xpath(".//*[@id='quickpostmessage']").send_keys("我是%s楼，哇哈哈哈哈哈哈哈"%str(i))
        driver.find_element_by_xpath(".//*[@id='quickpostsubmit']").click()
        time.sleep(1)
        i=i+1
    except:
        time.sleep(1)
