filename = "input_day3.txt"

def extractArg(claim):
	arguments = claim.split(" ")
	claimNum = int(arguments[0][1:])

	topleft = arguments[2][:-1].split(",")
	topleftX = int(topleft[0])
	topleftY = int(topleft[1])

	dimension = arguments[3].split("x")
	width = int(dimension[0])
	height = int(dimension[1])

	return (topleftX, topleftY, width, height, claimNum)


if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	'''
	# ========= Part 1 ==========
	cloth = [[0 for col in range(10000)] for row in range(10000)]
	overlap = 0
	for claim in data:
		arguments = extractArg(claim)
		topleftX = arguments[0]
		topleftY = arguments[1]
		width = arguments[2]
		height = arguments[3]

		# mark cloth, cloth stores how many times a square inch has been claimed
		for x in range(0, width):
			for y in range(0, height):
				if (cloth[topleftX + x][topleftY + y] == 1):
					overlap += 1
				cloth[topleftX + x][topleftY + y] += 1
	print("Part 1: " + str(overlap))
	'''

	# ========= Part 2 ==========
	cloth = [[0 for col in range(1000)] for row in range(1000)]
	nonOverlappingClaims = set()
	for claim in data:
		arguments = extractArg(claim)
		topleftX = arguments[0]
		topleftY = arguments[1]
		width = arguments[2]
		height = arguments[3]
		claimNum = arguments[4]

		# mark cloth, cloth stores claim number each square inch
		isOverlapping = False
		for x in range(0, width):
			for y in range(0, height):
				if (cloth[topleftX + x][topleftY + y] != 0):
					# has already been claimed
					isOverlapping = True
					# remove previous claim number from set
					if cloth[topleftX + x][topleftY + y] in nonOverlappingClaims:
						nonOverlappingClaims.remove(cloth[topleftX + x][topleftY + y])
				# mark with claim number
				cloth[topleftX + x][topleftY + y] = claimNum
		if (not isOverlapping):
			nonOverlappingClaims.add(claimNum)

	answer = nonOverlappingClaims.pop()
	print("Part 2: " + str(answer))

