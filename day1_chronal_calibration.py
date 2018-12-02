filename = "input_day1.txt"

def extractOp(change):
	return change[0]

def extractNum(change):
	return int(change[1:])

def addChange(frequency, change):
	operation = extractOp(change)
	number = extractNum(change)
	if operation == "-":
		frequency -= number
	elif operation == "+":
		frequency += number
	else:
		print("invalid operation")
	return frequency


if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	# ========= Part 1 ==========
	frequency = 0
	for change in data:
		frequency = addChange(frequency, change)
	print("Part 1: " + str(frequency))

	# ========= Part 2 ==========
	frequency = 0
	prevFrequencies = {} #dictionary to store previous frequencies
	prevFrequencies[0] = 1
	matchFound = False
	while True:
		for change in data:
			frequency = addChange(frequency, change)
			if frequency in prevFrequencies:
				matchFound = True
				break
			else:
				prevFrequencies[frequency] = 1
		if matchFound:
			break
	print("Part 2: " + str(frequency))

	close(filename)


