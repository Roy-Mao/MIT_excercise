class Tree(object):
	def __init__(self, cargo, left = None, right = None):
		self.cargo = cargo
		self.left = left
		self.right = right
	def __str__(self):
		return str(self.cargo)

def yes(ques):
	ans = raw_input(ques).lower()
	return ans[0] == 'y'

def the_game():
	root = Tree('bird')
	while True:
		print 
		if not yes('Are you thinking about an animal?'):
			break
		tree = root
		while tree.left is not None:
			if yes(tree.cargo):
				tree = tree.right
			else:
				tree = tree.left
		if tree.left is None:
			prompt = 'Is it a {0}'.format(tree.cargo)
			if yes(prompt):
				print 'I got it.'
			else:
				prompt = 'What animal?'
				animal = raw_input(prompt)
				prompt = 'how to distinguish?'
				distin = raw_input(prompt)
				prompt = 'can it do it'
				answer = raw_input(prompt)
				guess = tree.cargo
				tree.cargo = distin
				if answer == 'y':
					tree.right = Tree(animal)
					tree.left = Tree(guess) 
				else:
					tree.left = Tree(animal)
					tree.right = Tree(guess)
the_game()




