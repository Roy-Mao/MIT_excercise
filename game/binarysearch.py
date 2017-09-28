def binary_search_none(alist, key):
	length = len(alist)
	lower_bound = 0
	upper_bound = length - 1
	middle_index = (lower_bound + upper_bound) // 2
	while alist[middle_index] != key and upper_bound - lower_bound > 1:
		if alist[middle_index] > key:
			upper_bound = middle_index - 1
		if alist[middle_index] < key:
			lower_bound = middle_index + 1
		middle_index = (upper_bound + lower_bound) // 2
	if key == alist[lower_bound]:
		print 'The index of the data is: ' + str(lower_bound)
	elif key == alist[upper_bound]:
		print 'The index of the data is: ' + str(upper_bound)
	elif key ==alist[middle_index]:
		print 'The index of the data is: ' + str(middle_index)
	else:
		print 'no data found'

alist = [1,2,3,4,5,6,8]

def binary_search_recursive(alist, key):
	length = len(alist):
	


binary_search_recursive(alist, 5)


