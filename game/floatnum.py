alist = [1,2,6]
blist = [0,1,1,3]
dlist = [1,3,2,5,7,6,9,10,23,31,0]

def mtl(alist, blist):
	length_a = len(alist)
	length_b = len(blist)
	clist = []
	while(length_a != 0 and length_b != 0):
		if alist[0] <= blist[0]:
			clist.append(alist[0])
			del alist[0]
			length_a -= 1
		else:
			clist.append(blist[0])
			del blist[0]
			length_b -= 1
	if length_a == 0:
		for b in blist:
			clist.append(b)
	if length_b == 0:
		for a in alist:
			clist.append(a)
	return clist

def ms(dlist):
	length_d = len(dlist)
	if length_d <= 1:
		return dlist
	else:
		mid = length_d / 2
		left = ms(dlist[:mid])
		right = ms(dlist[mid:])
		result = mtl(left, right)
		return result


print ms(dlist)









