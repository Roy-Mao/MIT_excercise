# 10:43
import re
class Stack(object):
	def __init__(self):
		self.items = []
	def push(self, item):
		self.items.append(item)
	def pop(self):
		return self.items.pop()
	def is_empty(self):
		return (self.items == [])

def val_postfix(expre):
	token_list = re.split('([^0-9])',expre)
	s = Stack()
	for t in token_list:
		if t == '' or t == ' ':
			continue
		if t == '+':
			sum = s.pop() + s.pop()
			s.push(sum)
		elif t == '*':
			product = s.pop() * s.pop()
			s.push(product)
		else:
			s.push(int(t))
	return s.pop()
print val_postfix('56 47 + 2 *')


