#4.36  4.39
def recur_one(num):
	dic = {1:6}
	if num in dic:
		return dic[num]
	else:
		answer = 1.0 / 2 * recur_one(num - 1) + 4
		dic[num] = answer
		return answer

for i in range(1, 11):
	answer = recur_one(i)
	print ('n= {0} , a= {1}'.format(i, answer))