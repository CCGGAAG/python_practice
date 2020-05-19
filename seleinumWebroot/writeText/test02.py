'''
Created on 2017年4月21日

@author: test
'''
from selenium import webdriver
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By   
import logging
import sys

#准备阶段
driver = webdriver.Chrome()
f = open("黑铁之堡.txt","w")
#生成日志文件
logger = logging.getLogger()
formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')
file_handler = logging.FileHandler("黑铁之堡.log")
file_handler.setFormatter(formatter)  # 可以通过setFormatter指定输出格式
console_handler = logging.StreamHandler(sys.stdout)
console_handler.formatter = formatter 
logger.addHandler(file_handler)
logger.addHandler(console_handler)
logger.setLevel(logging.INFO)

#基本属性
a=".//*[@id='list']/dl/dd["
b = 9
c="]/a"

#封装方法
def count(b):
    b= b+1
    return b

def url(url):
    return (a+str(url)+c)

#打开目录页
driver.get("http://www.biqudu.com/0_249/")

#循环获取xpath
while b<2059:
    try:
        b= count(b)
        print(url(b))
        
       #xpath是目录页底部的一个元素的路径，为了确保页面加载完
        WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='footer']/div[2]/p[1]")))
        ele=driver.find_element_by_xpath(url(b))
        newUrl =ele.get_attribute("href")
        #获取到这章的Url，然后访问这章
        logger.info(newUrl )
        driver.get(newUrl )
        #标题
        title = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='wrapper']/div[5]/div[2]/div[2]/h1")))
        #内容
        text = WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,".//*[@id='content']")))
        #写入到txt文件，记得加入换行：\n
        f.write(title.text)
        f.write("\n")
        f.write(text.text)
        f.write("\n")
        #日志记录章节的信息
        logger.info(title.text)
        logger.info(b)
        #返回目录页
        driver.back()
    except:
        #如果由于网络等原因无法获取到，那么重新进入目录页
        logger.error(Exception)
        driver.get("http://www.biqudu.com/0_249/")
        b= b-1

#关闭文件和driver驱动
driver.close()   
f.close()

