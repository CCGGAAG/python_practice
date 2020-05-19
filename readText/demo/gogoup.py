from selenium import webdriver
import  time
import  traceback

driver = webdriver.Chrome()
pageNum = 1
alNum = 0
while pageNum <= 8:
    driver.get("http://www.gogoup.com/course/list?pageNum=%s" % pageNum)
    try:
        liNum = 1
        while liNum <= 16:
            xpath1 = ".//*[@id='body']/div[4]/div[1]/div[2]/ul/li[%s]/div/p[2]/span" % liNum
            xpath2 = ".//*[@id='body']/div[4]/div[1]/div[2]/ul/li[%s]/div/p[3]/span[2]" % liNum
            try:
                money = driver.find_element_by_xpath(xpath1).text
                person = driver.find_element_by_xpath(xpath2).text
            except:
                error = traceback.format_exc()
                print(error)
                liNum = liNum + 1
                continue
            print(money)
            print(person)
            if money.find("¥") != -1:
                b = money.find("¥")
                c = money.find(".")
                money_num = int(money[b+1:c])
                print("价格为：%s" % money_num)
                if person.find("在学") != -1:
                    d = person.find("人")
                    person_num = int(person[:d])
                    print("人数为：%s" % person_num)
                    print("总计：%s" % (person_num*money_num))
                    alNum = alNum + (person_num*money_num)
                    print("所有的总和钱数：%s" % alNum)
            liNum = liNum + 1
        pageNum = pageNum + 1
    except:
        error = traceback.format_exc()
        print(error)
driver.quit()
