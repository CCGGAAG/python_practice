from selenium import webdriver  
import time  
from selenium.webdriver.support.ui import WebDriverWait  
from selenium.webdriver.support import expected_conditions as EC  
from selenium.webdriver.common.by import By     
import logging  
import sys  
  
class readTexts():  
      
    def logger(self,logName):
        """ 获取logger"""  
        self.logger =logging.getLogger()  
        logger = self.logger  
        formatter = logging.Formatter('%(asctime)s %(levelname)-8s: %(message)s')  
        file_handler = logging.FileHandler(logName)  
        file_handler.setFormatter(formatter)    
        console_handler = logging.StreamHandler(sys.stdout)  
        console_handler.formatter = formatter   
        logger.addHandler(file_handler)  
        logger.addHandler(console_handler)  
        logger.setLevel(logging.INFO)  
        return logger      
  
    def driver(self):  
        """创建driver"""  
        self.driver = webdriver.Chrome()  
        return self.driver      
      
    def file(self, fileName):
        self.f = open(fileName, "w")
        return self.f
      
    def count(self,b):  
        b= b+1  
        return b  
    def setA(self,a):  
        self.a = a  
        return a  
    def setB(self,b):  
        self.b = int(b)
        return b  
    def setC(self,c):  
        self.c = c  
        return c  
    def setD(self,d):  
        self.d = int(d)
        return d  
#    def count(self,b):  
#        count=self.a+str(b)+self.c  
#        return count  
    def doText(self,log,file,driver,baseUrl,locatePath,titlePath,textPath):  
        logger = log  
        driver = driver  
        f= file  
        driver.get(baseUrl)  
        while self.b<self.d:  
            try:  
                self.b= self.b+1  
                locateXpath =self.a+str(self.b)+self.c  
                print(locateXpath)  
                 
                WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,locatePath)))  
                ele=driver.find_element_by_xpath(locateXpath)  
                newUrl =ele.get_attribute("href")
                logger.info(newUrl )  
                driver.get(newUrl )  
                  
                title = WebDriverWait(driver,5,0.5).until(EC.presence_of_element_located((By.XPATH,titlePath)))  
                text = WebDriverWait(driver,3,0.5).until(EC.presence_of_element_located((By.XPATH,textPath)))  
                f.write(title.text)  
                f.write("\n")  
                f.write(text.text)  
                f.write("\n")  
                logger.info(title.text)  
                logger.info(self.b)  
                driver.back()  
            except:  
                logger.error(Exception )  
                driver.get(baseUrl)  
              
        driver.close()     
        f.close()  