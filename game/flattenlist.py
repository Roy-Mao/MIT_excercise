# 450  457
def flatten(anlist):
	blist = []
	for a in anlist:
		if type(a) == type([]):
			blist += flatten(a)
		else:
			blist.append(a)
			print blist
	return blist
print flatten([1,['sam'],2,[(0,-1)],[[3],-89],4,5,6,7])
