# 11:52  11:55  12:09  12:15
class Node(object):
	def __init__(self, cargo, next = None):
		self.cargo = cargo
		self.next = next
	def __str__(self):
		if type(self.cargo) == type('a'):
			return "'{0}'".format(self.cargo)
		else:
			return str(self.cargo)
	def printList(self):
		while self is not None:
			print self,
			self = self.next

	def printBackward(self):
		if self.next is not None:
			head = self
			tail = self.next
			tail.printBackward()
		print self,

	def removeSecond(self):
		if self == None:
			return 
		first = self
		second = self.next
		first.next = second.next
		second.next = None
		return second

class linkedList(object):
	def __init__(self):
		self.length = 0
		self.head = None
	def addFirst(self, cargo):
		node = Node(cargo)
		node.next = self.head
		self.head = node
		self.length += 1
	def printList(self):
		if self.head is None:
			print '[]'
			return '[]'
		print '[',
		self.head.printList()
		print ']'
	def printBackward(self):
		if self.head is None:
			print '[]'
			return '[]'
		print '[',
		self.head.printBackward()
		print ']'

class Queue(object):
	def __init__(self):
		self.length = 0
		self.head = None
		self.tail = None
	def is_empty(self):
		return (self.length == 0)
	def insert(self, cargo):
		node = Node(cargo)
		if self.length == 0:
			self.head = self.tail = node
		else:
			last = self.tail 
			last.next = node
			self.tail = node
		self.length += 1
	def remove(self):
		cargo = self.head.cargo
		self.head = self.head.next
		self.length -= 1
		if self.length == 0:
			self.tail = None
		return cargo



