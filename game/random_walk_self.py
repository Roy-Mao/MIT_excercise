import random
import math
import matplotlib.pyplot as plt
import numpy as np

def random_move(): # returns a list representing the direction by one unit
	east = [1.0, 0]
	west = [-1.0, 0]
	north = [0, 1.0]
	south = [0, -1.0]
	options = [east, west, north, south]
	direction = random.choice(options)
	return direction

def current_point(stepNum):  # tell how many steps we should move
    x = 0
    y = 0
    Dlist = []
    for n in range(stepNum):
        direction = random_move()
        x += direction[0]
        y += direction[1]
        squaDis = x ** 2 + y ** 2
        distance = math.sqrt(squaDis)
        Dlist.append(distance)
    return Dlist

def plot_graph(trialTime,stepNum):
    Slist = []
    Dlist = current_point(stepNum)
    Length = len(Dlist)
    Flist = []
    for t in range(trialTime):
		Dlist = current_point(stepNum)
		Slist.append(Dlist)
    for i in range(Length):
		sum = 0
		for s in Slist:
			sum += s[i]
			average = round((float(sum / len(Slist))) , 5)
		Flist.append(average)
    return Flist



def average_graph(trialTime, stepNum):
    Flist = plot_graph(trialTime,stepNum)
    plt.plot(Flist)
    plt.xlabel('Stepsnumber')
    plt.ylabel('Distance')
    plt.show()

average_graph(3000, 10)
