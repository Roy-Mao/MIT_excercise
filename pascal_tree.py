def pascal(n):
	if n == 1:
		return [1]
	else:
		new_level = [1]
		previous_level = pascal(n - 1)
		num_circle = len(previous_level) - 1
		if num_circle > 0:
			for i in range (num_circle):
				new_level.append(previous_level[i] + previous_level[i + 1])
		new_level.append(1)
		return new_level
def loop_pascal(n):
	for i in range (n):
		print pascal(i + 1)
loop_pascal(100)
