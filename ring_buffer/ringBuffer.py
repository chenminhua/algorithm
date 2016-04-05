#coding:utf-8
class RingBuffer:
	def __init__(self, capacity):
		self.datas = [0] * capacity
		self.capacity = capacity
		self.readIndex = 0
		self.writeIndex = 0
		self.availableSpaceForReading = 0
		self.availableSpaceForWriting = capacity

	def isEmpty(self):
		return self.availableSpaceForReading == 0

	def isFull(self):
		return self.availableSpaceForWriting == 0

	def read(self):
		if self.isEmpty():
			return
		self.readIndex += 1
		self.availableSpaceForWriting += 1
		self.availableSpaceForReading -= 1
		return self[(self.readIndex-1) % self.capacity]

	def write(self,data):
		if self.isFull():
			return
		self[self.writeIndex % self.capacity] = data
		self.writeIndex += 1
		self.availableSpaceForReading += 1
		self.availableSpaceForWriting -= 1
		

	def __getitem__(self,i):
		return self.datas[i]

	def __setitem__(self,i,data):
		self.datas[i] = data

from nose.tools import assert_equal

def test():
	rb = RingBuffer(5)

	rb.write(12)
	rb.write(13)
	rb.write(14)
	rb.write(15)
	rb.write(16)
	rb.write(17)   #应该写不进去的
	assert_equal((rb.availableSpaceForWriting,rb.availableSpaceForReading),(0,5))
	assert_equal(rb.read(),12)
	assert_equal(rb.read(),13)
	assert_equal(rb.read(),14)
	assert_equal(rb.read(),15)
	assert_equal(rb.read(),16)
	assert_equal(rb.read(),None)
	assert_equal((rb.availableSpaceForWriting,rb.availableSpaceForReading),(5,0))

	print "success"

test()

