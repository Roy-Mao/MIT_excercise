#3:26
from string import punctuation

def odd_single(num):
	alist = []
	count = 0
	length = 0
	while length < num:
		if count % 2 != 0:
			alist.append(count)
		count += 1
		length = len(alist)
	return alist

def odd_multi(num):
	alist = odd_single(num)
	length = len(alist)
	start = 0
	savelist = []
	while length >= 1:
		clist = alist[start:]
		for i in range(start):
			clist.append(0)
		rlist = clist[::-1]
		flist = clist + rlist
		savelist.append(flist)
		my_string = ''.join(c for c in str(flist) if c not in punctuation)
		print my_string.replace('0',' ')
		start += 1
		length -= 1
	blist = savelist[::-1]
	for b in blist:
		b_string = ''.join(c for c in str(b) if c not in punctuation)
		print b_string.replace('0', ' ')

def filter(alist):
	for a in alist:
		print a,

odd_multi(5)






