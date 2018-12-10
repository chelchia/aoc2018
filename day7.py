from llist import dllist, dllistnode
import heapq

filename = "input_day7.txt"

class AdjacencyList: 
	def __init__(self):
		self.adjlist = {}
		self.prereq = {}
		self.isMarked = {}
		self.startingNodes = set()

	def addNode(self, node):
		self.adjlist[node] = dllist()
		self.isMarked[node] = False
		self.startingNodes.add(node)

	def addDependency(self, nodeFrom, nodeTo):
		if nodeFrom not in self.adjlist:
			self.addNode(nodeFrom)
		self.adjlist[nodeFrom].append(nodeTo)
		if nodeTo not in self.adjlist:
			self.addNode(nodeTo)
		if nodeTo in self.startingNodes:
			self.startingNodes.remove(nodeTo)

		if nodeTo not in self.prereq:
			self.prereq[nodeTo] = dllist()
		self.prereq[nodeTo].append(nodeFrom)

	def getDependencies(self, node):
		return self.adjlist[node]

	def isNodeMarked(self, node):
		return self.isMarked[node]

	def markNode(self, node):
		self.isMarked[node] = True

	def getStartingNode(self):
		nodes = []
		for node in self.startingNodes:
			nodes.append(node)
		return nodes

	def isPrereqComplete(self, node):
		for prereq in self.prereq[node]:
			if not self.isMarked[prereq]:
				return False
		return True

	def printGraph(self):
		print(self.adjlist)

def extractDependency(instruction):
	words = instruction.split(" ")
	return (words[1], words[7])


if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	# ========= Part 1 ==========
	#construct graph
	graph = AdjacencyList()
	for instruction in data:
		dep = extractDependency(instruction)
		graph.addDependency(dep[0], dep[1])

	graph.printGraph()
	#create heap for traversal of graph. pop from heap. for every node, add neighbours to heap. repeat
	heap = graph.getStartingNode()
	for node in heap:
		graph.markNode(node)
	sequence = ""
	while True:
		try:
			# print(heap)
			currNode = heapq.heappop(heap)
			graph.markNode(currNode)
			sequence += currNode
			for neighbour in graph.getDependencies(currNode):
				if (not graph.isNodeMarked(neighbour)) and graph.isPrereqComplete(neighbour):
					#not marked so not traversed, add to queue
					# print(currNode, neighbour)
					heapq.heappush(heap, neighbour)
		except IndexError:
			print("\nend of heap")
			break

	print(sequence)


		
