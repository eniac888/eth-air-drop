#!/usr/bin/python
# -*- coding: UTF-8 -*-
import urllib, urllib2
import  re;
from bs4 import BeautifulSoup
"""
todo:
    1.Ajava
"""

#获取网址的网页
def getHtml(num):
    # bai  0xbbd7b196d8ce1f56b2901145b3fcfc42cded5596
    # destroy  0xbbd7b196d8ce1f56b2901145b3fcfc42cded5596
    addr = "0xbbd7b196d8ce1f56b2901145b3fcfc42cded5596"
    values = {'a': addr, 'p': num}
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    url = 'https://etherscan.io/txs';
    textmod = urllib.urlencode(values)
    req = urllib2.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)
    res = urllib2.urlopen(req)
    res = res.read()
    soup = BeautifulSoup(res)

    return soup



def printTableInfo(body):
    for tr in body.findAll('tr'):
        content=[]
        for td in tr.findAll('td'):
            content.append(td.getText())
           # print  td.getText(),
        print(content)
# 打印交易的头部信息
def printTbody(num):
    soup = getHtml(num)
    body= soup.table.tbody
    printTableInfo(body)

# 输出交易的信息
def printTableHeader():
    soup = getHtml(1)
    body= soup.table.thead
    printTableInfo(body)


#获取总的页数
def getnumberPages():
    soup=getHtml(1)
    page=int(soup.find_all("div", attrs={"class": "row"})[0].findAll("span")[2].getText()[-3:])
    return page
# 获取交易数
def getnumberTransaction():
    soup=getHtml(1)
    page=soup.find_all("div", attrs={"class": "row"})[0].findAll("span")[1].getText()
    totalCount = re.sub("\D", "", page)
    return  int(totalCount)
print getnumberTransaction()
print getnumberPages()

# 获取所有的交易  --MAIN----
if __name__ == '__main__':
    for i in range(1,getnumberPages()+1):
        printTbody(i)

