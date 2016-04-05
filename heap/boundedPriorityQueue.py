#coding:utf
class LinkedListNode:
    def __init__(self,data,next=None):
        self.data = data
        self.next = next


class boundPriorityQueue:
    def __init__(self,head=None,capacity=10):
        self.head = head
        self.capacity = capacity
        self.length = 1 if head else 0

    def __len__(self):
        return self.length

    def isEmpty(self):
    	return len(self) == 0

    def peek(self):
    	return self.head.data if self.head else None

    def enqueue(self, data):
    	if self.isEmpty():
    		self.head = LinkedListNode(data)
    		self.length = 1
    		return

    	p = self.head
    	while p.next:
    		if p.data < data and p.next.data > data:
    			break
    		p = p.next

    	if self.length == self.capacity and p.data < data and not p.next:
    		return  #队列满了，而且入队失败

    	l = LinkedListNode(data)
    	l.next = p.next
    	p.next = l

    	if self.length < self.capacity:   #队列未满
    		self.length += 1
    		return
    	else:    #队列满了，入队成功
    		while p.next.next:
    			p = p.next
    		p.next = None

    def dequeue(self):
        if not self.head:
            return None
        if len(self) == 1: 
        	self.head, result, self.length = None, self.head.data, 0
        	return result
        p = self.head
        i = 0
        while i < self.length:
            p = p.next
            i += 1
        result = p.data
        
        self.length -= 1
        return result

    def getAll(self):
    	if self.isEmpty():
    		return None
    	res = []
    	p = self.head
    	while p:
    		res.append(p.data)
    		p = p.next
    	return res



from nose.tools import assert_equal

def test():
    head = LinkedListNode(1)
    bpq = boundPriorityQueue(head,capacity=3)
    assert_equal(bpq.isEmpty(),False)
    assert_equal(bpq.peek(),1)
    assert_equal(bpq.dequeue(),1)
    assert_equal(bpq.peek(), None)
    assert_equal(bpq.isEmpty(), True)

    bpq.enqueue(1)
    assert_equal(len(bpq),1)
    assert_equal(bpq.peek(),1)
    bpq.enqueue(9)
    bpq.enqueue(5)
    assert_equal(bpq.getAll(),[1,5,9])
    bpq.enqueue(4)
    assert_equal(bpq.getAll(),[1,4,5])
    assert_equal(len(bpq),3)


    print "success"


test()


        

