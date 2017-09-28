# 4*33  4:38
def recursive_min(alist):
	minval = None
	first_time = True
	for a in alist:
		if type(a) == type(0):
			if a < minval:
				minval = a
		else:
			a = recursive_min(a)
		if first_time or a < minval:
			minval = a
			first_time = False
	return minval

print recursive_min([[-8],1,2,3,4,[0,[[-5]],5],6,7])


