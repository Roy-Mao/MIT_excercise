
# import math, random, pylab

# class Location(object):
# 	def __init__(self, x, y):
# 		self.x = float(x)
# 		self.y = float(y)

# 	def move(self, xc, yc):
# 		return Location(self.x + float(xc), self.y + float(yc))

# 	def getCoords(self):
# 		return self.x, self.y

# 	def getDist(self, other):
# 		ox, oy = other.getCoords()
# 		xDist = self.x - ox
# 		yDist = self.y - oy
# 		return math.sqrt(xDist ** 2 + yDist ** 2)

# class CompassPt(object):
# 	possibles = ["N", "S", "E", "W"]
# 	def __init__(self, pt):
# 		if pt in self.possibles:
# 			self.pt = pt
# 		else:
# 			raise ValueError("in CompassPt.__init__")
# 	def move(self, dist):
# 		if self.pt == "N":
# 			return (0, dist)
# 		elif self.pt == "S":
# 			return (0, -dist)
# 		elif self.pt == "E":
# 			return (dist,0)
# 		elif self.pt == "W":
# 			return (-dist, 0)
# 		else:
# 			raise ValueError("in CompassPt.move")

# class Field(object):
# 	def __init__(self, drunk, loc):
# 		self.drunk = drunk
# 		self.loc = loc

# 	def move(self, cp, dist):
# 		oldLoc = self.loc
# 		xc, yc = cp.move(dist)
# 		self.loc = oldLoc.move(xc, yc)

# 	def getLoc(self):
# 		return self.loc

# 	def getDrunk(self):
# 		return self.drunk

# class Drunk(object):
# 	def __init__(self, name):
# 		self.name = name
# 	def move(self, field, time = 1):
# 		if field.getDrunk() != self:
# 			raise ValueError("Drunk.move called with drunk not in fields")

# 		for i in range(time):
# 			pt = CompassPt(random.choice(CompassPt.possibles))
# 			field.move(pt, 1)

# def performTrial(time, f):
# 	start = f.getLoc()
# 	distances = [0.0]
# 	for t in range (1, time + 1):
# 		f.getDrunk().move(f)
# 		newLoc = f.getLoc()
# 		distance = newLoc.getDist(start)
# 		distances.append(distance)
# 	return distances

# """drunk = Drunk("Roy Ryan")
# for i in range(1):
# 	f = Field(drunk, Location(0, 0))
# 	distances = performTrial(1, f)
# 	pylab.plot(distances)
# 	pylab.title("random walk")
# 	pylab.xlabel("how many times tried (average-value)")
# 	pylab.ylabel("distance from the original")
# pylab.show()


# """
# def performsim(time, numTrials):
# 	distLists = []
# 	for trial in range(numTrials):
# 		d = Drunk("Drunk" + str(trial))
# 		f = Field(d, Location(0, 0))
# 		distances = performTrial(time, f)
# 		distLists.append(distances)
# 	return distLists

# def ansQuest(numTime, numTrials):
# 	means = []
# 	distLists = performsim(numTime, numTrials)
# 	for t in range(numTime + 1):
# 		tot = 0.0
# 		for distL in distLists:
# 			tot += distL[t]
# 		means.append(tot/(len(distLists)))
# 		print tot

# 	pylab.figure()
# 	pylab.plot(means)
# 	pylab.title("random walk")
# 	pylab.xlabel("how many times tried (average-value)")
# 	pylab.ylabel("distance from the original")

# ansQuest(500, 200)	
# pylab.show()

for i in range(101):
	print i




