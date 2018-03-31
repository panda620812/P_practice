#!/usr/bin/env python
# coding=utf-8

# Python 的伪随机数（pseudorandom number）生成器用的是梅森旋转（Mersenne
# Twister）算法（https://en.wikipedia.org/wiki/Mersenne_Twister），它产生的随机数很难
# 预测且呈均匀分布，就是有点儿耗费 CPU 资源。真正好的随机数可不便宜！ 

# Python 默认的递归限制（程序递归地自我调用次数）是 1000 次    


# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.findAll("a"):
    # if 'href' in link.attrs:
        # print(link.attrs['href'])
        
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# html = urlopen("http://en.wikipedia.org/wiki/Kevin_Bacon")
# bsObj = BeautifulSoup(html)
# for link in bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$")):
    # if 'href' in link.attrs:
        # print(link.attrs['href'])
        
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import datetime
# import random   #random() 方法返回随机生成的一个实数，它在[0,1)范围内。 random.random()
# import re
# random.seed(datetime.datetime.now())
# def getLinks(articleUrl):
    # html = urlopen("http://en.wikipedia.org"+articleUrl)
    # bsObj = BeautifulSoup(html)
    # return bsObj.find("div", {"id":"bodyContent"}).findAll("a",href=re.compile("^(/wiki/)((?!:).)*$"))
# links = getLinks("/wiki/Kevin_Bacon")
# while len(links) > 0:
    # newArticle = links[random.randint(0, len(links)-1)].attrs["href"]   # random 模块的 randint()函数来生成随机数，你每次执行后都返回不同的数字（0 到 9）
    # print(newArticle)
    # links = getLinks(newArticle)
    
    
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# pages = set()
# def getLinks(pageUrl):
    # global pages
    # html = urlopen("http://en.wikipedia.org"+pageUrl)
    # bsObj = BeautifulSoup(html)
    # for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        # if 'href' in link.attrs:
            # if link.attrs['href'] not in pages:
            # #我们遇到了新页面
                # newPage = link.attrs['href']
                # print(newPage)
                # pages.add(newPage)
                # getLinks(newPage)
# getLinks("")    
    
# from urllib.request import urlopen
# from bs4 import BeautifulSoup
# import re
# pages = set()
# def getLinks(pageUrl):
    # global pages
    # html = urlopen("http://en.wikipedia.org"+pageUrl)
    # bsObj = BeautifulSoup(html)
    # try:
        # print(bsObj.h1.get_text())
        # print(bsObj.find(id="mw-content-text").findAll("p")[0])
        # print(bsObj.find(id="ca-edit").find("span").find("a").attrs['href'])
    # except AttributeError:
        # print("页面缺少一些属性！不过不用担心！ ")
    # for link in bsObj.findAll("a", href=re.compile("^(/wiki/)")):
        # if 'href' in link.attrs:
            # if link.attrs['href'] not in pages:
                ##我们遇到了新页面
                # newPage = link.attrs['href']
                # print("----------------\n"+newPage)
                # pages.add(newPage)
    # getLinks(newPage)
# getLinks("")

    
    
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import datetime
import random
pages = set()
random.seed(datetime.datetime.now())
# 获取页面所有内链的列表
def getInternalLinks(bsObj, includeUrl):
    internalLinks = []
    # 找出所有以"/"开头的链接
    for link in bsObj.findAll("a", href=re.compile("^(/|.*"+includeUrl+")")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in internalLinks:
                internalLinks.append(link.attrs['href'])
        return internalLinks
# 获取页面所有外链的列表
def getExternalLinks(bsObj, excludeUrl):
    externalLinks = []
    # 找出所有以"http"或"www"开头且不包含当前URL的链接
    for link in bsObj.findAll("a",href=re.compile("^(http|www)((?!"+excludeUrl+").)*$")):
        if link.attrs['href'] is not None:
            if link.attrs['href'] not in externalLinks:
                externalLinks.append(link.attrs['href'])
    return externalLinks
def splitAddress(address):
    addressParts = address.replace("http://", "").split("/") # 切片按照(parameter)
    return addressParts
def getRandomExternalLink(startingPage):
    html = urlopen(startingPage)
    bsObj = BeautifulSoup(html)
    externalLinks = getExternalLinks(bsObj, splitAddress(startingPage)[0])
    if len(externalLinks) == 0:
        internalLinks = getInternalLinks(startingPage)
        return getNextExternalLink(internalLinks[random.randint(0,len(internalLinks)-1)])
    else:
        return externalLinks[random.randint(0, len(externalLinks)-1)]
def followExternalOnly(startingSite):
    externalLink = getRandomExternalLink("http://oreilly.com")
    print("随机外链是："+externalLink)
    followExternalOnly(externalLink)
followExternalOnly("http://oreilly.com")    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    