from copy import deepcopy
from random import shuffle
import inspect
import random

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

	def getPile(self):
		return self.allCards[:52]

	def shuffleCards(self):
		shuffledDeck = deepcopy(self.allCards)
		shuffle(shuffledDeck)
		return shuffledDeck

	def numToChar(self, atuple):
		fChar = self.suit[atuple[0]]
		sChar = self.rank[atuple[1]]
		return (fChar, sChar)

	def charToNum(self, atuple):
		fnum = self.suit.index(atuple[0])
		snum= self.rank.index(atuple[1])
		return (fnum, snum)


class WithoutOneQueenDeck(Cards):
	def __init__(self, cards):
		copyFullDeck = deepcopy(self.allCards)
		for i, (d, q) in enumerate(copyFullDeck):
			if (d, q) == ('Clubs','Queen'):
				del copyFullDeck[i]
		self.allCards = deepcopy(copyFullDeck)

	def __repr__(self):
		return 'This is a 51 ready-deck without Queen of Clubs. You can shuffle the card using shuffleCards() method'

	def shuffleCards(self):
		anotherCopy = deepcopy(self.allCards)
		shuffle(anotherCopy)
		return anotherCopy

class Deck(Cards):
	def __init__(self, withoutonequeendeck):
		self.allCards = withoutonequeendeck.shuffleCards()

	def __repr__(self):
		return 'This is a shuffled 51 cards without one Queen of Club.'

	def pickCard(self):
		lastCardPicked = self.allCards.pop()
		return lastCardPicked

	def distribution(self, pnum):
		cardsList = self.allCards
		slist = [[] for _ in range(pnum)]
		for ind in range(len(cardsList)):
			item = cardsList[ind]
			remid = ind % pnum
			slist[remid].append(item)
		return slist

	def filterSingleList(self, alist):
		blist = []
		clist = []
		for a in alist:
			fnum = self.suit.index(a[0])
			snum = self.rank.index(a[1])
			blist.append((fnum, snum))
		for b in blist:
			j = blist.index(b) + 1
			for q in range(j, len(blist)):
				itemq = blist[q]
				if (itemq[1] == b[1]) and (itemq[0] + b[0] == 3):
					clist.append(b)
					clist.append(itemq)
		dlist = list(set(blist) -  set(clist))
		reVal = [clist, dlist]
		return reVal

	def removeDouble(self, nlist):
		fil = []
		for n in nlist:
			needDelete = []
			noDelete = []
			reVal = self.filterSingleList(n)
			for t in reVal[0]:
				needDele = self.numToChar(t)
				needDelete.append(needDele)
			for t in reVal[1]:
				noDele = self.numToChar(t)
				noDelete.append(noDele)
			result = (needDelete, noDelete)
			fil.append(result)
		return fil

		
def gameProcess(alist): #input should be a single list containing 3 sub-lists
	players = ['player1', 'player2', 'player3']
	listo = alist[0]
	listt = alist[1]
	listth = alist[2]
	elements = len(listo) + len(listt) + len(listth)
	i = 1
	while elements > 1:
		choose_person = i % 3
		print 'It is ' + players[choose_person - 1] + "'s turn, ready to pick a random card from " + players[choose_person]
		if choose_person != 0:
			choose_person_index = choose_person - 1
	    	chosen_person_index = choose_person_index + 1
		if choose_person == 0:
			choose_person_index = 2
			chosen_person_index = 0
		if len(alist[chosen_person_index]) == 0:
			print players[chosen_person_index] + 'has no card in hand.'
			chosen_person_index = (chosen_person_index + 1) % 3
			print 'Choose card from ' + players[chosen_person_index] 
		selectele = random.choice(alist[chosen_person_index])
		print str(selectele) + ' is selected..'
		alist[chosen_person_index].remove(selectele)
		nselectele = Cards().charToNum(selectele)
		numo = 3 - nselectele[0] 
		nums = nselectele[1]
		rselectele = Cards().numToChar((numo, nums)) 
		if rselectele in alist[choose_person_index]:
			print 'matches found, should discard both cards.'
			alist[choose_person_index].remove(rselectele)
		else:
			print 'no matches found, therefore ' + str(selectele) + 'is added into ' + players[choose_person_index] + "'s hand.." 
			alist[choose_person_index].append(selectele)
		i += 1
		elements = len(listo) + len(listt) + len(listth)
	for li in alist:
		if len(li) != 0:
			ind = alist.index(li)
			print 'The loser is ' + players[ind]


def playGame(player1, player2, player3):
	pnames = [player1, player2, player3]
	pnum = len(inspect.getargspec(playGame)[0])
	newCards = Cards()
	noqueenDeck = WithoutOneQueenDeck(newCards)
	gameDeck = Deck(noqueenDeck)

	slist = gameDeck.distribution(pnum)
	print '---------Cards have been dealt------------'
	for p in range(len(pnames)):
		print 'Hand ' + pnames[p] + ' contains: ' 
		print slist[p]

	fil = gameDeck.removeDouble(slist)
	print '----------Check double Cards and then Delete---------'
	for p in range(len(pnames)):
		if len(fil[p][0]) == 0:
			print pnames[p] + ' : no delete match found!'
		else:
			print pnames[p] + ': Deleting these cards: '
			print fil[p][0]

	print '-----------Remaining Cards----------------'
	for p in range(len(pnames)):
		print 'Hand ' + pnames[p] + ' has the following: '
		print fil[p][1]
		print ''

	print '-----------------First round begin-----------------'
	alist = []
	for p in range(len(pnames)):
		alist.append(fil[p][1])
	print gameProcess(alist)




	


playGame('Allen', 'Jeff', 'Chris')









