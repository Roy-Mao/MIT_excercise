
def format_tree(alist):
	for a in alist:
		print a,
	print

def show_tree():
	start = 0
	alist = []
	for i in range(10, 55):
		alist.append(i)
	for a in range(9):
		length = a + 1
		end = start + length
		slist = alist[start:end]
		format_tree(slist)
		start = end 

show_tree()







 	
