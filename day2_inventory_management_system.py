filename = "input_day2.txt"

def countLetters(id):
	letterCounter = {}
	for letter in id:
		if letter in letterCounter:
			letterCounter[letter] += 1
		else:
			letterCounter[letter] = 1
	return letterCounter

def hasTwice(dic):
	if 2 in dic.values():
		return True
	else:
		return False

def hasThrice(dic):
	if 3 in dic.values():
		return True
	else:
		return False

def printDict(dic):
	for i in dic:
		print i, dic[i]

def diffByOne(string, string2):
	diff = 0
	for i in range(0, len(string)):
		if (string[i] != string2[i]):
			diff += 1
	return diff == 1

def extractCommonLetters(string, string2):
	for i in range(0, len(string)):
		if (string[i] != string2[i]):
			return string[: i] + string[i + 1 :]


if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	# ========= Part 1 ==========
	twice = 0
	thrice = 0
	for id in data:
		letterCounter = countLetters(id)
		if hasTwice(letterCounter):
			twice += 1
		if hasThrice(letterCounter):
			thrice += 1
	checksum = twice * thrice
	print("Part 1: " + str(checksum))

	# ========= Part 2 ==========
	correctIdFound = False
	for id in data:
		for id2 in data:
			if diffByOne(id, id2):
				correctIdFound = True
				common = extractCommonLetters(id,id2)
				break
		if correctIdFound:
			break
	print("Part 2: " + common)


