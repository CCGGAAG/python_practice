# coding:utf-8
import ddt
import unittest
 
# 测试数据
test_data1 = [{"username": "张三", "pwd": "zhangsan"},
             {"username": "李四", "pwd": "lisi"},
             {"username": "王五", "pwd": "wangwu"},
             ]
test_data2 = [{"username": "悟空", "pwd": "wukong"},
             {"username": "悟能", "pwd": "woneng"},
             {"username": "悟净", "pwd": "wujing"},
             ]
 
 
 
@ddt.ddt
class Test(unittest.TestCase):
    def setUp(self):
        print("Start!")
 
    def tearDown(self):
        print("end!")
 
    @ddt.data(*test_data1)
    def test_ddt1(self, data):
        print(data)
 
    @ddt.data(*test_data2)
    def test_ddt2(self, data):
        print(data)
 
 
if __name__ == "__main__":
    unittest.main()
