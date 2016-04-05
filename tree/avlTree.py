#coding:utf-8
class TreeNode:
	"""根节点的深度为1，叶子节点的高度为1，非叶子节点的高度为其子树高度的最大值加1"""
	def __init__(self, data, left=None, right=None, height=1):
		self.data = data
		self.left = left
		self.right = right
		self.height = height

	def __str__(self):
		return "tree node %s with height %d" % (self.data, self.height)

	info = __str__


def height(node):
	return node.height if node else 0

class AVLTree:
	def __init__(self, root=None):
		self.root = root

	def insertroot(self, data):
		self.root = self.insert(data, self.root)


	def insert(self, data=None, node=None):
		if not node:
			return TreeNode(data)
		if data < node.data:
			#插在左子树上
			node.left = self.insert(data, node.left)
			if (height(node.left) - height(node.right) == 2):
				if data < node.left.data:
					node = self.rotateWithLeftChild(node)
				else: 
					node = self.doubleWithLeftChild(node)
		else:
			#插在右子树上
			node.right = self.insert(data, node.right)
			if (height(node.right) - height(node.left) == 2):
				if data > node.right.data:
					node = self.rotateWithRightChild(node)
				else:
					node = self.doubleWithRightChild(node)
		node.height = max(height(node.left), height(node.right)) + 1;
		return node

	def rotateWithLeftChild(self, k2):
		"""
		在左子树的左儿子上插入导致不平衡后进行调整
		k2                    k1
	k1      Z     =>     X          k2          
  X   Y                           Y    Z
		"""
		k1 = k2.left
		k2.left = k1.right
		k1.right = k2
		k2.height = max(height(k2.left), height(k2.right)) + 1
		k1.height = max(height(k1.left), height(k2)) + 1
		return k1

	def doubleWithLeftChild(self, k3):
		"""
		  k3                       k3                         k2
    k1        D      =>       k2         D      =>      k1           k3
  A    k2                   k1   C                    A    B       C     D
      B  C                 A  B

		在左子树的右儿子上插入，导致不平衡，采用这种旋转方法
		"""
		k3.left = self.rotateWithRightChild( k3.left );
		return self.rotateWithLeftChild(k3);


	def rotateWithRightChild(self, k1):
		"""
		在右子树的右儿子上插入导致的不平衡后进行调整
		k1                         K2
	X	      k2        =>    K1         Z
            Y    Z          X    Y
        """
		k2 = k1.right;
		k1.right = k2.left;
		k2.left = k1;
		k1.height = max( height(k1.left), height(k1.right) ) + 1;
		k2.height = max( height(k1), height(k2.right)) + 1; 
		return k2;

	def doubleWithRightChild(self, k1):
		"""
		k1                       k1                                k2
	A         k3       =>   A           k2         =>         k1         k3
	       k2     D                   B     k3               A  B       C  D
		  B  C                             C  D
		"""
		k1.right = self.rotateWithLeftChild(k1.right);
		return self.rotateWithRightChild(k1);



from nose.tools import assert_equal

def test():
	"""
	测试左旋转
	5          2
   2    =>    1 5
  1  
	"""
	tn = TreeNode(5)
	t = AVLTree(tn)
	t.insertroot(2)
	t.insertroot(1)
	assert_equal(t.root.info(), "tree node 2 with height 2")
	assert_equal(t.root.left.info(), "tree node 1 with height 1")
	assert_equal(t.root.right.info(), "tree node 5 with height 1")

	"""
	测试右旋转
	2                       2
  1   5        =>        1      6    
        6                     5   7
          7
	"""
	t.insertroot(6)
	t.insertroot(7)
	assert_equal(t.root.info(), "tree node 2 with height 3")
	assert_equal(t.root.right.info(), "tree node 6 with height 2")
	assert_equal(t.root.right.left.info(), "tree node 5 with height 1")
	assert_equal(t.root.right.right.info(), "tree node 7 with height 1")

	"""
	测试插在左子树上的右子树
	5           3
   2    =>    2   5    
   	3
	"""
	tn = TreeNode(5)
	t = AVLTree(tn)
	t.insertroot(2)
	t.insertroot(3)
	assert_equal(t.root.info(), "tree node 3 with height 2")
	assert_equal(t.root.left.info(), "tree node 2 with height 1")
	assert_equal(t.root.right.info(), "tree node 5 with height 1")

	"""
	测试插在右子树的左儿子上
	 3                  3   
  2    5         =>   2     7
          9               5    9
         7
	"""
	t.insertroot(9)
	t.insertroot(7)
	assert_equal(t.root.info(), "tree node 3 with height 3")
	assert_equal(t.root.right.info(), "tree node 7 with height 2")
	assert_equal(t.root.right.left.info(), "tree node 5 with height 1")
	assert_equal(t.root.right.right.info(), "tree node 9 with height 1")


	print "success"

test()



