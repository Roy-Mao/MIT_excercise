import random
rank = ['none', 'Ace', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King']
suit = ['Spades', 'Clubs', 'Diamonds', 'Hearts']
alist = [('Diamonds', 'King'), ('Spades', 'Queen'), ('Clubs', '5'), ('Clubs', '4'), ('Spades', '5'), ('Spades', '7'), ('Clubs', 'Ace'), ('Clubs', '8'), ('Spades', '10'), ('Clubs', '7'), ('Clubs', '3'), ('Clubs', '9'), ('Clubs', 'Jack'), ('Diamonds', '4'), ('Spades', '9'), ('Clubs', '10'), ('Diamonds', '7')]

list1 = [('Hearts', 'Ace'), ('Spades', '6'), ('Clubs', '8'), ('Clubs', '6'), ('Spades', '10'), ('Clubs', '9'), ('Spades', '3'), ('Diamonds', '4'), ('Hearts', '5')]
list2 = [('Spades', 'Ace'), ('Diamonds', '6'), ('Diamonds', '8'), ('Spades', 'King'), ('Diamonds', 'Ace'), ('Spades', 'Queen'), ('Hearts', '8'), ('Hearts', '9'), ('Clubs', '4'), ('Hearts', '4'), ('Diamonds', 'Queen')]
list3 = [('Hearts', 'Queen'), ('Hearts', '3'), ('Diamonds', '9'), ('Hearts', 'King'), ('Hearts', '10'), ('Spades', '5'), ('Hearts', '6'), ('Spades', '4'), ('Spades', '9'), ('Spades', '8'), ('Clubs', 'Ace')]
hlist = [list1, list2, list3]

players = ['player1', 'player2', 'player3']



def charToNum(atuple):
	fnum = suit.index(atuple[0])
	snum= rank.index(atuple[1])
	return (fnum, snum)

def numToChar(atuple):
	fChar = suit[atuple[0]]
	sChar = rank[atuple[1]]
	return (fChar, sChar)



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
		nselectele = charToNum(selectele)
		numo = 3 - nselectele[0] 
		nums = nselectele[1]
		rselectele = numToChar((numo, nums)) 
		if rselectele in alist[choose_person_index]:
			print 'matches found, should discard both cards.'
			alist[choose_person_index].remove(rselectele)
		else:
			print 'no matches found, therefore ' + str(selectele) + 'is added into ' + players[choose_person_index] + "'s hand.." 
			alist[choose_person_index].append(selectele)
		i += 1
		elements = len(listo) + len(listt) + len(listth)
	return alist
print gameProcess(hlist)








