def convert(node):
	if type(node.cargo) == type('a'):
		return "'{0}'".format(node.cargo)
	else:
		return node.cargo

class Node(object):
	def __init__(self, cargo = None, next = None):
		self.cargo = cargo
		self.next = next
	def __str__(self):
		return str(self.cargo)

	def print_list(self):
		while self is not None:
			if type(self.cargo) == type('a'):
				print "'{0}'".format(self),
			else:
				print self,
			self = self.next


	def print_backward(self):
		head = self
		if self.next is not None:
			tail = self.next
			tail.print_backward()
		if type(self.cargo) == type('a'):
			print "'{0}'".format(self),
		else:
			print self,

	def get_index(self,d):
		count = 0
		while self.cargo != d:
			count += 1
			self = self.next
			if self is None:
				count = -1
		return count


	def remove_ele1(self,index):
		count = 0
		while count != index:
			count += 1
			pre_node = self
			self = self.next
		if count != 0:
			this_node = self
			pre_node.next = this_node.next
			this_node.next = None
		else:
			this_node = self
			self.next = None
		return convert(this_node)

	def remove_ele2(self, cargo):
		count = 0
		while self.cargo != cargo:
			count += 1
			pre_node = self
			self = self.next
		if count != 0:
			this_node = self
			pre_node.next = this_node.next
			this_node.next = None
		else:
			this_node = self
			self.next = None
		return convert(this_node)

class LinkedList(object):
	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None
	def addNode(self,cargo):
		new_node = Node(cargo)
		if self.head == None:
			self.head = new_node
			self.tail = new_node
		else:
			self.tail.next = new_node
			self.tail = new_node
			self.tail.next = None
		self.length += 1

	def print_list(self):
		if self.head is None:
			print '[]'
		else:
			print '[',
			self.head.print_list()
			print ']'

	def print_backward(self):
		if self.head is None:
			print '[]'
		else:
			print '[',
			self.head.print_backward()
			print ']'

	def get_index(self,d):
		return self.head.get_index(d)


alist = LinkedList()
alist.addNode(1)
alist.addNode(2)
alist.addNode(3)
alist.addNode('a')
alist.addNode('b')
alist.addNode('c')
alist.print_list()
alist.print_backward()
print alist.get_index('a')
print alist.length