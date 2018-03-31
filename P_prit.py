#!/usr/bin/env python
# coding=utf-8

# D:\python-3.6.5-embed-amd64\python.exe
# 无限循环的部分进行检查    
import os
print (os.getcwd())
print("/******************************/")
print("git start 180330")


from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup
import re  # python regex module                                                                                                
# Charpter 1

html = urlopen( "http://www.pythonscraping.com/pages/page3.html")
bsObj = BeautifulSoup(html,"html.parser")


print(bsObj.findAll(lambda tag: len(tag.attrs) == 2)) #获取有两个属性的标签：
#lambda 存在是为了替换 regex


#regex  regular expression

# Attribute get
# myTag.attrs   #返回的是一个 Python 字典对象
# myImgTag.attrs["src"] 获取图片的资源位置 src


# image get
'''
images = bsObj.findAll("img",{"src":re.compile("\.\.\/img\/gifts/img.*\.jpg")}) #print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())
for image in images:
    print(image["src"])
'''

'''
aa*bbbbb(cc)*(d | )

a 后面跟着的 a*（读作 a 星）表示“重复任意次 a，包括 0 次”。
5 次 b
任意偶数个字符都可以编组，规则是用括号两个 c，然后跟一个星号，表示有任意次两个 c（也可以是 0 次）。
增加一个竖线（|） 在表达式里表示“这个或那个”---> d 或者是 空格

邮箱 : [A-Za-z0-9\._+]+@[A-Za-z]+\.(com|org|edu|net)

符　　号    含　　义                                                例　　子                   匹配结果
*           匹配前面的字符、子表达式或括号里的字符 0 次             a*b*                       aaaaaaaa， aaabbbbb，    bbbbbb
            或多次
+           匹配前面的字符、子表达式或括号里的字符至少1 次          a+b+                       aaaaaaab， aaabbbbb，abbbbbb
[]          匹配任意一个字符（相当于“任选一个”）                    [A-Z]*                     APPLE， CAPITALS，QWERTY
()          表达式编组（在正则表达式的规则里编组会优先运行）        (a*b)*                     a a a b a a b， a b a a a b，ababaaaaab
{m,n}       匹配前面的字符、子表达式或括号里的字符 m 到             a{2,3}b{2,3}               aabbb， aaabbb， aabb
            n 次（包含 m 或 n）
[^]         匹配任意一个不在中括号里的字符                          [^A-Z]*                    a p p l e， l o w e r c a s e，qwerty
|           匹配任意一个由竖线分割的字符、子表达式（注              b(a|i|e)d                  bad， bid， bed
            意是竖线，不是大字字母 I）
.           匹配任意单个字符（包括符号、数字和空格等）               b.d                       bad， bzd， b$d， b d
^           指字符串开始位置的字符或子表达式                        ^a                         apple， asdf， a
\           转义字符（把有特殊含义的字符转换成字面形式）              \.\ | \\                 . | \
$           经常用在正则表达式的末尾，表示“从字符串的               [A-Z]*[a-z]*$              ABCabc， zzzyx， Bob
            末端匹配”。如果不用它，每个正则表达式实际都
            带着“.*”模式，只会从字符串开头进行匹配。这
            个符号可以看成是 ^ 符号的反义词
?!          “不包含”。这个奇怪的组合通常放在字符或正则              ^((?![A-Z]).)*$            no-caps-here， $ymb0lsa4e f!ne
            表达式前面，表示字符不能出现在目标字符串里。
            这个符号比较难用，字符通常会在字符串的不同
            部位出现。如果要在整个字符串中全部排除某个
            字符，就加上 ^ 和 $ 符号


'''

'''
# .children
for child in bsObj.find("table",{"id":"giftList"}).children:
    print(child)
'''
# 父节点---》text
# print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())


# print(bsObj.find("table",{"id":"giftList"}).tr) #兄标签获取

###################未理解
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.previous_siblings:# 
    # print(sibling)#####
###################未理解
    
# 还有 next_sibling 和 previous_sibling 函数，与 next_siblings 和 previous_siblings的作用类似，只是它们返回的是单个标签，而不是一组标签。

# next_siblings() 函数可以让收集表格数据成为简单的事情，尤其是处理带标题行的表格：
# for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings:# 只会获得兄弟标签
    # print(sibling)
    
'''# Charpter 1
# 模拟请求
html = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj = BeautifulSoup(html)
nameList = bsObj.findAll("span",{"class":"green"})      # bsObj.findAll(tagName, tagAttributes)
                                                        # findAll(tag, attributes, recursive, text, limit, keywords)
                                                        #    find(tag, attributes, recursive, text, keywords)
                                                        # recursive 是一个布尔变量，为 True， findAll 就会根据你的要求去查找标签参数的所有子标签，以及子标签的子标签。如果为 # # # False， findAll 就只查找文档的一级标签。默认值是 True
for name in nameList:
    print(name.get_text())#get_text() 会把你正在处理的 HTML 文档中所有的标签都清除，然后返回一个只包含文字的字符串。 
    
nameList = bsObj.findAll(text = "the prince")       # 查找前面网页中包含“the prince” 内容的标签数量 
print ("\n",len(nameList))                          # 数量
'''

'''# Charpter 1
# 以下两种方式相同
nameList = bsObj.findAll(id="text")                 # 查找前面网页中包含“text” 内容的标签数量 
print ("\n",len(nameList))     
nameList = bsObj.findAll("",{"id":"text"})          # 查找前面网页中包含“text” 内容的标签数量 
print ("\n",len(nameList))        
'''

"""# Charpter 1
# class 保留关键字处理     
# bsObj.findAll(class="green") # 错误语法 #SyntaxError: invalid syntax
# 以下两种方式相同   
bsObj.findAll(class_="green") 
bsObj.findAll("",{"class":"green"}) 
"""

# BeautifulSoup 4 object: find findAll NavigableString:表示标签里的文字 Comment:注释标签， <!-- 像这样 -->

# 
"""
# Charpter 1
# html.title Get
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        print(e)    
		#return NULL
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")       # bsObj = BeautifulSoup(html.read())
        title = bsObj.title
    except attributeError as e:
        return None
    return title
urltest =  "http://www.rsks.czs.gov.cn/"   
title = getTitle(str(urltest))
if title == None:
    print("Title could not be found")
else:
    print(title)
"""   

# bsObj = BeautifulSoup(html.read())
# print(bsObj.head)
# print(bsObj.body)

#*******************************************************************************
    #Base Exercise
#*******************************************************************************
"""
class MyClass:
    i = 12345
    def f(self):
        return "hello world"

x = MyClass() # Instantiate the class
print("MyClass attribute i : ",x.i)
print("MyClass method    f : ",x.f())
"""
# print("MyClass method  f : ",x.f) #<bound method MyClass.f of <__main__.MyClass object at 0x0000000002E67320>>

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

