#coding:utf-8
class Stack:
	def __init__(self,datas=[]):
		self.datas = datas

	def __len__(self):
		return len(self.datas)

	def isEmpty(self):
		return len(self) == 0

	def push(self,data):
		self.datas.append(data)

	def pop(self):
		return self.datas.pop() if not self.isEmpty() else None

	def peek(self):
		return self[len(self.datas)-1] if not self.isEmpty() else None

	def __getitem__(self,i):
		return self.datas[i]

	def __setitem__(self,i,y):
		self.datas[i] = y


from nose.tools import assert_equal

def Test():
	s = Stack([1,2,3])
	assert_equal(len(s),3)
	s.push(4)
	assert_equal(s.datas, [1,2,3,4])
	assert_equal(s.peek(), 4)
	assert_equal(s.pop(),4)
	assert_equal(s.datas, [1,2,3])
	s = Stack()
	assert_equal(s.isEmpty(),True)
	assert_equal(s.pop(),None)
	assert_equal(s.peek(),None)
	print "success"

Test()