hand = {'y':2, 'q':1, 'e':2, 'g':2}
SCRABBLE_LETTER_VALUES = {
    'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}
points_dict = {}
rearrange_dict = {}
WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # wordlist: list of strings
    wordlist = []
    for line in inFile:
        wordlist.append(line.strip().lower())
    print "  ", len(wordlist), "words loaded."
    return wordlist

def get_words_to_points(word_list):
    for word in word_list:
        totVal = 0
        for letter in word:
            letterVal = SCRABBLE_LETTER_VALUES[letter]
            totVal += letterVal
        points_dict[word] = totVal


def get_word_rearrangements(word_list):
    for w in word_list:
        sum = ''
        sort_w = sorted(w)
        for i in sort_w:
            sum += i
        rearrange_dict[sum] = w


def display_hand(hand):
    """
    Displays the letters currently in the hand.

    For example:
       display_hand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
            print letter,              # print all on the same line
    print  


def update_hand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not mutate hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ...
    word.lower()
    new_hand = {}
    for element in hand.keys():
        for letter in word:
            if element == letter:
                val = hand[element] - 1
                hand[element] = val
                if hand[element] > 0:
                    continue
                else:
                    break
            else:
                continue
        if hand[element] > 0:
            new_hand[element] = hand[element]
        else:
            continue
    return new_hand


def count_letter(word,letter):#count how many letters appear in the word
	count = 0
	for i in word:
		if i == letter:
			count += 1
	return count

def pick_best_word(hand, points_dict):
    """
    Return the highest scoring word from points_dict that can be made 
    with the given hand.Return '.' if no words can be made with the 
    given hand. 
    """
    max_val = 0
    test_list = []
    final_list = []
    my_list = points_dict.keys()[:]
    another_list = points_dict.keys()[:]
    for i in my_list:     #get the key-word item in the dict
        for letter in i:           #iterate through the letters in the word
            if not letter in hand.keys():
                another_list.remove(i)
                break     #I will get a new dic must contain keys in hand
    if len(another_list) == 0:
        return '.'
    for j in hand.keys():          # loop the key-word in hand dict
        for i in another_list:       # loop the word-key item in scruded new dict
            count = count_letter(i, j)
            if count > hand[j]:
                if not i in test_list:
                    test_list.append(i)
                else:
                    continue
    for m in another_list:
        if not m in test_list:
            final_list.append(m)
    if len(final_list) == 0:
        return '.'
    for n in final_list:
        points = points_dict.get(n)
        if points >= max_val:
            max_val = points 
            max_key = n
    return max_key

def pick_best_word_faster(hand, rearrange_dict):
    # To find some word that can be made out of the letters in HAND:
    #  For each subset S of the letters of HAND:
    #      Let w = (string containing the letters of S in sorted order)
    #      If w in d: return d[w]
    conj = ''
    for letter in hand.keys():
        for j in range(hand[letter]):
            conj += letter
    hand_key_list = sorted(conj)
    while len(hand_key_list) > 0:
        sum = ''
        for n in hand_key_list:
            sum += n
            print sum
            if sum in rearrange_dict:
                return rearrange_dict[sum]
        hand_key_list.remove(hand_key_list[0])
    return '.'







word_list = load_words()
get_words_to_points(word_list)
get_word_rearrangements(word_list)
print pick_best_word_faster(hand,rearrange_dict)

