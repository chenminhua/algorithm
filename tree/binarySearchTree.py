#coding:utf-8
"""
二叉查找树的定义是，对于树中的每一个节点，其左子树中的所有元素都比它小，右子树中的所有元素都比它大
"""
class Node:
	def __init__(self, element, left=None, right=None):
		self.element = element
		self.left = left
		self.right = right

class BinarySearchTree:
	def __init__(self, root=None):
		self.root = root

	def clear(self):
		self.root = None

	def isEmpty(self):
		return self.root == None

	def contain(self, x, node):
		if node is None:
			return False
		if x < node.element:
			return self.contain(x, node.left)
		elif x > node.element:
			return self.contain(x, node.right)
		else:
			return True

	def findMin(self, node):
		if node == None:
			return None
		elif node.left == None:
			return node
		return self.findMin(node.left)


	def findMax(self, node):
		if node == None:
			return None
		elif node.right == None:
			return node
		return self.findMax(node.right)

	def insert(self, x, node):
		#不考虑相同元素出现
		if node == None:
			return Node(x)
		if x < node.element:
			node.left = self.insert(x,node.left)
		elif x > node.element:
			node.right = self.insert(x,node.right)
		return node

	def remove(self, x, node):
		if node == None:
			return node
		if x < node.element:
			node.left = self.remove(x, node.left)
		elif x > node.element:
			node.right = self.remove(x, node.right)
		elif node.left != None and node.right != None:
			node.element = self.findMin(node.right).element
			node.right = self.remove(node.element, node.right)
		else:
			node = node.left if (node.left is not None) else node.right

		return node			



	def print_tree(self, node):
		if node != None:
			self.print_tree(node.left)
			print node.element
			self.print_tree(node.right)	

	def post_order_print_tree(self, node):
		if node != None:
			self.post_order_print_tree(node.left)
			self.post_order_print_tree(node.right)
			print node.element	

	def pre_order_print_tree(self, node):
		if node != None:
			print node.element
			self.pre_order_print_tree(node.left)
			self.pre_order_print_tree(node.right)


from nose.tools import assert_equal

class TestBinarySearchTree:
	def test_insert(self):
		bst1 = BinarySearchTree()
		bst1.root = bst1.insert(11,bst1.root)
		bst1.print_tree(bst1.root)
		bst1.root = bst1.insert(30,bst1.root)
		bst1.print_tree(bst1.root)
		bst1.root = bst1.insert(3,bst1.root)
		bst1.print_tree(bst1.root)

	def test_findMin(self):
		bst1 = BinarySearchTree()
		bst1.root = bst1.insert(11,bst1.root)
		bst1.root = bst1.insert(30,bst1.root)
		bst1.root = bst1.insert(3,bst1.root)
		assert_equal(bst1.findMin(bst1.root).element, 3)

		print "success test findMin"

	def test_findMax(self):
		bst1 = BinarySearchTree()
		bst1.root = bst1.insert(11,bst1.root)
		bst1.root = bst1.insert(30,bst1.root)
		bst1.root = bst1.insert(3,bst1.root)
		assert_equal(bst1.findMax(bst1.root).element, 30)

		print "success test findMax"

	def test_remove(self):
		bst1 = BinarySearchTree()
		bst1.root = bst1.insert(9, bst1.root)
		bst1.root = bst1.insert(3, bst1.root)
		bst1.root = bst1.insert(2, bst1.root)
		bst1.root = bst1.insert(4, bst1.root)
		bst1.root = bst1.insert(6, bst1.root)
		bst1.root = bst1.insert(7, bst1.root)
		bst1.root = bst1.insert(8, bst1.root)
		bst1.remove(3,bst1.root)
		bst1.print_tree(bst1.root)

	def test_post_order(self):
		bst1 = BinarySearchTree()
		bst1.root = bst1.insert(6, bst1.root)
		bst1.root = bst1.insert(3, bst1.root)
		bst1.root = bst1.insert(2, bst1.root)
		bst1.root = bst1.insert(4, bst1.root)
		bst1.root = bst1.insert(9, bst1.root)
		bst1.root = bst1.insert(7, bst1.root)
		bst1.root = bst1.insert(8, bst1.root)
		print "\n post_order"
		bst1.post_order_print_tree(bst1.root)

	def test_pre_order(self):
		bst1 = BinarySearchTree()
		bst1.root = bst1.insert(6, bst1.root)
		bst1.root = bst1.insert(3, bst1.root)
		bst1.root = bst1.insert(2, bst1.root)
		bst1.root = bst1.insert(4, bst1.root)
		bst1.root = bst1.insert(9, bst1.root)
		bst1.root = bst1.insert(7, bst1.root)
		bst1.root = bst1.insert(8, bst1.root)
		print "\n pre_order"
		bst1.pre_order_print_tree(bst1.root)



def main():
	
	test = TestBinarySearchTree()
	test.test_insert()
	test.test_findMin()
	test.test_findMax()
	test.test_remove()
	test.test_post_order()
	test.test_pre_order()


if __name__ == "__main__":
	main()