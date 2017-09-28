def recursive_sum(n):
	memo = {1:1, 2:3}
	if not n in memo:
		memo[n] = n + recursive_sum(n - 1)
		return memo[n]
	else:
		return memo[n]
print recursive_sum(4)