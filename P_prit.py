#!/usr/bin/env python
# coding=utf-8

# D:\python-3.6.5-embed-amd64\python.exe

import os
print (os.getcwd())
print("/******************************/")


from urllib.request import urlopen
html = urlopen("https://www.bing.com/")
print(html.read())



"""
class MyClass:
	i = 12345
	def f(self):
		return "hello world"

x = MyClass() # Instantiate the class
print("MyClass attribute i : ",x.i)
print("MyClass method	 f : ",x.f())
"""
# print("MyClass method	 f : ",x.f)	#<bound method MyClass.f of <__main__.MyClass object at 0x0000000002E67320>>

##############################################
# f = open("test.txt", "w+", encoding="utf-8")
# print ("文件名为: ", f.name)
# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )
# print (f.tell());#输出当前指针位置
# f.seek(os.SEEK_SET)
# print (f.read())
# f.flush()
# f.close()#？？？--- 存在疑问，未解决
# io.UnsupportedOperation: not readable #open打开一个文件，此时调用的是w写入模式，下面使用read是没有权限的，你得使用w+读写
##############################################

# '!a' (使用 ascii()), '!s' (使用 str()) 和 '!r' (使用 repr()) 可以用于在格式化某个值之前对其进行转化:



"""
s = "Hello GK"
print(str(s))    #函数返回一个用户易读的表达形式
                #会输出运算结果，会屏蔽转义字符
print(repr(s))    #产生一个解释器易读的表达形式
print(1/7)       
print(str(1/7))   
print(repr(1/7))
print('{} : {}!'.format('runoob','test')) #runoob : test!
"""

"""
import sys
print (sys.argv)
print (sys.modules)
print (sys.platform)
print (sys.path)
"""
# from file.pythonFileName import moudleName
# import module
"""
import math

content = dir(math)

print (content)
"""

"""
#name space & scope
Money = 2000
def MoneyAdd():
    global Money   #avoid UnboundLocalError
    Money = Money + 1
print (Money)
MoneyAdd()
print (Money)
"""

"""
import sys
def Fibonacci(n):
    a,b,counter = 0,1,0
    while True:
       if (counter > n):
          return
       yield a
       a, b = b, a + b
       counter += 1

f = Fibonacci(10) # f is a iterator,return from generator

while True:
    try:
       print(next(f),end=" ")
    except StopIteration:
       sys.exit()
"""

#id(variable)  adress view

"""
for var in range(5): #traverse list
    print(var)       #range(start,end,step)
"""
 
"""
# parameters of the order is no effect
def printTest(name,age=35):
    print("name : ",name)
    print("age  : ",age)
    return

printTest(10,10)
printTest(name = 10,age = 11)
printTest(age = 11,name = 10)
"""

"""
a = 100
print(isinstance(a,int))# type judge
"""

"""
print("/******************************/")

def printme(str):
    print( str )
    return

printme("def function test\n")
"""
'''
import sys
#from sys import argv,path

for i in sys.argv:
    print(i)
print ("\n python path",sys.path)
'''

''' # outside input
a=sys.argv[1]
print (a)

print ("Hello world")
'''
'''
# Fibonacci serie
a, b = 0,1
while b < 10:
    print(b,end=",")
    a, b = b, a+b
'''

'''
var1 = 100
print("\n IF Test \n")
# if
if var1:
    print ("1 - if True")
    print (var1)

var2 = 0
if var2:
    print ("2 - if true")
    print (var2)
print ("Good bye!")
'''
'''
age = int(input("please input your dog age :"))
print("")
if age < 0 :
    print("Error")
elif age == 1 :
    print("equal a 14 years man\n")
elif age == 2 :
    print("equal a 22 years man\n")
elif age > 1 :
    human = 22 + (age -2)*5
    print ("human ",human)
input("Exit by Enter")
'''

print (r"\******************************\ ") #r 不转义

