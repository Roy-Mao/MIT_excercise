from pylab import *
import random, math
def throwDarts(numDarts):
	inCircle = 0
	estimates = []
	for darts in xrange(1, numDarts + 1, 1):
		x = random.random()
		y = random.random()
		if math.sqrt(x*x + y*y) <= 1.0:
			inCircle += 1
			piGuess = 4*(inCircle/float(darts))
			estimates.append(piGuess)
	xAxis = arange(1, len(estimates)+1)
	semilogx(xAxis, estimates)
	titleString = 'Estimations of pi, final estimate: ' + str(piGuess)
	title(titleString)
	xlabel('Number of Darts Thrown')
	ylabel('Estimate of pi')
	axhline(3.14159)
	return 4*(inCircle/float(numDarts))
throwDarts(10000)
show()

	
