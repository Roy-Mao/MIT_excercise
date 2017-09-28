#----------------------------------------#
"""
Question:

Write a program to compute 1/2+2/3+3/4+...+n/n+1 with a given n input by console (n>0).

Example:
If the following n is given as input to the program:

5

Then, the output of the program should be:

3.55

In case of input data being supplied to the question, it should be assumed to be a console input.

Hints:
Use float() to convert an integer to a float

Solution:

n=int(raw_input())
sum=0.0
for i in range(1,n+1):
    sum += float(float(i)/(i+1))
print sum


#----------------------------------------#
"""

dictionary = {1:float(1)/2}
def computation(num):
	if num in dictionary:
		return dictionary[num]
	else:
		dictionary[num] = float(num)/(num+1) + computation(num -1)
		return dictionary[num]
print computation(100)







