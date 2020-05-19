'''
Created on 2017年4月5日

@author: test
'''
from   selenium     import webdriver
driver1=webdriver.Chrome()
try:
    driver1.get("https://www.zhihu.com/")
    driver1.find_element_by_xpath("//*[@id='Popover-3562-51794-toggle']").send_keys("123")

    '''
#titile名
    title=str(driver1.title())
    print("打印title:%r"%title)
#url
    now_url= driver1.current_url()
    print(now_url)
    '''
    print(text)
except Exception:
    print(Exception)
    raise
