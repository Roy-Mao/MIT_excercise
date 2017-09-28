def multi_three(n):
	memo = {0:0, 1:3}
	if not n in memo:
		memo[n] = multi_three(n - 1) + 3
		return memo[n]
	else:
		return memo[n]
print multi_three()