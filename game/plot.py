import matplotlib.pyplot as plt
import numpy as np

m = [1,2,3,4,5,6,7,8,9,10]
n = [0,4,5,7,8,9,2,3,4,6]
p = [m,n]
alist = []
Length = len(m)
sum = 0
for i in range(Length):
	sum = 0
	for item in p:
		sum += item[i]
	average = round((float(sum) / 3), 5) 
	print average


