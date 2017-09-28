
# starting time 11:17
import random
def select_sort(alist):
	i = 0
	length = len(my_list)
	while i < length:
		min_index = i
		min_val = alist[i]
		j = i + 1
		for n in range(j, length):
			if alist[n] < min_val:
				min_val = alist[n]
				min_index = n
		temp = alist[i]
		alist[i] = min_val
		alist[min_index] = temp
		i += 1
	return alist

def print_list(my_list):
	for item in my_list:
		print item,
	print 

my_list = []
for i in range(10):
	my_list.append(random.randrange(100))

print_list(my_list)
select_sort(my_list)
print_list(my_list)




