'''
Created on 2017年4月12日

@author: test
'''
from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner


class Baidu(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.implicitly_wait(30)
        self.driver.get('https://www.baidu.com')


    def test_baidu_search(self):
        driver = self.driver
        # driver.get(self.base_url)
        driver.find_element_by_id('kw').send_keys('HTMLTestRunner')
        driver.find_element_by_id('su').click()

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    testunit = unittest.TestSuite()
    testunit.addTest(Baidu("test_baidu_search"))

    fp = open(r'./shark/result22.html','wb')
    runner = HTMLTestRunner(stream=fp,
                            title='百度搜索测试报告',
                            description='用例执行情况:')
    runner.run(testunit)
    fp.close()