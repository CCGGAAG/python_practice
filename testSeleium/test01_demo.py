# from selenium import webdriver
# from time import sleep
#
#
# driver = webdriver.Chrome()
# driver.get("https://jc.zsteel.cc/")
# driver.implicitly_wait(10)
#
# ele = driver.find_element_by_css_selector(".text-3EefK")
# print(ele)
# print(ele.text)
#
# js_sentence_light = "arguments[0].setAttribute('style', arguments[1]);"
# js_sentence_args = "color: yellow; border: 5px solid yellow;"
# driver.execute_script(js_sentence_light, ele, js_sentence_args)
#
#
import json


yaml_dict = {'请求方法': 'post', 'cert': None, '请求地址': 'http://wl-new.stable-test.bdfint.cn/api/v1/index/toppicList', '请求header': {'content-type': 'application/json;charset=UTF-8', 'X-Requested-With': 'XMLHttpRequest'}, '请求参数': {'name': 'zhangsan', 'email': '2981828@11.com', 'age': '12', 'phoneNo': '1232321231'}, 'json': None, 'detail': '物流平台轮播图列表請求方法', 'data': None}
excel_dict = {'客户端': 'pc', 'code': 'wl.demo.insertApi', '请求参数类型': 'all', '请求参数': '{"test":"123"}', '请求用户': 'empty', '期望结果': ['首页图片测试'], '验证字符': '首页图片测试', '环境地址': 'wl', '用例名称': '轮播列表-未登录'}

print(yaml_dict)
print(excel_dict)

dict3 = {}

from itertools import chain


def merge1(yaml_dic, excel_dic):
    for key, value in chain(yaml_dic.items(), excel_dic.items()):
        if key not in list(yaml_dic.keys()):
            yaml_dic[key] = value
        else:
            print("重複: %s" % key)
            print(value)
            print(type(value))
            if str(value).find("{") != -1:
                value_eval = eval(str(value))
            else:
                value_eval = value
            print(type(value_eval))
            if isinstance(value_eval, dict):
                print("xunhuan_yaml %s" % yaml_dic[key])
                print("xunhuan_excel %s" % value)
                merge1(eval(str(yaml_dic[key])), eval(str(value)))
                print("liebiao")
            else:
                pass
    return yaml_dict


ss = yaml_dict["请求参数"]
print(ss)
ex = eval(str(excel_dict))
ya = eval(str(yaml_dict))
print(type(ex))
print(type(ya))


ends = merge1(ya, ex)
print(ends)

