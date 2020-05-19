'''
Created on 2017年4月5日
@author: test
'''
from   selenium     import webdriver

test=webdriver.Chrome()
test.get("http://www.zsteel.cc/zlgxjy/index.html")
test.find_element_by_xpath("//*[@id=\"navigation_4\"]").click()
print(test.current_url())

#t2 = test01.find_element_by_xpath("html/body/div[7]/div[2]/div/div[2]/span/span/img")
#assert t2.is_displayed()
#print("页面显示图片位置")
#
#t3=test01.get("http://www.zsteel.cc/zlgxjy/userfiles/7410e38610d447ac8f16363f1346e72f/images/cms/article/2017/04/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20170402110847.jpg")
#assert t3!=("404")
#print("图片正确显示")