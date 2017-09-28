import random


def insertion_sort(alist):
	i = 0
	length = len(alist)
	while i < length - 1:
		j = i + 1
		pre_index = i
		after_index = j
		while alist[after_index] < alist[pre_index]:
			if pre_index == 0:
				temp = alist[pre_index]
				alist[pre_index] = alist[after_index]
				alist[after_index] = temp
				break
			temp = alist[pre_index]
			alist[pre_index] = alist[after_index]
			alist[after_index] = temp
			after_index = pre_index
			pre_index -= 1

		i += 1
	return alist

my_list = []
for a in range(10):
	my_list.append(random.randrange(100))

print my_list
insertion_sort(my_list)
print my_list



