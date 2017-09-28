#3.58 4.04
# for i in range(1, 21):
# 	answer = 1.0/i
# 	if i <= 9:
# 		print ('1/{:<2} = {:.3}'.format(i, answer))
# 	else:
# 		print ('1/{} = {:.4}'.format(i, answer))

#4.05
def re_fib(num):
	assert num >= 1, 'should be bigger than 1'
	dic = {1:1, 2:1}
	if num in dic:
		answer = dic[num]
	else:
		answer = re_fib(num - 1) + re_fib(num - 2)
		dic[num] = answer
	return answer

for i in range(1,36):
	answer = re_fib(i)
	if i >= 2 and i <= 9:
		print ('{:>2} -{:11,}'.format(i, answer))
	else:
		print ('{} -{:11,}'.format(i, answer))




