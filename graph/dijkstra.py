#coding:utf-8
MAX_NUM = 1000000
import copy
class Edge:
	def __init__(self, neighbour=None, distance=MAX_NUM):
		self.neighbour = neighbour
		self.distance = distance

class Vertex:
	def __init__(self,label=None):
		self.neighbours = []
		self.visited = False
		self.label =label
		self.path = None
	
class Graph:
	def __init__(self):
		self.vertexs = []
		self.edges = []

	def addVertex(self, label):
		vertex = Vertex(label)
		self.vertexs.append(vertex)
		return vertex

	def addEdge(self, source, dest, weight):
		edge = Edge(dest, weight)
		source.neighbours.append(edge)

def dijkstra(graph, source):
	for vertex in graph.vertexs:
		vertex.dist = MAX_NUM
		vertex.known = False
	source.dist = 0
	while True:
		#smallest unknown distance vertex
		min_dist = MAX_NUM
		v = Vertex()
		for node in graph.vertexs:
			if node.known == False and node.dist < min_dist:
				min_dist = node.dist
				v = node

		if not v.label:
			break
		v.known = True

		for edge in v.neighbours:
			if not edge.neighbour.known:
				if v.dist + edge.distance < edge.neighbour.dist:
					edge.neighbour.dist = v.dist + edge.distance
					edge.neighbour.path = v


def print_path(v):
	if v.path:
		print_path(v.path)
	print v.label


from nose.tools import assert_equal

def test():
	graph = Graph()
	nodeA = graph.addVertex('A')
	nodeB = graph.addVertex('B')
	nodeC = graph.addVertex('C')
	nodeD = graph.addVertex('D')
	nodeE = graph.addVertex('E')
	nodeF = graph.addVertex('F')

	graph.addEdge(nodeA, nodeB, 6)
	graph.addEdge(nodeA, nodeC, 3)
	graph.addEdge(nodeB, nodeC, 2)
	graph.addEdge(nodeB, nodeD, 5)
	graph.addEdge(nodeC, nodeD, 3)
	graph.addEdge(nodeC, nodeE, 4)
	graph.addEdge(nodeD, nodeE, 2)
	graph.addEdge(nodeD, nodeF, 3)
	graph.addEdge(nodeE, nodeF, 5)

	dijkstra(graph, nodeA)

	assert_equal(nodeA.dist,0)
	assert_equal(nodeB.dist,6)
	assert_equal(nodeC.dist,3)
	assert_equal(nodeD.dist,6)
	assert_equal(nodeE.dist,7)
	assert_equal(nodeF.dist,9)

	print "success"


test()
