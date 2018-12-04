filename = "input_day4.txt"

class Guard:
	def __init__(self, id):
		self.id = id
		self.totalMinAsleep = 0;
		self.tracker = [0 for x in range(60)]

	#increments the tracker for the period he's asleep and updates total time
	def recordSleep(self, start, end):
		for i in range(start, end):
			self.tracker[i] += 1
		self.totalMinAsleep = self.totalMinAsleep + (end - start)

	#returns a tuple of minute in which the guard was asleep the most number of times,
	#and number of times he was asleep during that minute
	def findMinuteAsleepMost(self):
		minuteAsleepMost = -1
		maximum = 0
		for minute in range(0,60):
			if self.tracker[minute] > maximum:
				minuteAsleepMost = minute
				maximum = self.tracker[minute]
		return (minuteAsleepMost, self.tracker[minuteAsleepMost])

	def printTracker(self):
		for minute in range(0,60):
			print(minute, self.tracker[minute])


def parseRecord(record):
	arguments = record.split(" ")
	date = int(arguments[0][-2:])
	minute = int(arguments[1][3:5])
	if arguments[2] == "Guard":
		description = "GUARD"
		guardId = int(arguments[3][1:])
	elif arguments[2] == "falls":
		description = "SLEEP"
		guardId = -1
	elif arguments[2] == "wakes":
		description = "WAKE"
		guardId = -1
	return (date, minute, description, guardId)


if __name__ == "__main__":
	#read input
	f = open(filename)
	data = f.readlines()

	# ========= Part 1 ==========
	#sort data
	data.sort()

	table = {} #maps id to Guard (guard info)

	mostAsleepGuard = -1
	mostTimeAsleep = 0

	currentId = -1 #current guard id
	startSleep = 0
	for record in data:
		description = parseRecord(record)[2]
		minute = parseRecord(record)[1]
		if description == "GUARD":
			id = parseRecord(record)[3]
			if id not in table:
				table[id] = Guard(id)
			currentId = id #set current guard id
		elif description == "SLEEP":
			startSleep = minute
		elif description == "WAKE":
			table[currentId].recordSleep(startSleep, minute)
			if table[currentId].totalMinAsleep > mostTimeAsleep:
				mostTimeAsleep = table[currentId].totalMinAsleep
				mostAsleepGuard = currentId

	minuteAsleepMost = table[mostAsleepGuard].findMinuteAsleepMost()[0]
	print("Part 1: " + str(mostAsleepGuard * minuteAsleepMost))

	# ========= Part 2 ==========
	mostNumOfTimesAsleep = 0
	minute = -1
	guardId = -1
	for guard in table:
		sleepyMinute = table[guard].findMinuteAsleepMost()
		if sleepyMinute[1] > mostNumOfTimesAsleep:
			mostNumOfTimesAsleep = sleepyMinute[1]
			minute = sleepyMinute[0]
			guardId = table[guard].id

	print("Part 1: " + str(guardId * minute))


