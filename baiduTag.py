#!/usr/bin/env python
# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup


web = requests.get("http://www.baidu.com/s")
web.encoding = 'utf-8'
# print(type(web))
soup = BeautifulSoup(web.text, 'lxml')
print(soup.prettify())

# s=0;
testlist = []
for tag in soup.find_all(True):
    # s=s+1
    # print(tag.name)
    testlist.append(tag.name)
    # print(type('tagname'))
print("total nametag = %d%s" % (len(soup.find_all(True)),(".")))
# print(s)

# testset = set(testlist)
# for tagname in testset:
#     print("the %s"% (tagname),"has found %d"% (testlist.count(tagname)))

testset = set(testlist)
for tagname in testset:
    print(testlist.count(tagname)," of ", "(",tagname,")", " in HTML tag of baidu.com")