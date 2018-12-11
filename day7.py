from llist import dllist, dllistnode
import heapq

filename = "input_day7.txt"

class Node:
	def __init__(self, node):
		self.neighbours = dllist()
		self.prereq = dllist()
		self.isMarked = False
		self.time = 60 + ord(node) - 64

	def addDependency(self, nodeTo):
		self.neighbours.append(nodeTo)

	def addPrereq(self, nodeFrom):
		self.prereq.append(nodeFrom)


class AdjacencyList: 
	def __init__(self):
		self.adjlist = {}
		self.prereq = {}
		# self.isMarked = {}
		self.startingNodes = set()

	def addNode(self, node):
		self.adjlist[node] = Node(node)
		# self.isMarked[node] = False
		self.startingNodes.add(node)

	def addDependency(self, nodeFrom, nodeTo):
		if nodeFrom not in self.adjlist:
			self.addNode(nodeFrom)
		if nodeTo not in self.adjlist:
			self.addNode(nodeTo)
		if nodeTo in self.startingNodes:
			self.startingNodes.remove(nodeTo)

		#add dependency
		self.adjlist[nodeFrom].addDependency(nodeTo)
		#add prereq
		self.adjlist[nodeTo].addPrereq(nodeFrom)

	def getDependencies(self, node):
		return self.adjlist[node].neighbours

	def isNodeMarked(self, node):
		return self.adjlist[node].isMarked

	def markNode(self, node):
		self.adjlist[node].isMarked = True

	def getStartingNode(self):
		nodes = []
		for node in self.startingNodes:
			nodes.append(node)
		return nodes

	def isPrereqComplete(self, node):
		for prereq in self.adjlist[node].prereq:
			if not self.adjlist[prereq].isMarked:
				return False
		return True

	def printGraph(self):
		for node in self.adjlist:
			print(node)
			print(self.adjlist[node].neighbours)

	def reset(self):
		for node in self.adjlist:
			self.adjlist[node].isMarked = False

	def getTime(self, node):
		return self.adjlist[node].time

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

	# Topo sort
	#create heap for traversal of graph. pop from heap. for every node, add neighbours to heap. repeat
	heap = graph.getStartingNode()
	for node in heap:
		graph.markNode(node)
	sequence = ""
	while True:
		try:
			currNode = heapq.heappop(heap)
			graph.markNode(currNode)
			sequence += currNode
			for neighbour in graph.getDependencies(currNode):
				if (not graph.isNodeMarked(neighbour)) and graph.isPrereqComplete(neighbour):
					#not marked so not traversed, add to queue
					heapq.heappush(heap, neighbour)
		except IndexError:
			print("\nend of heap")
			break

	print(sequence)

	# ========= Part 2 ==========
	numWorkers = 5
	workers = [0 for i in range(numWorkers)]
	jobs = ['.' for i in range(numWorkers)]

	graph.reset()
	heap = graph.getStartingNode()
	time = 0
	jobsDone = 0
	while jobsDone < 26:
		print(time, workers, jobs, heap)
		#assign jobs to free workers
		for worker in range(numWorkers):
			if workers[worker] == 0:
				try:
					#if heap is not empty,
					currNode = heapq.heappop(heap)
					workers[worker] = graph.getTime(currNode)
					jobs[worker] = currNode
					# graph.markNode(currNode)
				except IndexError:
					#heap is empty, do nothing. just wait.
					lol = 1

		#decrement time working for workers
		for worker in range(numWorkers):
			if jobs[worker] != '.':
				#has a job
				workers[worker] -= 1

		#when job is done, add neighbours is possible
		for worker in range(numWorkers):
			if workers[worker] == 0 and jobs[worker] != '.':
				job = jobs[worker]
				graph.markNode(job)
				for neighbour in graph.getDependencies(job):
					if (not graph.isNodeMarked(neighbour)) and graph.isPrereqComplete(neighbour) and not neighbour in heap:
						#not marked so not traversed, add to queue
						heapq.heappush(heap, neighbour)
				jobs[worker] = '.'
				jobsDone += 1

		time += 1

	print(time)


		
