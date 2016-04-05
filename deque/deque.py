#coding:utf
class Deque:
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

    def enqueueFront(self, data):
        self.datas.insert(0, data)

    def dequeueBack(self):
        return self.datas.pop() if not self.isEmpty() else None

    def peekFront(self):
        return self[0] if not self.isEmpty() else None

    def peekBack(self): 
    	return self[len(self)-1]  if not self.isEmpty() else None

    def __getitem__(self,i):
    	return self.datas[i]

    def __setitem__(self,i,y):
    	self.datas[i] = y


from nose.tools import assert_equal

def Test():
	d = Deque([1,2,3,4,5])
	assert_equal(d.isEmpty(), False)
	d.enqueue(6)
	assert_equal(d.datas, [1,2,3,4,5,6])
	d.enqueueFront(7)
	assert_equal(d.datas, [7,1,2,3,4,5,6])
	assert_equal(d.peekFront(), 7)
	assert_equal(d.peekBack(), 6)
	assert_equal(d.dequeueBack(), 6)
	assert_equal(d.dequeue(), 7)
	assert_equal(d.datas, [1,2,3,4,5])

	d = Deque()
	assert_equal(d.isEmpty(), True)
	assert_equal(d.peekBack(),None)
	assert_equal(d.peekFront(),None)
	assert_equal(d.dequeue(),None)
	assert_equal(d.dequeueBack(),None)

	print "success"

Test()


