a="123abc321abc"
try:
	print a.index("abcd")
except BaseException as e:
	print "Exception"
print a.index("abc")

"""
常见错误类型的继承关系
https://docs.python.org/3/library/exceptions.html#exception-hierarchy
"""