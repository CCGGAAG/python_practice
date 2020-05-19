import excel  
import readText as rt

class tests():  
    def mian(self):  
        #通过excel获取数据  
        excelList =excel.excel_table_byname("data/abc.xlsx", 0, "a")  
        rows =excel.excel_get_valueFromTitle(excelList, "name", "")
        #将数据通过字典传入到数据字段  
        log = rt.readTexts.logger(self,rows["logname"])  
        file = rt.readTexts.file(self,rows["filename"])  
        driver = rt.readTexts.driver(self)  
        rt.readTexts.setA(self,rows["a"])  
        rt.readTexts.setB(self,rows["b"])  
        rt.readTexts.setC(self,rows["c"])  
        rt.readTexts.setD(self,rows["d"])  
        baseUrl = rows["baseurl"]  
        locatePath=rows["locatepath"]  
        titlePath=rows["titlepath"]  
        textPath=rows["textpath"]  
        #记录日志  
        log.info("loading字典数据：")
        log.info(rows)  
        rt.readTexts.doText(self,log,file,driver,baseUrl,locatePath,titlePath,textPath)  
tests =tests()  
tests.mian()  