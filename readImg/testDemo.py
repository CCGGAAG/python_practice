from urllib import request
from selenium import webdriver
import time
from urllib.request import urlretrieve
import logs

if __name__ == "__main__":
        driver =webdriver.Chrome()
        log = logs.logger()
        gifNumber=0
        jpgn=0
        png=0
        pages = 0
        while pages <75:
            try:          
                url = "http://jandan.net/ooxx/page-%s#comments"%pages
                print(url)
                driver.get(url)
                time.sleep(5)
                pages=pages+1
                eles = driver.find_elements_by_tag_name("img")
                for i in eles:
#                        try:
                            if str(i.get_attribute("src")).find("gif")!=-1:
                                imgUrl = "http:"+str(i.get_attribute("org_src"))
                                log.info(imgUrl)
                                urlretrieve(imgUrl,'img/gif/%s.gif' % gifNumber)
                                gifNumber=gifNumber+1
                                print("第%s张gif图片"%gifNumber)
                            elif str(i.get_attribute("src")).find("jpg")!=-1:
                                imgUrl = str(i.get_attribute("src"))
                                log.info(imgUrl)
                                urlretrieve(imgUrl,'img/jpg/%s.jpg' % jpgn)
                                jpgn=jpgn+1
                                print("第%s张jpg图片"%jpgn)
                            else:
                                imgUrl = str(i.get_attribute("src"))
                                print(imgUrl)
                                urlretrieve(imgUrl,'img/png/%s.png' % png)
                                png=png+1
                                print("第%s张png图片"%png)
                         
#                        except :
#                           raise Exception
#                          
            except :
                print(Exception)
                driver.get(url)