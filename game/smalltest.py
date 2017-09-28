alist = [3,1,6,4,2,5]
blist = ['c', 'a', 'f', 'd', 'b', 'e']
def sort_double_list(alist, blist):
	dlist = []
	adict = {}
	for a in range(len(alist)):
		adict[alist[a]] = blist[a]
	clist = adict.keys()
	clist.sort()
	for c in clist:
		dlist.append(adict[c])
	print clist
	print dlist

sort_double_list(alist, blist)
