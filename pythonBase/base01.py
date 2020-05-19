'''
Created on 2017年4月4日
@author: test
'''
#coding=utf-8
import keyword                 #导入关键字
keyword.kwlist

#print输出-输出字符类型-不换行输出
n= ("python"); m=("java");p="123"
print("学习%s"%n)
print("学习：",n,m,p,end="")
print()

#为多个变量赋值
a=b=c=1
print(a,b,c,end="")
print()
a,b,c=1,2,"end"
print(a,b,c,end="")
print()
# input 输入
m=input("准备学习：")
print("接下来学习：%r"%m)

#if 条件语句
aName = 62
if  aName >90:
    print("优秀")
elif aName > 60 :
    print("及格")
else:
    print("挨打")
    
#for 循环
for i in range(5,9):
    print(i) 

    



