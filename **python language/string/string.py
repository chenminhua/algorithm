#coding:utf-8
"""
常见错误类型的继承关系
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""
#index, rindex
a="123abc321abc"
try:
	print a.index("abcd")   #抛出ValueError
except ValueError as e:
	print e
print a.index("abc")   #返回3
print a.rindex("abc")   #返回9

#find, rfind
a = "abcdebc"
print a.find("abd")  #-1表示没找到
print a.find("bc")   #返回1
print a.rfind("bc")  #返回5



#ord
print ord("A")   #65
try:
	print ord("😂")
except TypeError as e:
	print e

#capitalize
a = "abc"
b = a.capitalize()  #不改变原字符串，但是会返回新字符串并将其首字符大写
print a,b

#center
a = "abc"
b = a.center(11,"#")
print b   # 返回####abc####

#count
a = "abcba"
print a.count("a")    #2
print a.count("bc")   #1
print a.count("c")    #1
print a.count("d")    #0

#startswith, endswith
a = "abcde"
print a.endswith("cde")  #True

#format
print "the sum of 1 + 2 is {0}".format(1+2)

#isalnum, isalpha, isdigit
print "1234".isalnum()  #True
print "abc".isalnum()   #True
print "1234abc#".isalnum()  #False
print "abc".isalpha()  #True
print "123".isdigit()  #True

#islower, isupper, isspace
print "abc#".islower()  #True
print " 	".isspace() #True
print "ABC #@".isupper() #True

#join
print "/".join(["","etc","hosts"])  #/etc/hosts

#lstrip  删除开头字符，默认删除空字符
#rstrip  删除结尾字符，默认删除空字符
#strip   删除开头和结尾字符
a = "		spacious  	".lstrip()
print a
print "www.chenminhua.com".lstrip("w.")
print "blog.chenminhua.com".lstrip("blog.")
print "		spacious  	".rstrip()

#partition, rpartition
a = "WWW.CHENMINHUA.COM"
print a.partition(".")   #('WWW', '.', 'CHENMINHUA.COM')
print a.rpartition(".")  #('WWW.CHENMINHUA', '.', 'COM')
print a.partition("/")   #('WWW.CHENMINHUA.COM', '', '')

#replace
a = "WWW.CHENMINHUA.COM"
print a.replace('.', '/')  #WWW/CHENMINHUA/COM

#split, rsplit
a = "1 2 3  4 		5"
print a.split()      #['1', '2', '3', '4', '5']
a = "1,2,,3,4"
print a.split(",")   #['1', '2', '', '3', '4']











