
import itertools, time
def get_solutions():
	t0 = time.clock()
	solution = []
	alist = [0,1,2,3,4,5,6,7,8,9]
	aplist = list(itertools.permutations(alist))
	for a in aplist:
		done = False
		blist = list(a)
		Length = len(blist)
		for i, v in enumerate(blist):
			next_ind = i + 1
			for x in range(next_ind, Length):
				if abs(x-i) == abs(blist[x]-v):
					done = True
					break
			if done:
				break
		if done:
			continue
		else:
			solution.append(blist)
	t1 = time.clock()
	td = t1 - t0
	print td
	return solution
print len(get_solutions())





