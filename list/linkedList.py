#coding:utf-8

class Node:
	def __init__(self,val,next=None):
		self.data = val
		self.next = next

class LinkedList:
	def __init__(self, data=None):
		if data == None:
			self.head = None 
		else:
			self.head = Node(data[0])
			p = self.head
			for i in data[1:]:
				node = Node(i)
				p.next = node
				p = p.next

	def __len__(self):
		if self.head is None:
			return 0
		p = self.head
		result = 0
		while p != None:
			p = p.next
			result += 1
		return result

	def __getitem__(self, index):
		if index < 0 or index >= len(self):
			return None
		if self.head is None:
			return None
		p = self.head
		j = 0
		while j < index:
			p = p.next
			j += 1
		return p.data


	def __setitem__(self, index, value):
		if index < 0 or index >= len(self):
			return 
		if self.head is None:
			return 

		p = self.head
		j = 0
		while j < index:
			p = p.next
			j += 1
		p.data = value


	def is_empty(self):
		return self.head == None

	def clear(self):
		self.head = None

	def append(self, data):
		if data is None:
			return
		self.insert(len(self), data)


	def insert(self, index, data):
		if data is None:
			return
		if index < 0 or index > len(self):
			return

		if index == 0:
			#插在头部
			q = Node(data, self.head)
			self.head = q
			return

		p = self.head
		post = self.head
		j = 0
		while j < index:
			post = p
			p = p.next
			j += 1
			if index == j:
				q = Node(data, p)
				post.next = q
				
	def insert_front(self, data):
		if data is None:
			return

		self.insert(0, data)

	def delete(self, index):
		if index < 0 or index >= len(self):
			return None
		if self.head is None:
			return None
		if index == 0:
			result = self.head.data
			self.head = self.head.next
			return result
		p = self.head

		j = 0
		while j < index-1:
			p = p.next
			j += 1
		result = p.next.data
		p.next = p.next.next
		return result

	def get_all_data(self):
		result = []
		p = self.head
		while p is not None:
			result.append(p.data)
			p = p.next
		return result

	def reverse(self):
		if self.head is None or self.head.next is None:
			return
		cur = self.head
		pre = None
		while cur:
			tmp = cur.next
			cur.next = pre
			pre = cur
			cur = tmp
		self.head = pre




from nose.tools import assert_equal

class TestLinkedList:
	def test_is_empty(self):
		l1 = LinkedList()
		assert_equal(l1.is_empty(), True)
		l2 = LinkedList([3,5,7,9,2,4,6,8])
		assert_equal(l2.is_empty(), False)
		print "success test is_empty"

	def test_len(self):
		l1 = LinkedList()
		assert_equal(len(l1), 0)
		l2 = LinkedList([1])
		assert_equal(len(l2),1)
		l3 = LinkedList([1,2,3])
		assert_equal(len(l3),3)
		print "success test __len__"

	def test_insert(self):
		l1 = LinkedList()
		l1.insert(0,3)
		assert_equal(len(l1), 1)

		l1.insert(-2,4)   #插入失败则不插
		assert_equal(len(l1), 1)

		l1.insert(2,4)    #插入失败则不插
		assert_equal(len(l1), 1)

		l1.insert(1,4)
		assert_equal(len(l1),2)

		print "success test insert"

	def test_insert_front(self):
		l1 = LinkedList()
		l1.insert_front(3)
		assert_equal(l1.head.data, 3)
		l1.insert_front(4)
		assert_equal(l1.head.data, 4)
		assert_equal(l1.head.next.data, 3)
		print "success test insert_front"

	def test_append(self):
		l1 = LinkedList()
		l1.append(2)
		assert_equal(l1.head.data, 2)
		l1.append(5)
		assert_equal(l1.head.data, 2)
		assert_equal(l1.head.next.data, 5)
		print "success test append"

	def test_getitem(self):
		l1 = LinkedList()
		assert_equal(l1[0],None)
		l2 = LinkedList([88,77,66])
		assert_equal(l2[-1], None)
		assert_equal(l2[0],88)
		assert_equal(l2[1],77)
		assert_equal(l2[2],66)
		assert_equal(l2[3],None)

		print "success test __getitem__"

	def test_setitem(self):
		l1 = LinkedList()
		l1[0] = 88
		assert_equal(l1[0], None)
		
		l1 = LinkedList([88,77,66])
		l1[1] = 99
		assert_equal(l1[1], 99)

		print "success test __setitem__"

	def test_delete(self):
		l1 = LinkedList([11,22,33])
		assert_equal(l1.delete(0),11)
		assert_equal(l1.get_all_data(), [22,33])
		l2 = LinkedList([11,22,33])
		assert_equal(l2.delete(1),22)
		assert_equal(l2.get_all_data(), [11,33])
		l3 = LinkedList([11,22,33])
		assert_equal(l3.delete(2),33)
		assert_equal(l3.get_all_data(), [11,22])



		print "success test delete"

	def test_get_all_data(self):
		l1 = LinkedList()
		assert_equal(l1.get_all_data(), [])
		l2 = LinkedList([11,22,33])
		assert_equal(l2.get_all_data(), [11,22,33])
		print "success test get_all_data"

	def test_reverse(self):
		l1 = LinkedList([11,22,33,44,55])
		l1.reverse()
		assert_equal(l1.get_all_data(),[55,44,33,22,11])
		print "success test reverse"





def main():
	test = TestLinkedList()
	test.test_is_empty()
	test.test_len()
	test.test_insert()
	test.test_insert_front()
	test.test_append()
	test.test_getitem()
	test.test_setitem()
	test.test_delete()
	test.test_get_all_data()
	test.test_reverse()
	

if __name__ == "__main__":
	main()
