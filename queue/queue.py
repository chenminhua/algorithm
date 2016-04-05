#coding:utf
class Queue:
	def __init__(self,datas=[]):
		self.datas = datas

	def __len__(self):
		return len(self.datas)

	def isEmpty(self):
		return len(self) == 0

	def enqueue(self, data):
		self.datas.append(data)

	def dequeue(self):
		return self.datas.pop(0) if not self.isEmpty() else None

	def peek(self):
		return self[0] if not self.isEmpty() else None

	def __getitem__(self,i):
		return self.datas[i]

	def __setitem__(self,i,y):
		self.datas[i] = y



from nose.tools import assert_equal

def Test():
	q = Queue([1,2,3])
	assert_equal(len(q), 3)
	assert_equal(q.isEmpty(), False)
	q.enqueue(4)
	assert_equal(q.datas, [1,2,3,4])
	assert_equal(q.peek(), 1)
	assert_equal(q.dequeue(), 1)
	assert_equal(q.datas, [2,3,4])

	q = Queue()
	assert_equal(q.isEmpty(), True)
	assert_equal(q.peek(), None)
	assert_equal(q.dequeue(), None)
	print "success"


Test() 