#coding:utf-8
class Edge:
	def __init__(self, neighbour=None):
		self.neighbour = neighbour

class Vertex:
	def __init__(self,label):
		self.neighbours = []
		self.visited = False
		self.label =label
	
class Graph:
	def __init__(self):
		self.vertexs = []
		self.edges = []

	def addVertex(self, label):
		vertex = Vertex(label)
		self.vertexs.append(vertex)
		return vertex

	def addEdge(self, source, dest):
		edge = Edge(dest)
		source.neighbours.append(edge)


class Queue:
	def __init__(self, datas=[]):
		self.datas = datas
	def __len__(self):
		return len(self.datas)
	def isEmpty(self):
		return len(self) == 0
	def enqueue(self,data):
		self.datas.append(data)
	def dequeue(self):
		return self.datas.pop(0) if not self.isEmpty() else None
	def peek(self):
		return self.datas[0] if not self.isEmpty() else None


def BFS(graph, source):
	queue = Queue()
	queue.enqueue(source)

	result = [source.label]
	source.visited = True

	while not queue.isEmpty():
		node = queue.dequeue()
		for edge in node.neighbours:
			node = edge.neighbour
			if not node.visited:
				queue.enqueue(node)
				node.visited = True
				result.append(node.label)
	return result

from nose.tools import assert_equal

def test():
	graph = Graph()
	nodeA = graph.addVertex("a")
	nodeB = graph.addVertex("b")
	nodeC = graph.addVertex("c")
	nodeD = graph.addVertex("d")
	nodeE = graph.addVertex("e")
	nodeF = graph.addVertex("f")
	nodeG = graph.addVertex("g")
	nodeH = graph.addVertex("h")

	
	graph.addEdge(nodeA, nodeC)
	graph.addEdge(nodeA, nodeB)
	graph.addEdge(nodeB, nodeD)
	graph.addEdge(nodeB, nodeE)
	graph.addEdge(nodeC, nodeF)
	graph.addEdge(nodeC, nodeG)
	graph.addEdge(nodeE, nodeH)
	graph.addEdge(nodeE, nodeF)
	graph.addEdge(nodeF, nodeG)

	assert_equal(BFS(graph, nodeA),['a', 'c', 'b', 'f', 'g', 'd', 'e', 'h'])

	print "success"

	


test()












