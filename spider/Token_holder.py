import sys

reload(sys)
sys.setdefaultencoding("utf8")

import urllib, urllib2
import re
import csv
from bs4 import BeautifulSoup
import time


def getHtml(num):
    # bai  0xbbd7b196d8ce1f56b2901145b3fcfc42cded5596
    # destroy  0xbbd7b196d8ce1f56b2901145b3fcfc42cded5596
    addr = "0xbbd7b196d8ce1f56b2901145b3fcfc42cded5596"
    values = {'a': addr, 's': '2100000000', 'p': num}
    header_dict = {'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko'}
    url = 'http://etherscan.io/token/generic-tokenholders2';
    textmod = urllib.urlencode(values)
    req = urllib2.Request(url='%s%s%s' % (url, '?', textmod), headers=header_dict)
    res = urllib2.urlopen(req)
    res = res.read()
    soup = BeautifulSoup(res)
    return soup


def numberpage():
    soup = getHtml(1)
    page = str(soup.select("#PagingPanel > span")[0].getText())[-2:]
    return int(page)


def printTokenHolder(num):
    soup=getHtml(num)
    tables = soup.findAll('table')
    tab = tables[0]
    for tr in tab.findAll('tr'):
        for td in tr.findAll('td'):
            print td.getText(),
        print

if __name__ == '__main__':
    pages=numberpage()
    for num in range(1,pages+1):
        printTokenHolder(num)
