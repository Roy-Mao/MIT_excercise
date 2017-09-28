alist = [8,3,6,2,1,6,8,9,0,11,23,45,69]

def c_sort(alist):
	# find the biggest value in the list
	max_val = max(alist)
	ind_list_length = max_val + 1
	ind_list = [0] * ind_list_length
	inc_list = [0] * ind_list_length
	flist = [0] * (len(alist))
	for a in alist:
		ind_list[a] += 1
	for i, v in enumerate(ind_list):
		if i == 0:
			inc_list[0] = ind_list[0]
		else:
			inc_list[i] = inc_list[i - 1] + ind_list[i]
	for a in alist:
		inc_list[a] -= 1
		flist[inc_list[a]] = a
	print flist





	


c_sort(alist)