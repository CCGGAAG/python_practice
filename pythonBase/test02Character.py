'''
Created on 2017年4月5日

@author: test
''' 
#列表list,可以改变列表元素 [ ]
list=["java",123,2.222]
print(list)
print(list[1:2])

#元组Tuple，元组的元素不能修改 ( )
tuple = ("java",123,2.222)
print(tuple)
'''
tup1 = ()    空元组
tup2 = (20,)  一个元素，需要在元素后添加逗号
虽然tuple的元素不可改变，但它可以包含可变的对象，比如list列表。
'''

#集合Set  无序不重复元素的序列 { }      空集合用（）
student={1,2,3,4,5,6,7}
if('1' in student):
    print("1在集合里")
else:
    print("1不在集合里")
#集合的运算：
#      -  差集        |  并集        & 交集         ^两个集合不同时存在的元素（交集对于并集的补集）
a={1,2,3};b={3,6,8}
print(a|b)
a={'123156asdfasd'};b={'156sfaweffds'}
print(a | b)
#set方法进行集合运算
a = set('abracadabra')
b = set('alacazam')

print(a)

print(a - b)     # a和b的差集

print(a | b)     # a和b的并集

print(a & b)     # a和b的交集

print(a ^ b)     # a和b中不同时存在的元素


