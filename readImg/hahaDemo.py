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
        while pages <5102:
            try:          
                url = "http://www.haha.mx/pic/new/%s"%pages
                print(url)
                driver.get(url)
                time.sleep(5)
                pages=pages+1
                eles = driver.find_elements_by_tag_name("img")
                for i in eles:
                            if str(i.get_attribute("src")).find("gif")!=-1:#判断地址中是否包含gif字段
                                imgUrl = str(i.get_attribute("src"))
                                name =str(i.get_attribute("alt"))
                                log.info(imgUrl)
                                urlretrieve(imgUrl,'img/gif/%s.gif' %(str(gifNumber)+name))
                                gifNumber=gifNumber+1
                                print("第%s张gif图片"%gifNumber)
                            elif str(i.get_attribute("src")).find("jpg")!=-1::#判断地址中是否包含jpg字段
                                imgUrl = str(i.get_attribute("src"))
                                name =str(i.get_attribute("alt"))
                                log.info(imgUrl)
                                urlretrieve(imgUrl,'img/jpg/%s.jpg' %(str(jpgn)+name) )
                                jpgn=jpgn+1
                                print("第%s张jpg图片"%jpgn)
                            else:
                                log.info("wrong")
            except :
                print(Exception)
                driver.get(url)
                