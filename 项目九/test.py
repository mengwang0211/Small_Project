# -*- coding:utf-8 -*-
import re, urllib2

request = urllib2.urlopen('http://www.imooc.com/course/list')
buf = request.read()
listurl = re.findall(r'src=.+\.jpg',buf)
#listurl = re.findall(r'http:.+\.jpg',buf)
#print listurl

res=[]
for url in listurl:
    a= re.findall(r'http:.+\.jpg',url)
    res.append(a[0])

for url in res:
    print url
index = 0
for url in res:
    f = open(str(index)+'.jpg', 'wb')
    request = urllib2.urlopen(url)
    buf = request.read()
    f.write(buf)
    index = index + 1
#记得关闭文件
f.close()