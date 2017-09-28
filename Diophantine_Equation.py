def find_six(a):
	i = 0
	count = 0
	while i+1 < len(a):
		if a[i+1] - a[i] == 1:
			count += 1
			if count == 5:
				return "yes"
			i += 1
		else:
			count = 0
			i += 1
	if i+1 == len(a):
		return "No"


def dio_equation(i, p, q):
	Lst = []
	changeNum = 0
	n = 1
	done = False
	while n <= 200:
		for a in range(100):
			for b in range(100):
				for c in range(100):
					sum = i * a + p * b + q * c
					if sum == n:
						Lst.append(n)
						result = find_six(Lst)
						if result == "yes":
							return "Given pachage sizes <" + str(i) + ">, <" + str(p) + ">, <" + str(q) + "> Largest number that can not be bought in exact quantity is: " + str(changeNum)  
						n += 1
						done = True
						break
					else:
						continue
				if done:
					break
			if done:
				break
		if done:
			done = False
		else:
			changeNum = n
			n += 1

print dio_equation(6,13,15)


					

