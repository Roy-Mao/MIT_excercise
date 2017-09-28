
#My way of doing it
from math import *
def prime_num_check(numTh):
	Lst = [2]
	number = 3
	while len(Lst) <= numTh:
		for i in range (2, number):
			if number % i == 0:
				number += 1
				break
			else:
				if (i == number - 1) and (number % i != 0):
					Lst.append(number)
					number += 1
				else:
					continue
	return Lst

def extra_exe(logNum):
	Lst = prime_num_check(logNum)
	sum = 0
	for item in Lst:
		if item <= logNum:
			val = log(item)
			sum += val
	result = sum / logNum
	return result
print extra_exe(30000)







"""
# result = 2
# count = 1
# for i in range (3, 8000):
# 	if i % 2 != 0:
# 		j = i
# 		if j == 3:
# 			m = 3
# 		else:
# 			m = (j + 1) / 2
# 		for n in range(2, m):
# 			if j % n == 0:
# 				break
# 			else:
# 				if (n == m - 1) and (j % n != 0):
# 					result = j
# 					count += 1
# 					if count == 1000:
# 						print result
# 				else:
# 					continue
"""
