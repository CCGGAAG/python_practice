'''
Created on 2017年4月13日

@author: test
'''
#coding=utf-8      #防止中文乱码

from selenium import webdriver
#加载unittest模块
import unittest 
import time
#加载HTMLTestRunner，用于生成HTMLreuslt
import HTMLTestRunner
#加载test类
import testHomePage


#单元测试all_test
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(testHomePage.homePage))

                
if __name__ == '__main__':
# 执行测试
    nows = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time())) 
    #打开一个文件，将result写入此file中
    fp=open("result"+nows+".html",'wb')
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title='testHtml',description='result:')
    runner.run(suite)
    fp.close()
    