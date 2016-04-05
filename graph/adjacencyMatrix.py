#coding:utf
indexCounter = 0
class Graph:
	##不通的写0吧
	def __init__(self, matrix=[]):
		self.matrix = matrix

	def createVertex(self, data):
		size = len(self.matrix)
		for row in self.matrix:
			row.append(0)
		self.matrix.append([0]*(size+1))
		return Vertex(data)

	def connect(self, source, dest, weight):
		self.matrix[source.index][dest.index] = weight

	def weightBetween(self, source, dest):
		return self.matrix[source.index][dest.index] 

class Vertex:
	def __init__(self, data):
		global indexCounter
		self.data = data
		self.index = indexCounter
		indexCounter += 1


from nose.tools import assert_equal

def test():
	graph = Graph()
	v1 = graph.createVertex(1)
	v2 = graph.createVertex(2)
	v3 = graph.createVertex(3)
	v4 = graph.createVertex(4)
	v5 = graph.createVertex(5)

	graph.connect(v1, v2, 1.0)
	graph.connect(v4, v5, 3.0)

	print graph.matrix

test()