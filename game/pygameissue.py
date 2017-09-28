def square_root(n):
	assert(n >= 1), 'n must be bigger than 1'
	accuracy = 0.01
	ini = 3.0
	xinterse = (ini/2 + n/(2*ini))
	guesqr = xinterse ** 2
	difference = abs(guesqr - n)
	while difference > accuracy:
		guess = xinterse
		xinterse = (guess/2 + n/(2*guess))
		guesqr = xinterse ** 2
		difference = abs(guesqr - n)
	else:
		return xinterse
print square_root(1)




			


