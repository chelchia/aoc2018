filename = "input_day8.txt"
# filename = "test.txt"

def processInputIntoList(data):
	numbers = data[0].split(" ")
	length = len(numbers)
	for i in range(length):
		numbers[i] = int(numbers[i])
	return numbers

def calcParentMetadata(node, metadata):
	summ = 0
	for entry in metadata:
		if node.getChild(entry) != -1:
			summ += node.getChild(entry)
	return summ

class NodeInfo:
	def __init__(self, numChild, numMeta, index):
		self.numChild = numChild
		self.numMeta = numMeta
		self.index = index #index of the node info in the input list
		self.children = []

	def addChild(self, child):
		self.children.append(child)

	def getChild(self, childNum):
		if childNum > len(self.children):
			return -1
		else:
			return self.children[childNum - 1]

if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	# ========= Part 1 ==========
	# Use a stack to maintain info about parent nodes. 
	# traverse down the list over each node, pushing until you hit a leaf node.
	# calculate the leaf node and remove entirely from input list
	# Then pop the stack and update parent info (one less child)
	numbers = processInputIntoList(data)
	length = len(numbers)

	stack = []
	pointer = 0
	sumMetadata = 0
	while pointer < length:
		if numbers[pointer] == 0:
			#leaf node. calculate metadata
			numMetadata = numbers[pointer + 1]
			sumMetadata += sum(numbers[pointer + 2: pointer + 2 + numMetadata])

			#slice leaf node and metadata from numbers
			numbers = numbers[:pointer] + numbers[(pointer + 2 + numMetadata):]
			length = len(numbers)

			#reset pointer to parent node. decrement parent node number of child
			if stack == []:
				#only node left
				break
			else:
				parent = stack.pop()
				pointer = parent.index
				numbers[pointer] -= 1 #pointer is now pointing to parent. decrement because one less child
		else:
			#parent node. push onto stack
			node = NodeInfo(numbers[pointer], numbers[pointer + 1], pointer)
			stack.append(node)
			pointer += 2

	print(sumMetadata)

	# ========= Part 2 ==========
	numbers = processInputIntoList(data)
	length = len(numbers)

	stack = []
	pointer = 0
	currNode = None
	childMetadata = 0
	while pointer < length:
		# print(pointer, numbers, currNode)
		if numbers[pointer] == 0:
			#leaf node. calculate metadata
			numMetadata = numbers[pointer + 1]
			metadata = numbers[pointer + 2: pointer + 2 + numMetadata]
			if currNode != None:
				#is a parent node
				childMetadata = calcParentMetadata(currNode, metadata)
			else:
				childMetadata = sum(metadata)

			#slice leaf node and metadata from numbers
			numbers = numbers[:pointer] + numbers[(pointer + 2 + numMetadata):]
			length = len(numbers)

			#reset pointer to parent node. decrement parent node number of child
			if stack == []:
				#only node left
				break
			parent = stack.pop()
			currNode = parent
			currNode.addChild(childMetadata)
			# print(currNode.children)

			pointer = parent.index
			numbers[pointer] -= 1 #pointer is now pointing to parent. decrement because one less child
		else:
			#parent node. push onto stack
			if currNode != None:
				node = currNode
			else:
				node = NodeInfo(numbers[pointer], numbers[pointer + 1], pointer)
			stack.append(node)
			pointer += 2
			currNode = None

	print(childMetadata)



