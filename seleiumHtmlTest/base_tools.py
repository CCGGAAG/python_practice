'''
Created on 2017年4月13日

@author: test
'''
class toolsBase():
    
    def imgIs404(self,driver,xpathCode):
        t3 =driver.find_element_by_xpath(xpathCode)
        logoImgUrl =t3.get_attribute("src") #获取图片地址
        t2 = driver.get(logoImgUrl)
        assert t2!=("404")
        
    def textIsNotNull(self,driver,xpathCode):
         t1 = driver.find_element_by_xpath(xpathCode).text
         assert t1 != "" 
        
        