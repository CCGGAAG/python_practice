'''
Created on 2017年4月6日

@author: test
'''
from selenium import webdriver

print('判断图片是否存在  demo')
driver = webdriver.Chrome()
driver.get('http://222.209.88.121:9999/zlgxjy/infocenter/index.html')


p1 = driver.find_element_by_xpath(".//*[@id='searchResult']/ul/li/div/div[1]/img")
assert p1.is_displayed()
print(" 图片展示  Verified OK")


driver.get('http://222.209.88.121:9999/zlgxjy/userfiles/1/thumbs/images/cms/article/2017/04/%E7%94%B5%E5%8E%8B.jpg')
print(driver.current_url)

#判断元素是否存在，存在返回True,不存在返回False
def isElementExist(olddriver,element):
    flag=True
    try:
        olddriver.find_element_by_xpath(element)
        return flag
    except:
        flag=False
        return flag
#判断页面是否显示为异常，正确读取返回False,不存在返回True
def is404Found(driver):
    flag=False
    try:
        driver.find_element_by_xpath("html/body/div[1]/h1")
        return flag
    except:
        flag=True
        return flag

#检测异常页面是否存在
r1 = isElementExist(driver,"html/body/div[1]/h1")

#不存在即为正确读取图片
if r1 ==False:
    print("图片正确打开   Verified OK")
else:
    print("服务器404或者图片未找到")