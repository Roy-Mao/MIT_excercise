def fib_memoization(n):
	memo = {1:1, 2:1}
	if not n in memo:
		memo[n] = fib_memoization(n - 2) + fib_memoization(n - 1)
		return memo[n]
	else:
		return memo[n]
print fib_memoization(8)

#1 1 2 3 5 8 13 21 34 55 