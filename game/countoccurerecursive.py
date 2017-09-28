# returns the number of ocurences of target in a nested list
# 4:39 4:48
def count(anestlist,target):
	tot = 0
	for a in anestlist:
		if type(a) == type([]):
			tot += count(a, target)
		else:
			if a == target:
				tot += 1
	return tot

print count([1,2,3,4,[5,[[0]],5],5,3,4,4], 0)
