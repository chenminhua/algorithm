#coding:utf
class Heap:
	##最小堆（父亲比儿子小）
    def __init__(self, datas=[]):
        self.datas = datas
        self.buildheap()

    def buildheap(self):
    	for i in range(len(self) / 2 - 1, -1, -1):
    		self.percolateDown(i)

    def percolateDown(self, i):
    	tmp = self[i]
    	while i*2+1 < len(self):
    	    child = 2*i+1
    	    if child+1 < len(self) and self[child+1] < self[child]:
    	        child += 1
    	    if self[child] < tmp:
    	    	self[i] = self[child]
    	    	i = child
    	    else:
    	    	break
    	self[i] = tmp

    def __len__(self):
    	return len(self.datas)

    def isEmpty(self):
    	return len(self) == 0

    def findMin(self):
    	return self[0] if not self.isEmpty() else None

    def deleteMin(self):
    	if self.isEmpty():
    		return None
    	minItem = self[0]
    	self[0] = self.datas.pop()
    	self.percolateDown(0)
    	return minItem

    def insert(self, data):
    	hole = len(self)
    	self.datas.append(data)
    	while hole > 0 and data < self[(hole+1)/2-1]:
    		self[hole] = self[(hole + 1)/2 -1]
    		hole = (hole+1)/2-1
    	self[hole] = data

    def __getitem__(self,i):
    	return self.datas[i]

    def __setitem__(self,i,y):
    	self.datas[i] = y



from nose.tools import assert_equal

def test():
	h = Heap([32,68,19,65,24,26,13,21,16,31])
	assert_equal(h.datas, [13, 16, 19, 21, 24, 26, 32, 68, 65, 31])
	
	h.insert(14)
	assert_equal(h.datas, [13, 14, 19, 21, 16, 26, 32, 68, 65, 31, 24])
	assert_equal(h.deleteMin(),13)
	assert_equal(h.datas, [14, 16, 19, 21, 24, 26, 32, 68, 65, 31])

	print "success"

test()

