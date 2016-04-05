#coding:utf
class Edge:
	#IdCounter = 1
	def __init__(self, source=None, dest=None, weight=0):
		self.source = source
		self.dest = dest
		self.weight = weight
		#self.uniqueId = IdCounter
		#IdCounter += 1

class Vertex:
	def __init__(self, data):
		self.data = data
		self.edges = []

	def connectTo(self,dest,weight):
		self.edges.append(Edge(source=self,dest=dest,weight=weight))

	def connectBetween(self, dest, weight):
		self.connectTo(dest, weight)
		dest.connectTo(self, weight)

	def isConnectedTo(self, dest):
		for e in self.edges:
			if e.dest == dest:
				return True
		return False

from nose.tools import assert_equal

def test():
	"""
	1 --> 2 --> 3 --> 4 <--> 5
		  |                  ^
		  |__________________|
	"""
	v1 = Vertex(1)
	v2 = Vertex(2)
	v3 = Vertex(3)
	v4 = Vertex(4)
	v5 = Vertex(5)
	
	v1.connectTo(v2, 1.0)
	v2.connectTo(v3, 1.0)
	v3.connectTo(v4, 4.5)
	v4.connectBetween(v5, 2.8)
	v2.connectTo(v5, 3.2)

	assert_equal(v1.isConnectedTo(v2), True)
	assert_equal(v1.isConnectedTo(v3), False)
	assert_equal(v2.isConnectedTo(v1), False)
	assert_equal(v4.isConnectedTo(v5), True)
	assert_equal(v5.isConnectedTo(v4), True)

	print "success"

test()
