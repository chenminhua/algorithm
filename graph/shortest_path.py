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

def shortPath(graph, source):
	#无权图的最短路径问题
	distance = 0
	source.distance = distance
	result = {source.label: distance}
	queue = Queue()
	queue.enqueue(source)
	while not queue.isEmpty():
		node = queue.dequeue()
		for edge in node.neighbours:
			if not edge.neighbour.visited:
				edge.neighbour.visited = True
				edge.neighbour.distance = node.distance + 1
				queue.enqueue(edge.neighbour)
				result[edge.neighbour.label] = node.distance + 1
	return result

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

	print shortPath(graph, nodeA)



test()