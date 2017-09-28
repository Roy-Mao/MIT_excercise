class Cards(object):
	rank = ['none', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
	suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
	allCards = []
	def __init__(self):
		for r in range(1, len(self.rank)):
			for s in self.suit:
				oneCard = (s, self.rank[r])
				self.allCards.append(oneCard)

	def __repr__(self):
		return 'This is a normal deck with 52 different cards. Use allCards attribute to see the full list of chards.'

		





myCards = Cards()
print myCards.allCards


