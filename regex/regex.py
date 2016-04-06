#coding:utf-8
import re

#match
print re.match(r'^\d{3}\-\d{3,8}','010-12345')   #匹配成功则返回一个Match对象

print re.match(r'^\d{2}\-','010-12345')    #匹配失败则返回None

#group
m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')
print m
print m.group(0)  #010-12345
print m.group(1)  #010
print m.group(2)  #12345

#正则匹配是贪婪匹配
print re.match(r'^(\d+)(0*)$','102300').groups()   #('102300', '')

#加?可以变成非贪婪匹配



