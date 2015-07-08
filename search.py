#!/usr/bin/python
#-*- coding: utf-8 -*-
#encoding=utf-8

#这是一个基于BeautifulSoup的简单爬虫程序

import urllib2
import urllib
import os
from BeautifulSoup import BeautifulSoup
def getAllImageLink():
    html = urllib2.urlopen('http://www.dbmeinv.com/').read()
    soup = BeautifulSoup(html)

    liResult = soup.findAll('li',attrs={"class":"span3"})

    for li in liResult:
        imageEntityArray = li.findAll('img')
        
        for image in imageEntityArray:
            link = image.get('src')
            imageName = image.get('title')
            filesavepath = '/Users/rth/Desktop/zhaopian/%s.jpg' % imageName 
            urllib.urlretrieve(link,filesavepath)
            print filesavepath 

if __name__ == '__main__':
    getAllImageLink()