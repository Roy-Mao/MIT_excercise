def factorial(n):
	print "function called with num: ", n
	if n == 1:
		result = 1
		return result
	else:
		result = n * factorial(n - 1)
		print "Intermediate output: ", result
		return result
print factorial(4)