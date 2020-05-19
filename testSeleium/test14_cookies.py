from selenium import webdriver
from time import sleep

# 第一个浏览器来进行登录，然后记录登录后的cookie
driver = webdriver.Chrome()
driver.get("https://www.fhyx.com/account/login.html")
sleep(3)
driver.find_element_by_id("LoginForm_username").send_keys("15737957635")
driver.find_element_by_id("LoginForm_password").send_keys("FengHuang520yhy")
# 手动在命令行中输入验证码
code = input("验证码是：")
driver.find_element_by_id("LoginForm_code").send_keys(code)
sleep(1)
driver.find_element_by_xpath("//button[text()='登   录']").click()
sleep(3)
cookie_login = driver.get_cookies()
print("登陆后获取的cookie %s" % cookie_login)


# 第二个新打开的浏览器用来添加cookie
driver2 = webdriver.Chrome()
driver2.get("https://www.fhyx.com")
sleep(2)

# 循环赋值添加cookie
# driver2.delete_all_cookies()
for cookie in cookie_login:
    cookie_list = {
                'domain': '.fhyx.com',
                'name': cookie["name"],
                'value': cookie["value"],
                "expires": "",
                'path': '/',
                'httpOnly': False,
                'HostOnly': False,
                'Secure': False,
            }
    print("添加cookie： %s  ： %s" % (cookie["name"], cookie["value"]))
    driver2.add_cookie(cookie_list)


driver.get("https://www.fhyx.com")
sleep(1)
# 获取单个cookie
cookie_id = driver2.get_cookie("PHPSESSID")
print("获取单个cookie：PHPSESSID：%s" % cookie_id)
# 获取所有cookie
cookie_all = driver2.get_cookies()
print("已经添加的cookie个数 %s" % len(cookie_all))
# 删除单个cookie
driver.delete_cookie("PHPSESSID")
print("删除PHPSESSID后查询此字段，结果： %s" % driver.get_cookie("PHPSESSID"))
# 删除所有cookie（此时第一个浏览器cookie失效）
driver.delete_all_cookies()
print("全部删除后的cookie： %s " % driver.get_cookies())

