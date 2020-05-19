'''
Created on 2017年4月17日

@author: test
'''
from selenium import webdriver
import unittest
import time,sys
import HTMLTestRunner
#reload(sys)
#sys.setdefaultencoding("utf-8")
class Baidu(unittest.TestCase):
    """百度首页搜索测试用例"""
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.base_url = "http://www.baidu.com"
    def test_baidu_search(self):
        driver = self.driver
        print ("========【case_0001】 百度搜索=============")
        driver.get(self.base_url + "/")
        driver.find_element_by_id("kw").clear()
        driver.find_element_by_id("kw").send_keys("林志玲")
        driver.find_element_by_id("su").click()
        now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
        #必须要打印路径HTMLTestRunner才能捕获并且生成路径，\image\**.png 是获取路径的条件，必须这样的目录
        pic_path='..\\result\\image\\'+now+'.png'
        print (pic_path)
        driver.save_screenshot(pic_path)
        time.sleep(2)
        
    def tearDown(self):
#        self.driver.quit()
        pass

        
if __name__ == "__main__":
    now = time.strftime("%Y-%m-%d-%H_%M_%S", time.localtime(time.time()))
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))
    HtmlFile = "Test"+now+"HTMLtemplate.html"
    print( HtmlFile)
    fp = open(HtmlFile, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title="百度测试报告", description="用例测试情况")
    runner.run(testunit)