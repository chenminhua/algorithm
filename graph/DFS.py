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


def DFS(graph, source):
	result = [source.label]
	source.visited = True
	for edge in source.neighbours:
		if not edge.neighbour.visited:
			result += DFS(graph, edge.neighbour)
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

	assert_equal(DFS(graph, nodeA),['a', 'c', 'f', 'g', 'b', 'd', 'e', 'h'])
	print "success"

test()