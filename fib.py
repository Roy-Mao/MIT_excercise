count_num = 0
def fib(n):
	global count_num 
	count_num += 1
	print "function called with num: ", n

	if n <= 2:
		result = 1
		return result
	else:
		result = fib(n - 1) + fib(n - 2) 
		return result
print "The final result is: " + str(fib(7))
print "count number is: ", count_num












