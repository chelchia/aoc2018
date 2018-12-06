filename = "input_day5.txt"

def isUpperLowerPair(char1, char2):
	return char1.upper() == char2.upper() and \
		((char1.isupper() and char2.islower()) or (char1.islower() and char2.isupper()))

def react(polymer):
	length = len(polymer)
	i = 0
	while i < length - 1:
		if isUpperLowerPair(polymer[i], polymer[i + 1]):
			polymer = polymer[:i] + polymer[i + 2:]
			length -= 2
			if i > 0:
				i -= 1
		else:
			i += 1

	return length - 1 # answer is length - 1, last character is '\n'

def removeLetter(polymer, letter):
	length = len(polymer)
	i = 0
	while i < length - 1:
		if polymer[i].lower() == letter:
			polymer = polymer[:i] + polymer[i + 1:]
			length -= 1
		else:
			i += 1

	return polymer


if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	# ========= Part 1 ==========
	polymer = data[0]
	length = react(polymer)
	print("Part 1: " + str(length))

	# ========= Part 2 ==========
	alphabet = list("abcdefghijklmnopqrstuvwxyz")
	shortestLength = len(polymer)
	for letter in alphabet:
		improvedPolymer = removeLetter(polymer, letter)
		length = react(improvedPolymer)
		if length < shortestLength:
			shortestLength = length

	print("Part 2: " + str(shortestLength))


