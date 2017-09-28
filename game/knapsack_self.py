w = [23, 31, 29, 44, 53, 38, 63, 85, 89, 82]
v = [92, 57, 49, 68, 60, 43, 67, 84, 87, 72]
rw = 165
i = 0
count = 0
def d_c(w, v, i, rw, count):
	if rw == 0 or i == len(w):
	    return count
	if rw < w[i]:
		return d_c(w, v, i+1, rw, count)
	else:
		left = d_c(w, v, i+1, rw-w[i], count+v[i])
		right = d_c(w, v, i+1, rw, count)
	return max(left, right)
print d_c(w, v, i, rw, count)


