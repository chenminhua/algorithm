class Node:
	def __init__(self,data,next=None,prev=None):
		self.data = data
		self.next = next
		self.prev = prev

class DLinkedList:
	def __init__(self,datas=None):
		if datas is None:
			self.head = None
			self.tail = None
			return 
		if len(datas) == 1:
			node = Node(datas[0])
			self.head = node
			self.tail = self.head
			return
		self.head = Node(datas[0])
		self.tail = Node(datas[-1])
		p = self.head
		for data in datas[1:-1]:
			q = Node(data)
			p.next = q
			q.prev = p
			p = p.next
		p.next = self.tail
		self.tail.prev = p

	def __len__(self):
		if self.head is None:
			return 0
		p = self.head
		res = 0
		while p is not None:
			p = p.next
			res += 1
		return res

	def is_empty(self):
		return self.head == None

	def clear(self):
		self.head = None
		self.tail = None

	def get_all_data(self):
		result = []
		p = self.head
		while p is not None:
			result.append(p.data)
			p = p.next
		return result

	def insert(self, index, data):
		if data is None:
			return
		if index < 0 or index > len(self):
			return

		if self.is_empty() and index == 0:
			q = Node(data)
			self.head = q
			self.tail = self.head
			return

		if index == 0:
			q = Node(data, self.head, None)
			self.head.prev = q
			self.head = q
			return 
		if index == len(self):
			q = Node(data, None, self.tail)
			self.tail.next = q
			self.tail = q
			return 

		if index <= len(self) / 2:
			j = 0
			p = self.head
			post = self.head
			while j < index:
				post = p
				p = p.next
				j += 1
			q = Node(data, p, post)
			post.next = q
			p.prev = q
			return
		if index > len(self) / 2:
			j = len(self)
			p = self.tail
			post = self.tail
			while j > index:
				post = p
				p = p.prev
				j -= 1
			q = Node(data, post, p)
			post.prev = q
			p.next = q

	def unshift(self,data):
		self.insert(0,data)
		
	def append(self,data):
		self.insert(len(self),data)

	def delete(self, index):
		if index < 0 or index >= len(self):
			return 

		if index == 0:
			result = self.head.data
			self.head = self.head.next
			return result

		if index == len(self) - 1:
			result = self.tail.data
			self.tail = self.tail.prev
			return result

		if index <= len(self)/2:
			j = 0
			p = self.head
			post = self.head
			while j < index:
				post = p
				p = p.next
				j += 1
			post.next = p.next
			p.next.prev = post
			return p.data
		if index > len(self)/2:
			j = len(self)-1
			p = self.tail
			post = self.tail
			while j > index:
				post = p
				p = p.prev
				j = j-1
			post.prev = p.prev
			p.prev.next = post
			return p.data

	def pop(self):
		if self.is_empty():
			return 
		result = self.tail.data
		self.tail = self.tail.prev
		self.tail.next = None
		return result

	def shift(self):
		if self.is_empty():
			return
		result = self.head.data
		self.head = self.head.next
		self.head.prev = None
		return result

	





from nose.tools import assert_equal

class TestDLinkedList:

	def test_len(self):
		l1 = DLinkedList()
		assert_equal(len(l1),0)
		l2 = DLinkedList([123,456])
		assert_equal(len(l2),2)
		print "success test len"

	def test_get_all_data(self):
		l1 = DLinkedList()
		assert_equal(l1.get_all_data(), [])
		l2 = DLinkedList([123,456])
		assert_equal(l2.get_all_data(), [123,456])
		print "success test get_all_data"

	def test_clear(self):
		l1 = DLinkedList([123,456])
		l1.clear()
		assert_equal(l1.get_all_data(), [])
		print "success test clear"

	def test_unshift(self):
		l1 = DLinkedList()
		l1.unshift(33)
		assert_equal(l1.get_all_data(),[33])
		l1.unshift(44)
		assert_equal(l1.get_all_data(),[44,33])
		print "success test unshift"

	def test_append(self):
		l1 = DLinkedList()
		l1.append(33)
		assert_equal(l1.get_all_data(),[33])
		l1.append(44)
		assert_equal(l1.get_all_data(),[33,44])
		print "success test append"

	def test_delete(self):
		l1 = DLinkedList([1,2,3,4,5])
		l1.delete(2)
		assert_equal(l1.get_all_data(), [1,2,4,5])
		print "success test delete"

	def test_pop(self):
		l1 = DLinkedList([1,2,3,4,5])
		l1.pop()
		assert_equal(l1.get_all_data(), [1,2,3,4])
		print "success test pop"

	def test_shift(self):
		l1 = DLinkedList([1,2,3,4,5])
		l1.shift()
		assert_equal(l1.get_all_data(), [2,3,4,5])
		print "success test shift"
		



def main():
	test = TestDLinkedList()
	test.test_len()
	test.test_get_all_data()
	test.test_clear()
	test.test_unshift()
	test.test_append()
	test.test_delete()
	test.test_pop()
	test.test_shift()

if __name__ == "__main__":
	main()


