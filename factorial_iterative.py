def factorial_iterative(n):
	j = 1
	for i in range (1, n + 1):
		j = i * j
	print j
print factorial_iterative(4)
